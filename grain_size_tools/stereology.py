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

import numpy as np
from pandas import DataFrame
import tools as tools
import plots as plots


def Saltykov(diameters, numbins=10, calc_vol=None,
             text_file=None, return_data=False, left_edge=0):
    """ Estimate the actual (3D) distribution of grain size from the population of
    apparent diameters measured in a thin section using a Saltykov-type method.
    (Saltykov 1967; Sahagian and Proussevitch 1998).

    The Saltykov method is optimal to estimate the volume of a particular grain size
    fraction as well as to obtain a qualitative view of the appearance of the actual
    3D grain size population, either in uni- or multimodal populations.

    Parameters
    ----------
    diameters : array_like
        the apparent diameters of the grains.

    numbins : positive integer, optional
        the number of bins/classes of the histrogram. If not declared, is set
        to 10 by default.

    calc_vol : positive scalar or None, optional
        if the user specifies a number, the function will return the volume
        occupied by the grain fraction up to that value.

    text_file : string or None, optional
        if the user specifies a name, the function will return a csv file
        with that name containing the data used to construct the Saltykov
        plot.

    return_data : bool, optional
       if True the function will return the position of the midpoints and
       the frequencies.

    left_edge : positive scalar or 'min', optional
        set the left edge of the histogram. Default is zero.

    Call functions
    --------------
    - unfold_population
    - Saltykov_plot (from plots)

    Examples
    --------
    >>> Saltykov(diameters)
    >>> Saltykov(diameters, numbins=16, calc_vol=40)
    >>> Saltykov(diameters, text_file='foo.csv')
    >>> left_edges, frequencies = Saltykov(diameters, return_data=True)

    References
    ----------
    | Saltykov SA (1967) http://doi.org/10.1007/978-3-642-88260-9_31
    | Sahagian and Proussevitch (1998) https://doi.org/10.1016/S0377-0273(98)00043-2

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

    # Unfold the population of apparent diameters using the Scheil-Schwartz-Saltykov method
    freq3D = unfold_population(freq, bin_edges, binsize, mid_points)

    # Calculate the volume-weighted cumulative frequency distribution TODO -> better an own function
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
            print(' ')
            print('volume fraction (up to', calc_vol, 'microns) =', round(volume, 2), '%')
        else:
            print(' ')
            print('volume fraction (up to', calc_vol, 'microns) =', 100, '%')

    # Create a text file (if apply) with the midpoints, class frequencies, and cumulative volumes
    if text_file is not None:
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
        print(' ')
        print('The file {} was created' .format(text_file))

    # return data or figure (if apply)
    if return_data is True:
        return mid_points, freq3D

    elif return_data is False:
        print('bin size =', round(binsize, 2))
        return plots.Saltykov_plot(left_edges, freq3D, binsize, mid_points, cdf_norm)

    else:
        raise TypeError('return_data must be set as True or False')


def calc_shape(diameters, class_range=(10, 20)):
    """ Approximates the shape of the actual (3D) distribution of grain size from a
    population of apparent diameters measured in a thin section using the two-step
    method (Lopez-Sanchez and Llana-Funez, 2016).

    The method only works properly for unimodal lognormal-like grain size populations
    and returns the MSD (i.e. shape) and the geometric mean (i.e. scale) values, which
    describe the lognormal population of grain sizes at their lineal scale. For
    details see Lopez-Sanchez and Llana-Funez (2016).

    Parameters
    ----------
    diameters : array_like
        the apparent diameters of the grains

    class_range : tupe or list with two values, optional
        the range of classes considered. The algorithm will estimate the optimal
        number of classes within this range.


    Call functions
    --------------
    - Saltykov
    - fit_log, log_function, and gen_xgrid (from tools)
    - twostep_plot (from plots)

    Examples
    --------
    >>> calc_shape(diameters)
    >>> calc_shape(diameters, class_range=(12, 18))
    >>> calc_shape(diameters, initial_guess=True)

    References
    ----------
    | Saltykov SA (1967) http://doi.org/10.1007/978-3-642-88260-9_31
    | Sahagian and Proussevitch (1998) https://doi.org/10.1016/S0377-0273(98)00043-2
    | Lopez-Sanchez and Llana-Funez (2016) https://doi.org/10.1016/j.jsg.2016.10.008

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
        optimal_params, sigma_error = tools.fit_log(mid_points, frequencies, initial_guess=(shape, scale))
        stds[index] = sigma_error[0]

    # get the optimal number of clases and estimate the best fit parameters
    optimal_num_classes = class_list[np.argmin(stds)]
    mid_points, frequencies = Saltykov(diameters, numbins=optimal_num_classes, return_data=True)
    optimal_params, sigma_err = tools.fit_log(mid_points, frequencies, (shape, scale))

    print(' ')
    print('OPTIMAL VALUES')
    print('Number of clasess: {}' .format(optimal_num_classes))
    print('MSD (log-normal shape) = {msd:0.2f} ± {err:0.2f}' .format(msd=optimal_params[0], err=3 * sigma_err[0]))
    print('Geometric mean (scale) = {gmean:0.2f} ± {err:0.2f}' .format(gmean=optimal_params[1], err=3 * sigma_err[1]))
    print(' ')
    # print(' Covariance matrix:\n', covm)

    # prepare data for the plot
    xgrid = tools.gen_xgrid(0.1, diameters.max())
    best_fit = tools.log_function(xgrid, optimal_params[0], optimal_params[1])

    # Estimate all the combinatorial posibilities for fit curves taking into account the uncertainties
    values = np.array([tools.log_function(xgrid, optimal_params[0] + sigma_err[0], optimal_params[1] + sigma_err[1]),
                       tools.log_function(xgrid, optimal_params[0] - sigma_err[0], optimal_params[1] - sigma_err[1]),
                       tools.log_function(xgrid, optimal_params[0] + sigma_err[0], optimal_params[1] - sigma_err[1]),
                       tools.log_function(xgrid, optimal_params[0] - sigma_err[0], optimal_params[1] + sigma_err[1])])

    # Estimate the standard deviation of the all values obtained
    fit_error = np.std(values, axis=0)

    return plots.twostep_plot(xgrid, mid_points, frequencies, best_fit, fit_error)


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

    return 1 / R * (np.sqrt(R**2 - r1**2) - np.sqrt(R**2 - r2**2))
