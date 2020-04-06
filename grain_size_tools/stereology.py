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
#    Version 3.0beta2                                                          #
#    For details see: http://marcoalopez.github.io/GrainSizeTools/             #
#    download at https://github.com/marcoalopez/GrainSizeTools/releases        #
#                                                                              #
# ============================================================================ #

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def Saltykov(diameters, numbins=10, calc_vol=None, text_file=None,
             return_data=False, left_edge=0):
    """ Estimate the actual (3D) distribution of grain size from the population
    of apparent diameters measured in a thin section using a Saltykov-type
    algorithm (Saltykov 1967; Sahagian and Proussevitch 1998).

    The Saltykov method is optimal to estimate the volume of a particular grain
    size fraction as well as to obtain a qualitative view of the appearance of
    the actual 3D grain size population, either in uni- or multimodal populations.

    Parameters
    ----------
    diameters : array_like
        the apparent diameters of the grains.

    numbins : positive integer, optional
        the number of bins/classes of the histogram. If not declared,
        is set to 10 by default.

    calc_vol : positive scalar or None, optional
        if the user specifies a diameter, the function will return the volume
        occupied by the grain fraction up to that diameter.

    text_file : string or None, optional
        if the user specifies a name, the function will store a csv file
        with that name containing the Saltykov output.

    return_data : bool, optional
       if True the function will return the position of the midpoints and
       the frequencies.

    left_edge : positive scalar or 'min', optional
        set the left edge of the histogram. Default is zero.

    Call functions
    --------------
    - unfold_population
    - Saltykov_plot

    Examples
    --------
    >>> Saltykov(diameters)
    >>> Saltykov(diameters, numbins=16, calc_vol=40)
    >>> Saltykov(diameters, text_file='foo.csv')
    >>> left_edges, frequencies = Saltykov(diameters, return_data=True)

    References
    ----------
    Saltykov SA (1967) http://doi.org/10.1007/978-3-642-88260-9_31
    Sahagian and Proussevitch (1998) https://doi.org/10.1016/S0377-0273(98)00043-2

    Return
    ------
    Statistical descriptors, a plot, and/or a file with the data (optional)
    """

    if isinstance(numbins, int) is False:
        raise ValueError('Numbins must be a positive integer')
    if numbins <= 0:
        raise ValueError('Numbins must be higher than zero')
    if isinstance(left_edge, (int, float)):
        if left_edge < 0:
            raise ValueError("left_edge must be a positive scalar or 'min'")

    # compute the histogram
    if left_edge == 'min':
        freq, bin_edges = np.histogram(diameters,
                                       bins=numbins,
                                       range=(diameters.min(), diameters.max()),
                                       density=True)
    else:
        freq, bin_edges = np.histogram(diameters,
                                       bins=numbins,
                                       range=(left_edge, diameters.max()),
                                       density=True)

    binsize = bin_edges[1] - bin_edges[0]

    # Create an array with the left edges of the bins and other with the midpoints
    left_edges = np.delete(bin_edges, -1)
    mid_points = left_edges + binsize / 2

    # Unfold the population of apparent diameters using the Saltykov method
    freq3D = unfold_population(freq, bin_edges, binsize, mid_points)

    # Calculate the volume-weighted cumulative frequency distribution
    # TODO -> better an own function
    x_vol = binsize * (4 / 3.) * np.pi * (mid_points**3)
    freq_vol = x_vol * freq3D
    cdf = np.cumsum(freq_vol)
    cdf_norm = 100 * (cdf / cdf[-1])

    # Estimate the volume of a particular grain size fraction (if proceed)
    if calc_vol is not None:
        x, y = mid_points, cdf_norm
        index = np.argmax(mid_points > calc_vol)
        angle = np.arctan((y[index] - y[index - 1]) / (x[index] - x[index - 1]))
        volume = y[index - 1] + np.tan(angle) * (calc_vol - x[index - 1])
        if volume < 100.0:
            print('=======================================')
            print('volume fraction (up to', calc_vol, 'microns) =', round(volume, 2), '%')
            print('=======================================')
        else:
            print('=======================================')
            print('volume fraction (up to', calc_vol, 'microns) =', 100, '%')
            print('=======================================')

    # Create a text file (if apply) with the midpoints, class frequencies, and
    # cumulative volumes
    if text_file is not None:
        from pandas import DataFrame
        if isinstance(text_file, str) is False:
            print('text_file must be None or string type')
        df = DataFrame({'mid_points': np.around(mid_points, 3),
                        'freqs': np.around(freq3D, 4),
                        'cum_vol': np.around(cdf_norm, 2)})
        if text_file.endswith('.txt'):
            df.to_csv(text_file, sep='\t')
        elif text_file.endswith('.csv'):
            df.to_csv(text_file, sep=';')
        else:
            raise ValueError('text file must be specified as .csv or .txt')
        print('=======================================')
        print('The file {} was created' .format(text_file))
        print('=======================================')

    # return data or figure (if apply)
    if return_data is True:
        return mid_points, freq3D

    elif return_data is False:
        print('=======================================')
        print('bin size =', round(binsize, 2))
        print('=======================================')
        return Saltykov_plot(left_edges, freq3D, binsize, mid_points, cdf_norm)

    else:
        raise TypeError('return_data must be set as True or False')


def calc_shape(diameters, class_range=(10, 20)):
    """ Approximates the shape of the actual (3D) distribution of grain size
    from a population of apparent diameters measured in a thin section using
    the two-step method (Lopez-Sanchez and Llana-Funez, 2016).

    The method only works properly for unimodal lognormal-like grain size
    populations and returns the MSD (i.e. shape) and the geometric mean
    (i.e. scale) values, which describe the lognormal population of grain sizes
    at their original (linear) scale.

    Parameters
    ----------
    diameters : array_like
        the apparent diameters of the grains

    class_range : tupe or list with two values, optional
        the range of classes considered. The algorithm will estimate the optimal
        number of classes within the defined range. Default = (10, 20)


    Call functions
    --------------
    - Saltykov,
    - fit_log,
    - log_function
    - gen_xgrid
    - twostep_plot

    Examples
    --------
    >>> calc_shape(diameters)
    >>> calc_shape(diameters, class_range=(12, 18))
    >>> calc_shape(diameters, initial_guess=True)

    References
    ----------
    Saltykov SA (1967) http://doi.org/10.1007/978-3-642-88260-9_31
    Sahagian and Proussevitch (1998) https://doi.org/10.1016/S0377-0273(98)00043-2
    Lopez-Sanchez and Llana-Funez (2016) https://doi.org/10.1016/j.jsg.2016.10.008

    Returns
    -------
    A plot with an estimate of the actual (3D) grains size distribution and
    several statistical parameters
    """

    # estimate the prior shape and scale based on the apparent distribution
    shape = np.exp(np.std(np.log(diameters), ddof=1))
    scale = np.median(diameters)

    # estimate the number of classes that produces the best fit within the range defined
    class_list = list(range(class_range[0], class_range[1] + 1))
    stds = np.zeros(len(class_list))

    for index, item in enumerate(class_list):
        mid_points, frequencies = Saltykov(diameters, numbins=item, return_data=True)
        optimal_params, sigma_error = fit_log(mid_points, frequencies, initial_guess=(shape, scale))
        stds[index] = sigma_error[0]

    # get the optimal number of clases and estimate the best fit parameters
    optimal_num_classes = class_list[np.argmin(stds)]
    mid_points, frequencies = Saltykov(diameters, numbins=optimal_num_classes, return_data=True)
    optimal_params, sigma_err = fit_log(mid_points, frequencies, (shape, scale))

    print('=======================================')
    print('OPTIMAL VALUES')
    print('Number of classes: {}' .format(optimal_num_classes))
    print('MSD (log-normal shape) = {msd:0.2f} ± {err:0.2f}'
          .format(msd=optimal_params[0], err=3 * sigma_err[0]))
    print('Geometric mean (scale) = {gmean:0.2f} ± {err:0.2f}'
          .format(gmean=optimal_params[1], err=3 * sigma_err[1]))
    print('=======================================')
    # print(' Covariance matrix:\n', covm)

    # prepare data for the plot
    xgrid = np.linspace(0.1, diameters.max(), 1000)
    best_fit = log_function(xgrid, optimal_params[0], optimal_params[1])

    # Estimate all the combinatorial posibilities for fit curves taking into account the uncertainties
    values = np.array([log_function(xgrid, optimal_params[0] + sigma_err[0], optimal_params[1] + sigma_err[1]),
                       log_function(xgrid, optimal_params[0] - sigma_err[0], optimal_params[1] - sigma_err[1]),
                       log_function(xgrid, optimal_params[0] + sigma_err[0], optimal_params[1] - sigma_err[1]),
                       log_function(xgrid, optimal_params[0] - sigma_err[0], optimal_params[1] + sigma_err[1])])

    # Estimate the standard deviation of the all values obtained
    fit_error = np.std(values, axis=0)

    return twostep_plot(xgrid, mid_points, frequencies, best_fit, fit_error)


def unfold_population(freq, bin_edges, binsize, mid_points, normalize=True):
    """ Applies the Saltykov-type algorithm to unfold the population of apparent
    (2D) diameters into the actual (3D) population of grain sizes. Following the
    reasoning of Higgins (2000), R (or D) is placed at the center of the classes
    (i.e. the midpoints).

    Reference
    ----------
    Higgins (2000) doi:10.2138/am-2000-8-901
    Saltykov SA (1967) http://doi.org/10.1007/978-3-642-88260-9_31
    Sahagian and Proussevitch (1998) https://doi.org/10.1016/S0377-0273(98)00043-2

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
            d_values = np.delete(d_values, -1)
            midpoints = np.delete(midpoints, -1)

        # if the value of the current class is zero or negative move to the next class
        else:
            i -= 1
            d_values = np.delete(d_values, -1)
            midpoints = np.delete(midpoints, -1)

    if normalize is True:
        freq = np.clip(freq, a_min=0.0, a_max=None)  # replacing negative values with zero
        freq_norm = freq / sum(freq)  # normalize to one
        freq_norm = freq_norm / binsize  # normalize such that the integral over the range is one
        return freq_norm

    else:
        return freq


def wicksell_solution(D, d1, d2):
    """ Estimate the cross-section size probability for a discretized population
    of spheres based on the Wicksell (1925) and later on Scheil (1931),
    Schwartz (1934) and Saltykov (1967). This is:

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

    return 1 / R * (np.sqrt(R**2 - r1**2) - np.sqrt(R**2 - r2**2))


# ============================================================================ #
# AUXILIARY FUNCTIONS                                                          #
# ============================================================================ #


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
    # fit a log normal function (it assumes that shape is within the 1-10 range
    # and location is positive)
    optimal_params, cov_matrix = curve_fit(log_function, x, y, initial_guess,
                                           bounds=((1, 0), (10, np.inf)))

    # estimate the uncertainty of the fit.
    sigma_error = np.sqrt(np.diag(cov_matrix))

    return optimal_params, sigma_error


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


def gen_xgrid(start, stop, precision):
    """ Returns a mesh of values (i.e. discretize the
    sample space) with a fixed range and desired precision.

    Parameters
    ----------
    start : scalar
        the starting value of the sequence
    stop : scalar
        the end value of the sequence
    precision : scalar, int or float
        the desired precision (density) of the mesh
    """

    rango = stop - start

    # num = range / precision; as long as range > precision
    if rango < precision:
        raise ValueError('The precision must be smaller than the range of grain sizes')
    else:
        n = int(round(rango / precision, 0))

    return np.linspace(start, stop, num=n)


def Saltykov_plot(left_edges, freq3D, binsize, mid_points, cdf_norm):
    """ Generate two plots once the Saltykov method is applied:

    i)  a bar plot (ax1)
    ii) a volume-weighted cumulative frequency plot (ax2)
    """

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(13, 5))

    # frequency vs grain size plot
    ax1.bar(left_edges, freq3D,
            width=binsize,
            color='#415e9d',
            edgecolor='#d9d9d9',
            align='edge')
    ax1.set_ylabel('density',
                   fontsize=15)
    ax1.set_xlabel(r'diameter ($\mu m$)',
                   fontsize=15)
    ax1.set_title('estimated 3D grain size distribution',
                  color='#1F1F1F',
                  fontsize=15,
                  y=1.02)

    # volume-weighted cumulative frequency curve
    ax2.set_ylim([-2, 105])
    ax2.plot(mid_points, cdf_norm,
             'o-',
             color='#ed4256',
             label='volume weighted CFD',
             linewidth=2)
    ax2.set_ylabel('cumulative volume (%)',
                   fontsize=15)
    ax2.set_xlabel(r'diameter ($\mu m$)',
                   fontsize=15)
    ax2.set_title('volume-weighted cumulative freq. distribution',
                  color='#1F1F1F',
                  fontsize=15,
                  y=1.02)

    fig.tight_layout()

    return None


def twostep_plot(xgrid, mid_points, frequencies, best_fit, fit_error):
    """ Generate a plot with the best fitting lognormal distribution (two-step method)"""

    # matplotlib stuff
    fig, ax = plt.subplots()

    # bar plot from Saltykov method
    ax.bar(mid_points, frequencies,
           width=mid_points[1] - mid_points[0],
           edgecolor=None,
           color='#415e9d',
           linewidth=1,
           label='Saltykov method',
           alpha=0.65)

    # log-normal distribution
    ax.plot(xgrid, best_fit,
            color='#1F1F1F',
            label='best fit',
            linewidth=2)

    ax.fill_between(xgrid, best_fit + (3 * fit_error), best_fit - (3 * fit_error),
                    color='#525252',
                    label='trust region',
                    alpha=0.5)

#    ax.plot(mid_points, frequencies,  # datapoints used for the fitting procedure
#            'o',
#            color='#d53e4f',
#            label='datapoints',
#            linewidth=1.5)

    ax.set_ylabel('freq. (per unit vol.)', fontsize=15)
    ax.legend(loc='best', fontsize=15)
    ax.set_xlabel(r'diameter ($\mu m$)', fontsize=15)

    fig.tight_layout()

    return None


if __name__ == '__main__':
    pass
else:
    print('module stereology imported')
