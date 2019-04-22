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
#    Version 2.0.3                                                             #
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
from numpy import mean, std, median, sqrt, exp, log, delete
from scipy.optimize import curve_fit
from scipy.stats import gaussian_kde, iqr, mstats


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
    print('Area-weighted mean grain size = {} microns' .format(round(weightedMean, 2)))
    print(' ')
    print('HISTOGRAM FEATURES')
    print('The modal interval is {left} - {right} microns' .format(left=round(bin_edges[getIndex], 2), right=round(bin_edges[getIndex] + h, 2)))
    print('Midpoint (of modal interval) = {} microns' .format(round((bin_edges[getIndex] + (bin_edges[getIndex] + h)) / 2.0, 1)))
    print('The number of classes are {}' .format(len(histogram)))
    if type(binsize) is str:
        print('The bin size is {bin} according to the {rule} rule' .format(bin=round(h, 2), rule=binsize))
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
    """

    if len(diameters) < 433:  # TODO: Change this in next version, this is not apply for all distributions!
        print(' ')
        print('Caution! You should use at least 433 grain measurements for reliable results')

    mean_GS, std_GS = mean(diameters), std(diameters)
    median_GS, iqr_GS = median(diameters), iqr(diameters)
    if plot == 'linear':
        gmean = mstats.gmean(diameters)  # geometric mean
        gsd = np.exp(np.std(np.log(diameters)))  # multiplicative (geometric) standard deviation
        mean_RMS = sqrt(mean(diameters**2))  # root mean square

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
    print('CENTRAL TENDENCY ESTIMATORS')
    print('Arithmetic mean = {} microns' .format(round(mean_GS, 2)))
    if plot == 'linear':
        print('Geometric mean = {} microns' .format(round(gmean, 2)))
        print('RMS mean = {} microns (discouraged)' .format(round(mean_RMS, 2)))
    print('Median = {} microns' .format(round(median_GS, 2)))
    print('Peak grain size (based on KDE) = {} microns' .format(round(peak, 2)))

    print(' ')
    print('DISTRIBUTION FEATURES (SPREADING AND SHAPE)')
    print('Standard deviation = {} (1-sigma)' .format(round(std_GS, 2)))
    print('Interquartile range (IQR) = {}' .format(round(iqr_GS, 2)))
    if plot == 'linear':
        print('Multiplicative standard deviation (lognormal shape) = {}' .format(round(gsd, 2)))

    print(' ')
    print('HISTOGRAM AND KDE FEATURES')
    print('The modal interval is {left} - {right}' .format(left=round(modInt_leftEdge, 2), right=round(modInt_rightEdge, 2)))
    print('The number of classes are {}' .format(len(histogram)))
    if type(bin_method) is str:
        print('The bin size is {bin} according to the {rule} rule' .format(bin=round(binsize, 2), rule=bin_method))

    if type(bandwidth) is str:
        print('KDE bandwidth = {a} ({b} rule)' .format(a=bw, b=bandwidth))
    else:
        print('KDE bandwidth =', bandwidth)

    if plot == 'linear':
        print('Maximum precision of the KDE estimator =', max_precision)
        return plots.freq_plot(diameters, bin_edges, x_kde, y_kde, y_max, peak, mean_GS, median_GS, plot, gmean)
    elif plot == 'log':
        print('Maximum precision of the KDE estimator =', max_precision)
    elif plot == 'log10':
        print('Maximum precision of the KDE estimator =', max_precision)
    elif plot == 'sqrt':
        print('Maximum precision of the KDE estimator =', max_precision)

    return plots.freq_plot(diameters, bin_edges, x_kde, y_kde, y_max, peak, mean_GS, median_GS, plot)


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
    the distribution of points approach a lognormal distribution

    Call functions
    --------------
    log_function
    curve_fit (from Scipy)

    Returns
    -------
    The optimal params and the error of the fit
    """
    # fit a log normal function
    optimal_params, cov_matrix = curve_fit(log_function, x, y, initial_guess)

    # estimate the uncertainty of the fit.
    sigma_error = np.sqrt(np.diag(cov_matrix))

    return optimal_params, sigma_error


def gen_xgrid(start, stop, precision):
    """ Returns a mesh of values (i.e. discretize the
    sample space) with a range and desired precision.

    Parameters
    ----------
    start : scalar
        the starting value of the sequence
    stop : scalar
        the end value of the sequence
    precision : scalar
        the desired precision (density) of the mesh
    """

    rango = stop - start

    # num = range / precision; as long as range > precision
    if rango < precision:
        raise ValueError('Caution! the precision must be smaller than the range of grain sizes')
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
        print('The script requires Python 3.5 or higher')

    return file_path


def log_function(x, shape, scale):
    """ Defines a logarithmic function to fit the data using the scipy
    curve_fit routine. In this case, it is the two-parameter equation
    that describes a lognormal distribution using the mean and the
    standard deviation of the log(x) with base e.

    Parameters
    ----------
    x: array_like
        the x-values

    shape: positive scalar
        the shape parameter; it relates to the sigma parameter: s = log(shape)

    scale: positive scalar
        the scale parameter; it relates to the mean of log(x): m = log(scale)
    """

    s = log(shape)
    m = log(scale)

    return 1 / (x * s * sqrt(2 * np.pi)) * exp(-1 / 2. * ((log(x) - m)**2 / s**2))


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
        scale = mean(log(diameters))
    elif factor == 2:
        scale = median(log(diameters))
    elif factor == 3:
        _, _, scale, _, _ = calc_freq_peak(log(diameters), bandwidth=bandwidth, binsize=None)
    else:
        raise ValueError('Normalization factor has to be defined as 1, 2, or 3')

    return log(diameters) / scale


def unfold_population(freq, bin_edges, binsize, mid_points, normalize=True):
    """ Applies a Scheil-Schwartz-Saltykov-type method to unfold the population
    of apparent (2D) diameters into the actual (3D) population of grain sizes.
    Following the reasoning of Higgins (2000), R (or D) is placed at the center
    of the classes (i.e. the midpoints).

    Reference
    ----------
    Higgins (2000) doi:10.2138/am-2000-8-901

    Parameters
    ----------
    freq : array_like
        frequency values of the different classes

    bin_edges : array_like
        the edges of the classes

    mid_points : array_like
        the midpoints of the classes

    normalize : boolean, optional
        when True negative frequency values are set to zero and the
        distribution normalized. True by default.

    Call function
    -------------
    - wicksell_eq

    Returns
    -------
    The normalized frequencies of the unfolded population such that the integral
    over the range is one. If normalize is False the raw frequencies of the
    unfolded population.
    """

    d_values = np.copy(bin_edges)
    midpoints = np.copy(mid_points)
    i = len(midpoints) - 1

    while i > 0:
        j = i
        D = d_values[-1]
        Pi = wicksell_solution(D, d_values[i], d_values[i + 1])

        if freq[i] > 0:
            while j > 0:
                D = midpoints[-1]
                Pj = wicksell_solution(D, d_values[j - 1], d_values[j])
                P_norm = (Pj * freq[i]) / Pi
                np.put(freq, j - 1, freq[j - 1] - P_norm)  # replace specified elements of an array
                j -= 1

            i -= 1
            d_values = delete(d_values, -1)
            midpoints = delete(midpoints, -1)

        # if the value of the current class is zero or negative move to the next class
        else:
            i -= 1
            d_values = delete(d_values, -1)
            midpoints = delete(midpoints, -1)

    if normalize is True:
        freq = np.clip(freq, 0., 2**20)  # replacing negative values with zero
        freq_norm = freq / sum(freq)  # normalize to one
        freq_norm = freq_norm / binsize  # normalize such that the integral over the range is one
        return freq_norm

    else:
        return freq


def wicksell_solution(D, d1, d2):
    """ Estimate the cross-section size probability for a discretized population
    of spheres based on the Wicksell (1925) equation originally proposed by
    Scheil (1931), Schwartz (1934) and Saltykov (1967) (the so-called
    Scheil-Schwartz-Saltykov method). The general solution is the equation:

    P(r1 < r < r2) = 1/R * (sqrt(R**2 - r1**2) - sqrt(R**2 - r2**2))

    where R is the sphere radius and r the cross-section radius.
    r1 and r2 are the lower and upper bounds of the classes, respectively.
    R can be placed at the at the center or the upper/lower limit of the
    classes.

    Parameters
    ----------
    D: positive scalar
        the midpoint of the actual class

    d1: positive scalar
        the lower limit of the bin/class

    d2: positive scalar
        the upper limit of the bin/class

    References
    ----------
    | Saltykov (1967) doi:10.1007/978-3-642-88260-9_31
    | Scheil (1931) doi:10.1002/zaac.19312010123
    | Schwartz (1934) Met. Alloy 5:139
    | Wicksell (1925) doi:10.2307/2332027
    | Higgins (2000) doi:10.2138/am-2000-8-901

    Returns
    -------
    the cross-section probability for a especific range of grain size
    """

    # convert diameters to radii
    R, r1, r2 = D / 2, d1 / 2, d2 / 2

    return 1 / R * (sqrt(R**2 - r1**2) - sqrt(R**2 - r2**2))
