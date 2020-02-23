# ============================================================================ #
#                                                                              #
#    This is part of the "GrainSizeTools Script"                               #
#    A Python script for characterizing grain size from thin sections          #
#    and paleopiezometry estimates based on grain size.                        #
#                                                                              #
#    Copyright (c) 2014-present   Marco A. Lopez-Sanchez                       #
#                                                                              #
#    Licensed under the Apache License, Version 2.0 (the "License");           #
#    you may not use this file except in compliance with the License.          #
#    You may obtain a copy of the License at                                   #
#                                                                              #
#        http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                              #
#    Unless required by applicable law or agreed to in writing, software       #
#    distributed under the License is distributed on an "AS IS" BASIS,         #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#    See the License for the specific language governing permissions and       #
#    limitations under the "License".                                          #
#                                                                              #
#    Version 3.0                                                               #
#    For details see: http://marcoalopez.github.io/GrainSizeTools/             #
#    download at https://github.com/marcoalopez/GrainSizeTools/releases        #
#                                                                              #
# ============================================================================ #

# Imports
from scipy.stats import bayes_mvs, gaussian_kde, iqr, t, norm
import tools as tools
import numpy as np

# ============================================================================ #
# AVERAGES                                                                     #
# ============================================================================ #


def amean(pop, ci=0.95, method='CLT'):
    """ Returns the arithmetic mean, the Bessel corrected SD,
    and the confidence interval based on the chosen method.

    Parameters
    ----------
    pop : array-like
        the population

    ci : float, scalar between 0 and 1
        the confidence interval, default = 0.95

    method : string
        the method to estimate the confidence interval, either
        'CLT': central limit theorem based (ASTM default)
        'GCI': generalized confidence interval method
        'mCox': modified Cox method

    Assumptions
    -----------
    - arithmetic mean is optimal for normal-like distributions
    - CLT confidence interval is optimized for normal distributions
    - GCI and mCox methods are optimized for lognormal distributions

    Call functions
    --------------
    - CLT_ci
    - GCI_ci
    - mCox_ci

    Returns
    -------
    the arithmetic mean,
    the SD (Bessel corrected),
    the confidence interval (scalar or tuple)
    the confidence interval length (float),
    """

    n = len(pop)
    mean, std = np.mean(pop), np.std(pop, ddof=1)  # SD using n-1 degrees of freedom (Bessel corrected)

    # confidence interval
    if method == 'CLT':
        conf_int, length = CLT_ci(mean, std, n, ci)
        return mean, std, conf_int, length

    elif method == 'GCI':
        ci_limis, length = GCI_ci(pop, ci)
        return mean, std, ci_limis, length

    elif method == 'mCox':
        ci_limis, length = mCox_ci(pop, ci)
        return mean, std, ci_limis, length

    else:
        raise Exception("ci methods must be 'CLT', 'GCI', or 'mCox'")


def gmean(pop, ci=0.95, method='CLT'):
    """ Returns the geometric mean, the multiplicative (geometric) SD,
    and the confidence interval.

    Parameters
    ----------
    pop : array-like
        the population

    ci : float, scalar between 0 and 1
        the confidence interval, default = 0.95

    method : string
       the method to estimate the confidence interval, either
        'CLT': Central limit theorem based
        'bayes': Bayesian based

    Assumptions
    -----------
    - geometric mean is optimal for lognormal-like distributions
    - the multiplicative SD is a measure of the lognormal shape of
    the distribution
    - The bayes method is slighly superior to CLT for very small (< 30)
    sample sizes

    Call functions
    --------------
    - CLT_ci
    - bayesian_ci

    Returns
    -------
    the geometric mean,
    the multiplicative SD (MSD),
    the confidence interval (tuple),
    the confidence interval length (float),
    """

    # compute statistics of the log-transformed data
    mean_log, n = np.mean(np.log(pop)), len(pop)
    std_log = np.std(np.log(pop), ddof=1)  # Bessel corrected SD (n-1 degrees of freedom)

    # compute the back-transformed values (gmean and mSD in linear scale)
    gmean = np.exp(mean_log)
    mSD = np.exp(std_log)

    # confidence intervals of the back-transformed values
    if method == 'CLT':
        ci_limis, length = CLT2_ci(mean_log, std_log, n, ci)
        return gmean, mSD, ci_limis, length

    elif method == 'bayes':
        ci_limis, length = bayesian_ci(pop, ci)
        return gmean, mSD, ci_limis, length

    else:
        raise Exception("CI methods must be 'CLT' or 'bayes'")


def median(pop, ci=0.95):
    """ Returns the median, the interquartile length, and the
    confidence intervals for the median based on th rule-of-
    thumb method of Hollander and Wolfe (1999).

    Parameters
    ----------
    pop : array-like
        the population

    ci : float, scalar between 0 and 1
        the confidence interval, default = 0.95

    Assumptions
    -----------
    - median is optimal for both normal and lognormal-like distributions.
    It behaves better than the means when data contamination is expected.
    - the interquertile length/range is a measure of the spread of
    the distribution

    Reference
    ---------
    Hollander and Wolfe (1999) Nonparametric Statistical Methods.
    3rd ed. John Wiley, New York. 787 pp.

    Call functions
    --------------
    - norm.ppf and iqr from Scipy

    Returns
    -------
    the median (float),
    the interquartile range,
    the confidence interval (tuple),
    the confidence length (float)
    """
    pop, n = np.sort(pop), len(pop)
    median, iqr_range = np.median(pop), iqr(pop)

    # compute confidence intervals
    ci_limis, length = median_ci(pop, n, ci=0.95)

    return median, iqr_range, ci_limis, length


def calc_freq_peak(diameters, bandwidth, max_precision):
    """ Returns the peak of the frequency ("mode") of a continuous
    distribution based on the Gaussian kernel density estimator. It
    uses Scipy's gaussian kde method.

    Parameters
    ----------
    diameters : array_like
        the diameters of the grains

    bandwidth : string, positive scalar or callable
        the method to estimate the bandwidth or a scalar directly defining the
        bandwidth. Methods can be 'silverman' or 'scott'.

    max_precision : positive scalar
        the maximum precision expected for the "peak" estimator.

    Call functions
    --------------
    - gen_xgrid from tools
    - kde (from scipy)

    Returns
    -------
    the x and y values to contruct the kde,
    the mode or peak grain size,
    the density value of the peak,
    the bandwidth
    """

    # check bandwidth and estimate Gaussian kernel density function
    if isinstance(bandwidth, (int, float)):
        bw = bandwidth / np.std(diameters, ddof=1)
        kde = gaussian_kde(diameters, bw_method=bw)

    elif isinstance(bandwidth, str):
        kde = gaussian_kde(diameters, bw_method=bandwidth)
        bw = round(kde.covariance_factor() * diameters.std(ddof=1), 2)

    else:
        raise ValueError("bandwidth must be integer, float, or plug-in methods 'silverman' or 'scott'")

    # locate and get the frequency peak
    xgrid = tools.gen_xgrid(diameters.min(), diameters.max(), max_precision)
    densities = kde(xgrid)
    y_max, peak_grain_size = np.max(densities), xgrid[np.argmax(densities)]

    return xgrid, densities, peak_grain_size, y_max, bw


# ============================================================================ #
# CONFIDENCE INTERVAL METHODS                                                  #
# ============================================================================ #


def CLT_ci(amean, std, n, ci=0.95):
    """ Estimate the error margin for the arithmetic mean based
    on the central limit theorem and the t-statistics. This is
    the method describet in the ASTM norm E112-12.

    Parameters
    ----------
    amean : scalar, float
        the arithmetic mean of the population

    std : scalar, float
        the standard deviation of the population

    n : scalar, positive int
        the sample size

    ci : float, scalar between 0 and 1
        the confidence interval, default = 0.95

    Reference
    ---------
    ASTM-E112-12 (1996) Standard test methods for determining
    average grain size.

    Call
    ----
    calc_t

    Returns
    -------
    the lower and upper confidence intervals (tuple)
    the interval length (scalar)
    """
    t_score = critical_t(confidence=ci, sample_size=n)
    err = t_score * std / np.sqrt(n)

    lower, upper = amean - err, amean + err
    interval = upper - lower

    return (lower, upper), interval


def CLT2_ci(mean_log, std_log, n, ci=0.95):
    """ Returns the error margin for the geometric mean based
    on the central limit theorem and the t-statistics.

    Parameters
    ----------
    mean_log : scalar, float
        the arithmetic mean of the log-transformed data

    std_log : scalar, float
        the standard deviation of the log-transformed data

    n : scalar, positive int
        the sample size

    ci : float, scalar between 0 and 1
        the confidence interval, default = 0.95

    Reference
    ---------
    ASTM-E112-12 (1996) Standard test methods for determining
    average grain size.

    Call
    ----
    calc_t

    Returns
    -------
    the lower and upper confidence intervals (tuple)
    the interval length (scalar)
    """
    t_score = critical_t(ci, n)

    upper_ci = np.exp(mean_log + t_score * (std_log / np.sqrt(n)))
    lower_ci = np.exp(mean_log - t_score * (std_log / np.sqrt(n)))
    interval = upper_ci - lower_ci

    return (lower_ci, upper_ci), interval


def mCox_ci(data, ci=0.95):
    """ Returns the error margin for the arithmetic mean using the modified
    Cox method. This is a method optimized from lognormal populations. The
    method implemented below uses the Bessel corrected SD as it produces
    safer/robust results for small sample sizes

    Parameters
    ----------
    data : array_like
        the dataset

    ci : float, scalar between 0 and 1
        the confidence interval, default = 0.95

    Reference
    ---------
    Anderson....
    Lopez-Sanchez (2020)

    Call
    ----
    calc_t

    Returns
    -------
    the lower and upper confidence intervals (tuple)
    the interval length (scalar)
    """

    n = len(data)
    t = critical_t(confidence=ci, sample_size=n)
    data = np.log(data)
    mean_log, std_log = np.mean(data), np.std(data, ddof=1)

    lower = np.exp(mean_log + 0.5 * std_log**2 - t * (std_log / np.sqrt(n)) * np.sqrt(1 + (std_log**2 * n) / (2 * (n + 1))))
    upper = np.exp(mean_log + 0.5 * std_log**2 + t * (std_log / np.sqrt(n)) * np.sqrt(1 + (std_log**2 * n) / (2 * (n + 1))))
    interval = upper - lower

    return (lower, upper), interval


def GCI_ci(data, ci=0.95, runs=10000):
    """ Ruturns the confidence interval for the arithmetic mean using the
    generalized confidence interval (GCI) method (Krishnamoorthy and Mathew,
    2003). This is a Monte Carlo method optimized for lognormal populations.

    Parameters
    ----------
    data : array_like
        the dataset

    ci : float, scalar between 0 and 1
        the confidence interval, default = 0.95

    runs : integer, default=10000
        the number of (Monte Carlo) iterations to generate z and u**2 values

    Reference
    ---------
    Krishnamoorthy and Mathew (2003) https://doi.org/10.1016/S0378-3758(02)00153-2

    Assumptions
    -----------
    - The population follows a lognormal distribution

    Call
    ----
    GCI_equation

    Returns
    -------
    the lower and upper confidence intervals (tuple)
    the interval length (scalar)
    """

    # estimate the log-transformed population y = ln(x) and the degrees of freedom
    data = np.log(data)
    mu_log, var_log, n = np.mean(data), np.var(data), len(data)
    ddof = n - 1
    alpha = 0.05

    # Generate random values from the normal N(0,1) distribution
    z_array = np.random.normal(loc=0, scale=1.0, size=runs)

    # Generate random values from (non-central) chi-square distribution
    # with n-1 degrees of freedom
    u2_array = np.random.noncentral_chisquare(df=ddof, nonc=0, size=runs)
    u_array = np.sqrt(u2_array)

    # Compute the test statistic T values and sort them
    T_array = GCI_equation(mu_log, var_log, z_array, u_array, n)
    T_array = np.sort(T_array)

    # Estimate confidence limits
    lower = np.percentile(T_array, 100 * (alpha / 2))
    upper = np.percentile(T_array, 100 * (1 - (alpha / 2)))
    interval = upper - lower

    return (lower, upper), interval


def GCI_equation(mu_log, var_log, z, u, n):
    """ Generalized confidence interval (GCI) equation.

    Parameters
    ----------
    mu_log : integer, float
        the mean of the log-transformed population
    var_log : integer, float
        the variance of the log-transformed population
    z : array-like
        random values of the normal N(0,1) distribution
    u : array-like
        random values of the chi-square distribution with n-1 degrees
        of freedom
    n : integer, float
        size of the dataset

    Returns
    -------
    scalar or array-like
    """

    # estimate the second and third terms of the equation
    second_term = (z / (u / np.sqrt(n - 1))) * (np.sqrt(var_log) / np.sqrt(n))
    third_term = 0.5 * var_log / (u**2 / (n - 1))

    return np.exp(mu_log - second_term + third_term)


def bayesian_ci(data, ci=0.95):
    """ Use a bayesian approach to estimate the confidence intervals
    of the geometric mean. It uses the scipy bayes_msv routine over
    the log-transformed data and then estimate the back-transformed
    values.

    Parameters
    ----------
    data : array_like
        the dataset

    ci : float, scalar between 0 and 1
        the confidence interval, default = 0.95

    Reference
    ---------
    Oliphant (2006) https://scholarsarchive.byu.edu/facpub/278

    Assumptions
    -----------
    - The population follows a lognormal distribution

    Call
    ----
    bayes_mvs from scipy.stats module

    Returns
    -------
    the lower and upper confidence intervals (tuple)
    the interval length (scalar)
    """

    data = np.log(data)
    mu_log, var_log, SD_log = bayes_mvs(data, alpha=ci)
    mu, (lower_log, uppper_log) = mu_log
    lower, upper = np.exp(lower_log), np.exp(uppper_log)
    interval = upper - lower

    return (lower, upper), interval


def median_ci(pop, n, ci=0.95):
    """ Estimate the approximate ci 95% error margins for the median
    using a rule of thumb based on Hollander and Wolfe (1999).

    Parameters
    ----------
    pop : numpy array
        a sorted dataset

    n : scalar, positive int
        the sample size

    ci : float, scalar between 0 and 1
        the confidence interval, default = 0.95

    Reference
    ---------
    Hollander and Wolfe (1999) Nonparametric Statistical Methods.
    3rd ed. John Wiley, New York. 787 pp.

    Call
    ----

    Returns
    -------
    the lower and upper confidence intervals (tuple)
    the interval length (scalar)
    """

    z_score = norm.ppf(1 - (1 - ci) / 2)  # two-tailed z score

    id_upper = 1 + (n / 2) + (z_score * np.sqrt(n)) / 2
    id_lower = (n / 2) - (z_score * np.sqrt(n)) / 2
    upper_ci, lower_ci = pop[int(np.ceil(id_upper))], pop[int(np.floor(id_lower))]
    interval = upper_ci - lower_ci

    return (lower_ci, upper_ci), interval


# ============================================================================ #
# OTHERS                                                                       #
# ============================================================================ #


def critical_t(confidence, sample_size):
    """Returns the (two-tailed) critical value of t-distribution

    Parameters
    ----------
    confidence : float, scalar between 0 and 1
        the level of confidence. E.g. 0.95 -> 95%

    sample_size : scalar, int
        the sample size

    Assumptions
    -----------
    - the population is symmetric
    """

    # recalculate confidence for the two-tailed t-distribution
    confidence = confidence + ((1 - confidence) / 2)

    return t.ppf(confidence, sample_size)
