# ============================================================================ #
#                                                                              #
#    This is part of the "GrainSizeTools Script"                               #
#    A Python script for characterizing grain size from thin sections          #
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
#    limitations under the License.                                            #
#                                                                              #
#    Version 3.0                                                               #
#    For details see: http://marcoalopez.github.io/GrainSizeTools/             #
#    download at https://github.com/marcoalopez/GrainSizeTools/releases        #
#                                                                              #
# ============================================================================ #

# ============================================================================ #
# TODO functions doing specific tasks used by the GrainSizeTools script        #
# The names of the functions are self-explanatory and appear in alphabetical   #
# order. Save this file in the same directory as GrainSizeTools_script.py      #
# ============================================================================ #

import numpy as np
from scipy.stats import sem, t
import averages


def area2diameter(areas, correct_diameter=None):
    """ Calculate the equivalent cirular diameter from sectional areas.

    Parameters
    ----------
    areas : array_like
        the sectional areas of the grains

    correct_diameter : None or positive scalar, optional
        add the width of the grain boundaries to correct the diameters. If
        correct_diameter is not declared no correction is considered.

    Returns
    -------
    A numpy array with the equivalent circular diameters
    """

    # calculate the equivalent circular diameter
    diameters = 2 * np.sqrt(areas / np.pi)

    # diameter correction adding edges (if applicable)
    if correct_diameter is not None:
        diameters += correct_diameter

    return diameters


def conf_interval(data, confidence=0.95):
    """Estimate the confidence interval using the t-distribution with n-1
    degrees of freedom t(n-1). This is the way to go when sample size is
    small (n < 30) and the standard deviation cannot be estimated accurately.
    For large datasets, the t-distribution approaches the normal distribution.

    Parameters
    ----------
    data : array-like
        the dataset

    confidence : float between 0 and 1, optional
        the confidence interval, default = 0.95

    Assumptions
    -----------
    the data follows a normal or symmetric distrubution (when sample size
    is large)

    call_function(s)
    ----------------
    Scipy's t.interval

    Returns
    -------
    the arithmetic mean, the error, and the limits of the confidence interval
    """

    dof = len(data) - 1
    sample_mean = np.mean(data)
    std_err = sem(data)  # Standard error of the mean SD / sqrt(n)
    low, high = t.interval(confidence, dof, sample_mean, std_err)
    err = high - sample_mean

    print(' ')
    print('Confidence set at {} %' .format(confidence * 100))
    print('Mean = {mean:0.2f} ± {err:0.2f}' .format(mean=sample_mean, err=err))
    print('Max / min = {max:0.2f} / {min:0.2f}' .format(max=high, min=low))
    print('Coefficient of variation = {:0.1f} %' .format(100 * err / sample_mean))

    return sample_mean, err, (low, high)


def summarize(diameters, avg=('amean', 'gmean', 'median', 'mode'), ci_level=0.95,
              ci_method='ASTM', bandwidth='silverman', precision=0.1):
    """ Estimate different grain size statistics. This includes different means,
    the median, the frequency peak grain size via KDE

    Parameters
    ----------
    diameters : array_like
        the apparent diameters of the grains

    avg : tuple or list, optional
        the averages to be estimated

        | Types:
        | 'amean' - arithmetic mean
        | 'gmean' - geometric mean
        | 'median' - median
        | 'mode' - the kernel-based frequency peak of the distribution

    bandwidth : string {'silverman' or 'scott'} or positive scalar, optional
        the method to estimate the bandwidth or a scalar directly defining the
        bandwidth. It uses the Silverman plug-in method by default.

    precision : positive scalar or None, optional
        the maximum precision expected for the "peak" kde-based estimator.
        Default is None

    Call functions
    --------------
    - amean, gmean, median, and freq_peak (from averages)

    Examples
    --------
    >>> summarize(diameters)
    >>> summarize(diameters, plot='log')
    >>> summarize(diameters, binsize='doane', bandwidth=2.5)
    >>> summarize(diameters, bandwidth='scott', precision=0.1)

    Returns
    -------
    TODO
    """

    if 'amean' in avg:

        amean, std, arith_ci, length = averages.amean(diameters, ci_level, ci_method)

        print(' ')
        print('arithmetic mean = {:0.2f} microns' .format(amean))
        if ci_method == 'ASTM':
            print('confidence interval = ± {:0.2f} at {:0.1f} %' .format(arith_ci, ci_level * 100))
        else:
            print('confidence interval = {:0.2f}, {:0.2f} (lower, upper) at {:0.1f} %' .format(arith_ci[0], arith_ci[1], ci_level * 100))
        print('ci length = {:0.2f}' .format(length))
        print('CI method used:', ci_method)
        print(' ')

    if 'gmean' in avg:

        # apply optimal method to estimate confidence intervals
        if len(diameters) > 99:
            m = 'CLT'
        else:
            m = 'bayes'

        gmean, msd, (low_ci, high_ci), length = averages.gmean(diameters, ci_level, method=m)

        # estimate coefficients of variation
        lower_cvar = 100 * (gmean - low_ci) / gmean
        upper_cvar = 100 * (high_ci - gmean) / gmean

        print(' ')
        print('Geometric mean = {:0.2f} microns' .format(gmean))
        print('confidence interval = {:0.2f}, {:0.2f} (lower, upper) at {:0.1f} %' .format(low_ci, high_ci, ci_level * 100))
        print('coeff. var. = -{:0.2f}%, +{:0.2f}%' .format(lower_cvar, upper_cvar))
        print('ci length = {:0.2f}' .format(length))
        print('CI method used:', m)
        print(' ')

    if 'median' in avg:
        median, iqr, (low_ci, high_ci), length = averages.median(diameters, ci_level)

        # estimate coefficients of variation
        lower_cvar = 100 * (median - low_ci) / median
        upper_cvar = 100 * (high_ci - median) / median

        print(' ')
        print('Median = {:0.2f} microns)' .format(median))
        print('confidence interval = {:0.2f}, {:0.2f} (lower, upper) at {:0.1f} %' .format(low_ci, high_ci, ci_level * 100))
        print('coeff. var. = -{:0.2f}%, +{:0.2f}%' .format(lower_cvar, upper_cvar))
        print('ci length = {:0.2f}' .format(length))
        print('CI method used: Hollander and Wolfe (1999)')
        print(' ')

    if 'mode' in avg:
        __, mode, __, bw = averages.freq_peak(diameters, bandwidth, precision)

        print('Mode = {:0.2f} microns (KDE-based)' .format(mode))
        print('Maximum precision set to:', precision)

        if type(bandwidth) is str:
            print('KDE bandwidth = {a} ({b} rule)' .format(a=bw, b=bandwidth))
        else:
            print('KDE bandwidth =', bandwidth)

    print(' ')
    print('DISTRIBUTION FEATURES (SPREADING AND SHAPE)')
    print('Standard deviation = {:0.2f} (1-sigma)' .format(std))
    print('Interquartile range (IQR) = {:0.2f}' .format(iqr))
    print('Lognormal shape (Multiplicative Standard Deviation) = {:0.2f}' .format(msd))
    print(' ')

    return None
