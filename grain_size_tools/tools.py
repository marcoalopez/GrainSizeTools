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
# Auxiliary functions doing specific tasks used by the GrainSizeTools script   #
# The names of the functions are self-explanatory. They appear in alphabetical #
# order. Save this file in the same directory as GrainSizeTools_script.py      #
# ============================================================================ #

import os
import numpy as np
import plots as plots
from scipy.optimize import curve_fit
from scipy.stats import gaussian_kde, t


def calc_areaweighted_grainsize(areas, diameters, binsize):
    """ Calculates the area percentage of each grain size interval. It is
    based on Herwegh (2000) and Berger et al. (2011) approach. Returns the
    the grain size interval with the maximum area accumulated, the middle
    value of this interval and the area weighted arithmetic mean.

    References
    ----------
    | Herwegh (2000) doi:10.1016/S0191-8141(99)00165-0
    | Berger et al. (2011) doi:10.1016/j.jsg.2011.07.002

    Parameters
    ----------
    areas: array_like
        a list with the sectional areas of the grains

    diameters: array_like
        a list with the equivalent circular diameters of the grains

    binsize: a string (plug-in methods) or scalar
        the bin size
    """

    # calculate the area weighted arithmetic mean
    areatotal = np.sum(areas)
    weightedAreas = areas / areatotal
    weigtedDiameters = diameters * weightedAreas
    weightedMean = np.sum(weigtedDiameters)

    # estimate the bin size using an automatic plug-in method (if apply)
    if type(binsize) is str:
        histogram, bin_edges = np.histogram(diameters, bins=binsize, range=(0.0, diameters.max()))
        h = bin_edges[1]
    else:
        bin_edges = np.arange(0.0, diameters.max() + binsize, binsize)
        h = binsize

    # estimate the cumulative areas of each grain size interval
    cumulativeAreas = np.zeros(len(bin_edges))
    for index, values in enumerate(bin_edges):
        mask = np.logical_and(diameters >= values, diameters < (values + h))
        area_sum = np.sum(areas[mask])
        cumulativeAreas[index] = round(area_sum, 1)

    # get the index of the maximum value (the modal interval)
    getIndex = np.argmax(cumulativeAreas)

    print(' ')
    print('DESCRIPTIVE STATISTICS')
    print(' ')
    print('Area-weighted mean grain size = {:0.2f} microns' .format(weightedMean))
    print(' ')
    print('HISTOGRAM FEATURES')
    print('The modal interval is {left:0.2f} - {right:0.2f} microns' .format(left=bin_edges[getIndex], right=bin_edges[getIndex] + h))
    print('Midpoint (of modal interval) = {:0.2f} microns' .format(bin_edges[getIndex] + (bin_edges[getIndex] + h) / 2.0))
    print('The number of classes are {}' .format(len(histogram)))
    if type(binsize) is str:
        print('The bin size is {bin:0.2f} according to the {rule} rule' .format(bin=h, rule=binsize))
    print(' ')

    return plots.area_weighted_plot(bin_edges, cumulativeAreas, h, weightedMean)


def calc_freq_grainsize(diameters, binsize, plot, bandwidth, max_precision):
    """ Calculate the distribution of grain sizes using the histogram and Gaussian
    kernel density estimator (KDE). It returns the modal interval, the middle value
    of modal interval, and the frequency peak based on the KDE, and call the
    function responsible for generating the corresponding plot.

    Parameters
    ----------
    diameters : array_like
        the diameters of the grains

    binsize : string (rule of thumb), or posive scalar
        the bin size

    plot : string
        the type of plot and grain size, either 'linear', 'log' or 'sqrt'.

    bandwidth : string, scalar or callable, optional
        the method to estimate the bandwidth or a scalar directly defining the
        bandwidth. Methods can be 'silverman' or 'scott'.

    max_precision : positive scalar
        the maximum precision expected for the "peak" kde-based estimator

    References
    ----------
    Scott, D.W. (1992) Multivariate Density Estimation: Theory, Practice, and Visualization
    Silverman, B.W. (1986) Density Estimation for Statistics and Data Analysis

    Call functions
    --------------
    - freq_plot
    - calc_freq_peak
    - _mean_
    - _gmean_
    - _median_
    """

    mean, std, std_err = _mean_(diameters, ci=0.95)
    median, iqr_pop, med_conf, med_std_err = _median_(diameters, ci=0.95)
    if plot == 'linear':
        gmean, mSD, geo_conf, geo_std_err = _gmean_(diameters, ci=0.95)

    # estimate the number of classes using an automatic plug-in method (if apply)
    if type(binsize) is str:
        bin_method = binsize
        histogram, bin_edges = np.histogram(diameters, bins=binsize, range=(diameters.min(), diameters.max()))
        binsize = bin_edges[1] - bin_edges[0]
    else:
        bin_method = None
        bin_edges = np.arange(diameters.min(), diameters.max() + binsize, binsize)
        histogram, bin_edges = np.histogram(diameters, bins=bin_edges)

    # find the grain size range in which the histogram value is maximum
    modInt_leftEdge = bin_edges[np.argmax(histogram)]
    modInt_rightEdge = modInt_leftEdge + binsize

    # Estimate the frequency peak grain size based on kde
    x_kde, y_kde, peak, y_max, bw = calc_freq_peak(diameters, bandwidth, max_precision)

    print(' ')
    print('CENTRAL TENDENCY ESTIMATORS (confidence intervals at 95 %)')
    print('Arithmetic mean = {:0.2f} microns' .format(mean))
    print('      abs. err. = ± {:0.2f}' .format(std_err))
    print('      coeff. var = {:0.2f}%' .format(100 * std_err / mean))
    if plot == 'linear':
        print('')
        print('Geometric mean = {:0.2f} microns' .format(gmean))
        print('      abs err = {:0.2f}, +{:0.2f} (lower, upper)' .format(geo_std_err[0], geo_std_err[1]))
        print('      range = {:0.2f}, {:0.2f}' .format(geo_conf[0], geo_conf[1]))
        print('      coeff. var. = {:0.2f}%, {:0.2f}%' .format(100 * geo_std_err[0] / gmean, 100 * geo_std_err[1] / gmean))
    print('')
    print('Median = {:0.2f} microns)' .format(median))
    print('      abs. err. = {:0.2f}, +{:0.2f} (lower, upper) ' .format(med_std_err[0], med_std_err[1]))
    print('      range = {:0.2f}, {:0.2f}' .format(med_conf[0], med_conf[1]))
    print('      coeff. var. = {:0.2f}%, {:0.2f}%' .format(100 * med_std_err[0] / median, 100 * med_std_err[1] / median))
    print('')
    print('Mode = {:0.2f} microns (KDE-based peak grain size)' .format(peak))

    print(' ')
    print('DISTRIBUTION FEATURES (SPREADING AND SHAPE)')
    print('Standard deviation = {:0.2f} (1-sigma)' .format(std))
    print('Interquartile range (IQR) = {:0.2f}' .format(iqr_pop))
    if plot == 'linear':
        print('Multiplicative standard deviation (lognormal shape) = {:0.2f}' .format(mSD))

    print(' ')
    print('HISTOGRAM AND KDE FEATURES')
    print('Number of classes = {}' .format(len(histogram)))
    print('The modal interval is {left:0.2f} - {right:0.2f}' .format(left=modInt_leftEdge, right=modInt_rightEdge))
    if type(bin_method) is str:
        print('The bin size is {bin:0.2f} according to the {rule} rule' .format(bin=binsize, rule=bin_method))

    if type(bandwidth) is str:
        print('KDE bandwidth = {a} ({b} rule)' .format(a=bw, b=bandwidth))
    else:
        print('KDE bandwidth =', bandwidth)

    if plot == 'linear':
        print('Maximum precision of the KDE estimator =', max_precision)
        return plots.freq_plot(diameters, bin_edges, x_kde, y_kde, y_max, peak, mean, median, plot, gmean)
    elif plot == 'log':
        print('Maximum precision of the KDE estimator =', max_precision)
    elif plot == 'log10':
        print('Maximum precision of the KDE estimator =', max_precision)
    elif plot == 'sqrt':
        print('Maximum precision of the KDE estimator =', max_precision)

    return plots.freq_plot(diameters, bin_edges, x_kde, y_kde, y_max, peak, mean, median, plot)


def calc_freq_peak(diameters, bandwidth, max_precision):
    """ Estimate the peak of the frequency ("mode") of a continuous
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
    - gen_xgrid
    - kde (from scipy)

    Returns
    -------
    The x and y values to contruct the kde, the peak grain size,
    the maximum density value,, and the bandwidth
    """

    # check bandwidth and estimate Gaussian kernel density function
    if isinstance(bandwidth, (int, float)):
        bw = bandwidth / diameters.std(ddof=1)
        kde = gaussian_kde(diameters, bw_method=bw)

    elif isinstance(bandwidth, str):
        kde = gaussian_kde(diameters, bw_method=bandwidth)
        bw = round(kde.covariance_factor() * diameters.std(ddof=1), 2)

    else:
        raise ValueError("bandwidth must be integer, float, or plug-in methods 'silverman' or 'scott'")

    # locate the peak
    xgrid = gen_xgrid(diameters.min(), diameters.max(), max_precision)
    densities = kde(xgrid)
    y_max, peak_grain_size = np.max(densities), xgrid[np.argmax(densities)]

    return xgrid, densities, peak_grain_size, y_max, bw


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
    - the population is symetric
    """

    # recalculate confidence for the two-tailed t-distribution
    confidence = confidence + ((1 - confidence) / 2)

    return t.ppf(confidence, sample_size)


def fit_log(x, y, initial_guess):
    """ Fit a lognormal distribution to data. It uses the curve_fit
    scipy routine, which is a non-linear least-square implementation of
    the Levenberge-Marquardt algorithm.

    Parameters
    ----------
    x : array-like
        the x coordinates of the points

    y : array-like
        the y coordinates of the points

    initial_guess : tuple or list with two values
        a tuple or list with the two starting guess values

    Assumptions
    -----------
    - the distribution of points approach a lognormal distribution.
    - It is assumed that the multiplicative SD lies within the range
    from 1 (gaussian) to 10.

    Call functions
    --------------
    log_function
    curve_fit (from Scipy)

    Returns
    -------
    The optimal params and the error of the fit
    """
    # fit a log normal function (it assumes that shape is within the 1-10 range)
    optimal_params, cov_matrix = curve_fit(log_function, x, y, initial_guess,
                                           bounds=((1, 0), (10, np.inf)))

    # estimate the uncertainty of the fit.
    sigma_error = np.sqrt(np.diag(cov_matrix))

    return optimal_params, sigma_error


def gen_xgrid(start, stop, precision=None):
    """ Returns a mesh of values (i.e. discretize the
    sample space) with a fixed range and desired precision.

    Parameters
    ----------
    start : scalar
        the starting value of the sequence
    stop : scalar
        the end value of the sequence
    precision : scalar or None
        the desired precision (density) of the mesh
    """

    rango = stop - start

    if precision is None:
        precision = 1 / rango

    # num = range / precision; as long as range > precision
    if rango < precision:
        raise ValueError('The precision must be smaller than the range of grain sizes')
    else:
        n = int(round(rango / precision, 0))

    return np.linspace(start, stop, num=n)


def get_filepath():
    """ Get a file path through a file selection dialog."""

    try:
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(),
                                               title="Select file",
                                               filetypes=[('Text files', '*.txt'),
                                                          ('Text files', '*.csv'),
                                                          ('Excel files', '*.xlsx')])
    except ImportError:
        print('Requires Python 3.6+')

    return file_path


def log_function(x, shape, scale):
    """ This is the two-parameter equation that describes a lognormal
    distribution using the mean and the standard deviation of the
    log(x) with base e.

    Parameters
    ----------
    x: array_like
        the x-values

    shape: positive scalar
        the shape parameter; it relates to the sigma parameter: s = log(shape)

    scale: positive scalar
        the scale parameter; it relates to the mean of log(x): m = log(scale)
    """

    s = np.log(shape)
    m = np.log(scale)

    return 1 / (x * s * np.sqrt(2 * np.pi)) * np.exp(-1 / 2. * ((np.log(x) - m)**2 / s**2))


def norm_grain_size(diameters, binsize, bandwidth):
    """ Recalculates grain size scaled by its mean, median, or frequency
    peak value ("mode")

    Parameters
    ----------
    diameters : array_like
        the apparent diameters of the grains

    binsize : string or positive scalar, optional
        the bin size

    bandwidth : string {'silverman' or 'scott'} or positive scalar, optional
        the method to estimate the bandwidth or a scalar directly defining the
        bandwidth. It uses the Silverman plug-in method by default.

    Call function
    -------------
    - calc_freq_peak

    Returns
    -------
    the normalized grain size population
    """

    factor = int(input("Define the normalization factor (1 to 3) \n 1 -> mean; 2 -> median; 3 -> max_freq: "))

    if factor == 1:
        scale = np.mean(np.log(diameters))
    elif factor == 2:
        scale = np.median(np.log(diameters))
    elif factor == 3:
        _, _, scale, _, _ = calc_freq_peak(np.log(diameters), bandwidth=bandwidth, binsize=None)
    else:
        raise ValueError('Normalization factor has to be defined as 1, 2, or 3')

    return np.log(diameters) / scale
