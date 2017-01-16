# ============================================================================ #
#                                                                              #
#    GrainSizeTools Script                                                     #
#    A Python script for estimating grain size features from thin sections     #
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
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND*, either express or implied. #
#    See the License for the specific language governing permissions and       #
#    limitations under the License.                                            #
#                                                                              #
#    Version 1.3                                                               #
#    For details see: http://marcoalopez.github.io/GrainSizeTools/             #
#    download at https://github.com/marcoalopez/GrainSizeTools/releases        #
#                                                                              #
#    Requirements:                                                             #
#        Python version 2.7.x or 3.4.x or higher                               #
#        Numpy version 1.11 or higher                                          #
#        Matplotlib version 1.4.2 or higher                                    #
#        Scipy version 0.13 or higher                                          #
#        Pandas version 0.16.x or higher                                       #
#                                                                              #
#   *There are two ways to write error-free programs; only the third works.    #
#   Alan J. Perlis                                                             #
#                                                                              #
# ============================================================================ #


from __future__ import division, print_function  # avoid python 2.x - 3.x compatibility issues
import os
import numpy as np
from numpy import mean, std, median, pi, sqrt, exp, log, array, tan, arctan, delete
from pandas import read_table, read_csv, DataFrame
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from scipy.optimize import curve_fit

import matplotlib as mpl
mpl.style.use('ggplot')  # set plot style
#mpl.rcParams['font.family'] = 'Helvetica Neue'  # uncomment this line to change the default font in the plots
mpl.rcParams['xtick.labelsize'] = 12.
mpl.rcParams['ytick.labelsize'] = 12.


def extract_areas(file_path, form='txt', col_name='Area'):
    """ Extract the data corresponding to the areas of grain profiles from the
    tabular-like data generated with the ImageJ application. Use always forward
    slashes (or double backslashes) in the file path to avoid problems.

    PARAMETERS

    file_path:
    the file location in the OS in quotes.

    form:
    the form of the file, either 'txt' or 'csv'.

    col_name:
    the name of the column that contains the areas of the grain profiles.
    It is set to 'Area' by default.
    """

    if form == 'txt':
        data_frame = read_table(file_path)
        data_set = array(data_frame[col_name])

    elif form == 'csv':
        data_frame = read_csv(file_path)
        data_set = array(data_frame[col_name])

    else:
        print("Form was not defined as 'txt' nor 'csv'. We assume that you meant 'csv'")
        return extract_areas(file_path, form='csv', col_name=col_name)

    print(' ')
    print(data_frame.head())
    print('...')
    print(data_frame.tail())
    print(' ')
    print('data extracted =', data_set)
    print('n =', len(data_set))
    print(' ')

    return data_set


def calc_diameters(areas, addPerimeter=0):
    """ Calculate the diameters from the sectional areas via the equivalent circular
    diameter.

    PARAMETERS

    areas:
    A numpy array with the sectional areas of the grains

    addPerimeter:
    Correct the diameters estimated from the areas by adding the perimeter of
    the grain. If addPerimeter is not declared, it is considered 0. A float or
    integer.
    """

    # calculate diameters via equivalent circular diameter
    diameters = 2 * sqrt(areas / pi)

    # diameter correction adding edges (if applicable)
    if addPerimeter != 0:
        diameters += addPerimeter

    return diameters


def find_grain_size(areas, diameters, plot='lin', binsize='auto'):
    """Estimate different 1D measures of grain size from a population
    of apparent diameters and their areas. It includes the mean, the
    area-weighted mean, the median and the frequency peak grain sizes.

    PARAMETERS

    areas:
    A numpy array with the areas of the grain profiles

    diameters:
    A numpy array with the apparent diameters of the grains

    plot:
    the preferred type of plot and grain size estimation. This can
    be 'lin' for a linear frequency vs diameter plot, 'log' for a
    frequency vs logarithmic diameter plot, 'sqrt' for a frequency
    vs square root diameter plot, and 'area' for a area-weighted
    frequency vs diameter plot.

    binsize:
    the method used to calculate the bin size. This can be 'auto',
    'fd' (Freedman-Diaconis rule), 'doane' (Doane's rule), 'scott'
    (Scott rule), 'sturges' (Sturge's rule), or a scalar
    of type integer or float. If not specified, the 'auto' rule
    is used by default.
    """

    # determine the grain size parameters using a number-weighted approach
    if plot == 'lin':
        return calc_freq_grainsize(diameters, binsize)
    elif plot == 'log':
        diameters = log(diameters)
        return calc_freq_grainsize(diameters, binsize, plot='log')
    elif plot == 'sqrt':
        diameters = sqrt(diameters)
        return calc_freq_grainsize(diameters, binsize, plot='sqrt')

    # determine the grain size using the area-weighted approach
    elif plot == 'area':
        return calc_areaweighted_grainsize(areas, diameters, binsize)
    else:
        print("Error: the type of plot was not defined as 'lin', 'log', 'sqrt' or 'area'. Try again.")
        return None


def derive3D(diameters, numbins=10, set_limit=None, fit=False, initial_guess=False):
    """Estimates the actual distribution of grain size from the population of
    apparent diameters measured in a thin section using two approaches:

    i) the Saltykov method (Saltykov 1967; Sahagian and Proussevitch 1998)
    ii) the two-step method (Lopez-Sanchez and Llana-Funez, 2016).

    The Saltykov method is optimal to estimate the volume of a particular grain size
    fraction as well as to obtain a qualitative view of the appearance of the actual
    3D grain size population, either in uni- or multimodal populations.

    The two-step method is aimed at estimating quantitatively the shape of the
    actual 3D distribution of grain sizes. The method only works properly for
    unimodal lognormal-like grain size populations (i.e. completely recrystallized
    rocks) and returns the MSD (i.e. shape) and median (i.e. scale) values that
    describe the lognormal population of grain sizes at their lineal scale. For
    details see Lopez-Sanchez and Llana-Funez (2016).

    REFERENCES

    Saltykov SA (1967) doi:10.1007/978-3-642-88260-9_31
    Sahagian and Proussevitch (1998) J. Vol. Geotherm. Res. doi:10.1029/95JB02500
    Lopez-Sanchez and Llana-Funez (2016) J. Struc. Geol. doi:10.1016/j.jsg.2016.10.008

    PARAMETERS

    diameters:
    A numpy array or Python list with the apparent diameters of the grains.

    numbins:
    The number of bins/classes of the histrogram. If not declared, is set by
    default to 10. An integer.

    set_limit:
    If the user defines a number, the script will return the volume occupied by the
    grain fraction of size less than or equal to that value. An integer or float.

    fit:
    If False, the standard Saltykov method is applied. If True, the two-step method
    is applied.

    initial_guess:
    If False, the script will use the default guessing values to fit the lognormal
    distribution. If True, the script will ask the user to define the MSD and
    median guessing values.
    """

    # compute the histogram
    freq, bin_edges = np.histogram(diameters, bins=numbins, range=(0., max(diameters)), density=True)
    binsize = bin_edges[1]
    print(' ')
    print('sample size =', len(diameters))
    print('bin size =', round(binsize, 2))
    print(' ')

    # Create an array with the left edges of the bins and other with the midpoints
    left_edges = delete(bin_edges, -1)
    mid_points = left_edges + binsize / 2.
    print('midpoints = ', np.around(mid_points, 2))

    # Applied the Scheil-Schwartz-Saltykov method to unfold the population of apparent diameters
    freq3D = Saltykov(freq, bin_edges, binsize, mid_points)
    print('class freqs. (norm.) =', np.around(freq3D, 4))

    # Calculates the volume-weighted cumulative frequency distribution
    x_vol = binsize * (4 / 3.) * pi * (mid_points**3)
    freq_vol = x_vol * freq3D
    cdf = np.cumsum(freq_vol)
    cdf_norm = 100 * (cdf / cdf[-1])
    print('cumulative vol. (%) =', np.around(cdf_norm, 2))  # Delete for released versions
    print(' ')

    if fit is False:
        if set_limit is not None:
            x = mid_points
            y = cdf_norm
            index = np.argmax(mid_points > set_limit)
            angle = arctan((y[index] - y[index - 1]) / (x[index] - x[index - 1]))
            volume = y[index - 1] + tan(angle) * (set_limit - x[index - 1])
            print('volume fraction (up to', set_limit, 'microns) =', round(volume, 2), '%')
            print(' ')

        # Generate the plot
        Saltykov_plot(left_edges, freq3D, binsize, mid_points, cdf_norm)

        # Save a text file with the midpoints, class frequencies, and cumulative volumes
        df = DataFrame({'mid_points': np.around(mid_points, 3), 'freqs': np.around(freq3D, 4), 'cum_vol': np.around(cdf_norm, 2)})
        print('A file named Saltykov_output.csv was generated')
        return df.to_csv('Saltykov_output.csv', sep='\t')

    # Fit a lognormal distribution with uncertainties to 3D data
    elif fit is True:
        if initial_guess is False:
            shape = 1.2
            scale = 25.0
        elif initial_guess is True:
            shape = float(input('Define an initial guess for the MSD parameter (the default value is 1.2; MSD > 1.0): '))
            scale = float(input('Define an initial guess for the median parameter (the default value is 25.0; median > 0.0 ): '))
        else:
            print('initial_guess was not set as True nor False. The default guessing values will be used')
            shape = 1.2
            scale = 25.0

        # optp = OPTimal Parameters for fit; covm = COVariance Matrix
        optp, covm = curve_fit(fit_function, mid_points, freq3D, [shape, scale])

        # estimate the uncertainty of the fit. We use the square root of the
        # diagonal values within the covariance matrix, which are the standard
        # deviations
        sigma_err = sqrt([covm[0, 0], covm[1, 1]])

        print(' ')
        print('Optimal coefficients:\n', '[MSD(shape) ; median]\n',
              round(optp[0], 2), ';', round(optp[1], 2))
        print(' ')
        print('Confidence interval\n', '[MSD(shape) ; median]\n',
              round(3 * sigma_err[0], 2), ';', round(3 * sigma_err[1], 2))
        print(' ')
        # print(' Covariance matrix:\n', covm)

        # Generate a mesh of x-values
        xgrid = gen_xgrid(diameters, 0.1, max(diameters))

        # Calculate the curve of the best fit
        best_fit = fit_function(xgrid, optp[0], optp[1])

        # Estimate all the combinatorial posibilities for fit curves taking into account the uncertainties
        values = array([fit_function(xgrid, optp[0] + sigma_err[0], optp[1] + sigma_err[1]),
                        fit_function(xgrid, optp[0] - sigma_err[0], optp[1] - sigma_err[1]),
                        fit_function(xgrid, optp[0] + sigma_err[0], optp[1] - sigma_err[1]),
                        fit_function(xgrid, optp[0] - sigma_err[0], optp[1] + sigma_err[1])])

        # Estimate the standard deviation of the all values obtained
        # I use this approach instead of getting the min a max values obtained
        fit_error = std(values, axis=0)

        # Generate the plot
        twostep_plot(left_edges, freq3D, binsize, mid_points, freq3D, xgrid, best_fit, fit_error)

        # Save a text file with the midpoints and class frequencies
        df = DataFrame({'mid_points': np.around(mid_points, 3), 'freqs': np.around(freq3D, 4)})
        print('A file named twoStep_output.csv was generated')
        return df.to_csv('twoStep_output.csv', sep='\t')

    else:
        print('fit parameter was not defined as True nor False. Please try again.')
        return None


# ============================================================================ #
# Functions used by the find_grain_size and the derive3D functions to plot the #
# results using the matplotlib capabilities. I use hex color codes to set the  #
# colors.                                                                      #
# ============================================================================ #

def freq_plot(diameters, binList, xgrid, y_values, y_max, x_peak, mean_GS, median_GS,
              plot='freq'):
    """ Generate a frequency vs grain size plot."""

    plt.figure(tight_layout=True)
    plt.gcf().subplots_adjust(bottom=0.15)  # this is to prevent x-label cut off

    plt.hist(diameters,
             bins=binList,
             range=(0, diameters.max()),
             normed=True,
             color='#66C2A5',
             edgecolor='#EBF7F3')
    plt.plot([mean_GS, mean_GS], [0.0001, y_max],
             linestyle='-',
             color='#e7298a',
             label='mean grain size',
             linewidth=2)
    plt.plot([median_GS, median_GS], [0.0001, y_max],
             linestyle='-',
             color='#7570b3',
             label='median grain size',
             linewidth=2)
    plt.plot(xgrid, y_values,
             color='#252525',
             label='Gaussian KDE',
             linewidth=2)
    plt.ylabel('frequency',
               fontsize=15)
    if plot == 'freq':
        plt.xlabel(r'apparent diameter ($\mu m$)',
                   fontsize=15)
        plt.title('Linear grain size distribution',
                  color='#525252',
                  fontsize=16,
                  y=1.02)
    elif plot == 'log':
        plt.xlabel(r'apparent diameter ln ($\mu m$)',
                   fontsize=15)
        plt.title('Logarithmic (base e) grain size distribution',
                  color='#525252',
                  fontsize=16,
                  y=1.02)
    elif plot == 'sqrt':
        plt.xlabel(r'apparent diameter sqrt ($\mu m$)',
                   fontsize=15)
        plt.title('Square root grain size distribution',
                  color='#525252',
                  fontsize=16,
                  y=1.02)
    plt.plot([x_peak], [y_max],
             'o',
             color='#252525')
    plt.vlines(x_peak, 0.0001, y_max,
               linestyle='--',
               color='#252525',
               linewidth=2)
    plt.annotate('Gaussian KDE peak',
                 xy=(x_peak, y_max),
                 xytext=(+10, +30),
                 label='peak')
    plt.legend(loc='upper right',
               fontsize=13)

    return plt.show()


def area_weighted_plot(intValues, cumulativeAreas, h, weightedMean):
    """ Generate the area-weighted frequency vs grain size plot."""

    plt.figure(tight_layout=True)
    plt.gcf().subplots_adjust(bottom=0.15)  # this is to prevent x-label cut off

    # normalize the y-axis values to percentage of the total area
    totalArea = sum(cumulativeAreas)
    cumulativeAreasNorm = [(x / float(totalArea)) * 100 for x in cumulativeAreas]
    maxValue = max(cumulativeAreasNorm)

    # figure aesthetics stuff
    plt.bar(intValues, cumulativeAreasNorm, width=h,
            color='#66C2A5',
            edgecolor='#EBF7F3')
    plt.plot([weightedMean, weightedMean], [0.0001, maxValue],
             linestyle='--',
             color='#252525',
             label='area weighted mean',
             linewidth=2)
    plt.ylabel('% of area fraction within the interval',
               fontsize=15)
    plt.xlabel(r'apparent diameter ($\mu m$)',
               fontsize=15)
    plt.title('Area-weighted grain size distribution',
              color='#525252',
              fontsize=16,
              y=1.02)
    plt.legend(loc='upper right',
               fontsize=13)

    return plt.show()


def Saltykov_plot(left_edges, freq3D, binsize, mid_points, cdf_norm):
    """ Generate two plots uding the Saltykov method: i) A frequency plot,
    and ii) a volume-weighted cumulative frequency plot"""

    plt.figure(figsize=(13, 5), tight_layout=True)
    plt.gcf().subplots_adjust(bottom=0.15)  # this is to prevent x-label cut off

    plt.subplot(121)
    plt.bar(left_edges, freq3D,
            width=binsize,
            color='#80b1d3',
            edgecolor='#EBF7F3')
#    plt.plot(mid_points, freq3D,
#             'o',
#             color='#fb8072')
    plt.ylabel('frequency',
               fontsize=15)
    plt.xlabel(r'diameter ($\mu m$)',
               fontsize=15)
    plt.title('estimated 3D grain size distribution',
              color='#525252',
              fontsize=16,
              y=1.02)

    plt.subplot(122)
    plt.ylim([0, 105])
    plt.plot(mid_points, cdf_norm,
             'o-',
             color='#ed4256',
             label='volume weighted CDF',
             linewidth=2)
    plt.ylabel('cumulative volume (%)',
               fontsize=15)
    plt.xlabel(r'diameter ($\mu m$)',
               fontsize=15)
    plt.title('volume-weighted cumulative freq. distribution',
              color='#525252',
              fontsize=16,
              y=1.02)

    return plt.show()


def twostep_plot(left_edges, freq3D, binsize, mid_points_corrected,
                 freq3D_corrected, xgrid, best_fit, fit_error):
    """ Generate a plot applying the two-step method.

    Reference:
    Lopez-Sanchez and Llana-Funez (2016) J. Struc. Geol 93:149-161
    """

    plt.figure(tight_layout=True)
    plt.gcf().subplots_adjust(bottom=0.15)  # this is to prevent x-label cut off

    # log-normal distribution
    plt.plot(xgrid, best_fit,  # best fit
             color='#525252',
             label='best fit',
             linewidth=2)
    plt.plot(mid_points_corrected, freq3D_corrected,  # datapoints used for the fitting procedure
             'o',
             color='#d53e4f',
             label='Datapoints',
             linewidth=1.5,
             alpha=0.75)
    plt.fill_between(xgrid, best_fit + (3 * fit_error), best_fit - (3 * fit_error),
                     color='#525252',
                     label='trust region',
                     alpha=0.5)
    # bar plot from Saltykov method
    plt.bar(left_edges, freq3D,
            width=binsize,
            color='#3288bd',
            label='Saltykov method',
            linewidth=1,
            edgecolor='#ffffff',
            alpha=0.5)

    plt.ylabel('freq. (per unit vol.)',
               fontsize=15)
    plt.legend(loc='upper right',
               fontsize=13)
    plt.xlabel(r'diameter ($\mu m$)',
               fontsize=15)

    return plt.show()


# ============================================================================== #
# functions used by the find_grain_size and the derive3D functions to obtain all #
# the parameters needed to estimate the grain size and generate the plots. The   #
# names of the functions are self-explanatory.                                   #
# ============================================================================== #

def calc_freq_grainsize(diameters, binsize, plot='freq'):
    """ Calculate the histogram and the Gaussian kernel density estimator of the
    grain diameters population. It prints the modal interval, the middle value of
    the modal interval and the Gaussian kernel density estimation peak. It returns
    a list with the histogram bin edges, the x and y values neccesary to build the
    Gaussian kde curve and the x and y location of the Gaussian kde peak. This
    values will be used later to make the number weighted plot.

    PARAMETERS

    diameters:
    A numpy array or Python list with the diameters of the grains

    binsize:
    A string (rule of thumb), integer or float.

    plot:
    The type of plot and grain size, either 'freq', 'log' or 'sqrt'.
    """

    mean_GS = mean(diameters)
    median_GS = median(diameters)

    # estimate the histogram and the bin edges
    histogram, bin_edges = np.histogram(diameters, bins=binsize, range=(0.0, diameters.max()))
    h = bin_edges[1]

    # find the grain size range in which the histogram value is the maximum
    index = np.argmax(histogram)  # see numpy.argmax for details
    modInt_leftEdge = bin_edges[index]
    modInt_rightEdge = modInt_leftEdge + h

    # calculate the Gaussian kernel density function
    # the bandwidth selection is based on the Silverman rule (Silverman 1986)
    kde = gaussian_kde(diameters, bw_method=my_kde_bandwidth)

    # determine where the Gaussian kde function reach it maximum value
    xgrid = gen_xgrid(diameters, diameters.min(), diameters.max())  # generate x-values
    y_values = kde(xgrid)  # generate y-values using the gaussian kde function estimated
    y_max = np.max(y_values)  # get maximum value
    index = np.argmax(y_values)  # get the index of the maximum value along the y-axis
    x_peak = xgrid[index]  # get the diameter (x-value) where y-value is maximum

    if plot == 'freq':
        print(' ')
        print('NUMBER WEIGHTED APPROACH (linear apparent grain size):')
        print(' ')
        print('Mean grain size =', round(mean_GS, 2), 'microns')
        print('Median grain size =', round(median_GS, 2), 'microns')
        print(' ')
        print('HISTOGRAM FEATURES')
        print('The modal interval is', round(modInt_leftEdge, 2), '-', round(modInt_rightEdge, 2))
        # print('Middle value =', round((modInt_leftEdge+modInt_rightEdge)/2., 1), 'microns')
        print('The number of classes are', len(histogram))
        if type(binsize) is str:
            print('The bin size is', round(h, 2), 'according to the', binsize, 'rule')
        print(' ')
        print('GAUSSIAN KERNEL DENSITY ESTIMATOR FEATURES')
        print('KDE peak (peak grain size) = ', round(x_peak, 2), 'microns')
        print('Bandwidth =', round(kde.covariance_factor() * diameters.std(ddof=1), 2), '(Silverman rule)')
        print(' ')

        return freq_plot(diameters, bin_edges, xgrid, y_values, y_max, x_peak, mean_GS, median_GS)

    elif plot == 'log':
        print(' ')
        print('NUMBER WEIGHTED APPROACH (log apparent grain size):')
        print(' ')
        print('Mean (log) grain size =', round(mean_GS, 2), 'microns')
        print('Median (log) grain size =', round(median_GS, 2), 'microns')
        print(' ')
        print('HISTOGRAM FEATURES')
        print('The modal interval is', round(modInt_leftEdge, 2), '-', round(modInt_rightEdge, 2))
        # print('Middle value =', round((modInt_leftEdge+modInt_rightEdge)/2., 1), 'microns')
        print('The number of classes are', len(histogram))
        if type(binsize) is str:
            print('The bin size is', round(h, 2), 'according to the', binsize, 'rule')
        print(' ')
        print('GAUSSIAN KERNEL DENSITY ESTIMATOR FEATURES')
        print('KDE peak (peak grain size) = ', round(x_peak, 2), 'microns')
        print('Bandwidth =', round(kde.covariance_factor() * diameters.std(ddof=1), 2), '(Silverman rule)')
        print(' ')

        return freq_plot(diameters, bin_edges, xgrid, y_values, y_max, x_peak, mean_GS, median_GS, plot='log')

    elif plot == 'sqrt':
        print(' ')
        print('NUMBER WEIGHTED APPROACH (square root apparent grain size):')
        print(' ')
        print('Mean (sqrt) grain size =', round(mean_GS, 2), 'microns')
        print('Median (sqrt) grain size =', round(median_GS, 2), 'microns')
        print(' ')
        print('HISTOGRAM FEATURES')
        print('The modal interval is', round(modInt_leftEdge, 2), '-', round(modInt_rightEdge, 2))
        # print('Middle value =', round((modInt_leftEdge+modInt_rightEdge)/2., 1), 'microns')
        print('The number of classes are', len(histogram))
        if type(binsize) is str:
            print('The bin size is', round(h, 2), 'according to the', binsize, 'rule')
        print(' ')
        print('GAUSSIAN KERNEL DENSITY ESTIMATOR FEATURES')
        print('KDE peak (peak grain size) = ', round(x_peak, 2), 'microns')
        print('Bandwidth =', round(kde.covariance_factor() * diameters.std(ddof=1), 2), '(Silverman rule)')
        print(' ')

        return freq_plot(diameters, bin_edges, xgrid, y_values, y_max, x_peak, mean_GS, median_GS, plot='sqrt')


def gen_xgrid(pop, start, stop):
    """Returns a mesh of x_values.

    PARAMETERS

    pop:
    the population

    start:
    the starting value of the sequence

    stop:
    the end value of the sequence
    """

    d_range = pop.max() - pop.min()

    if d_range < 400:
        density = 2**12
    else:
        density = 2**14

    return np.linspace(start, stop, density)


def my_kde_bandwidth(obj, fac=1.):
    """Returns the Silverman bandwidth multiplied by a constant factor
    if neccesary. Returns the bandwidth of the Gaussian kde.

    obj: the kde object
    fac: the constant factor, 1. as default
    """

    bandwidth = np.power(obj.n * (obj.d + 2.0) / 4.0, -1. / (obj.d + 4)) * fac

    return bandwidth


def calc_areaweighted_grainsize(areas, diameters, binsize):
    """ Calculates the area percentage of each grain size interval. It is
    based on Herwegh (2000) and Berger et al. (2011) approach. Returns the
    the grain size interval with the maximum area accumulated, the middle
    value of this interval and the area weighted arithmetic mean.

    REFERENCES

    Herwegh (2000) doi:10.1016/S0191-8141(99)00165-0
    Berger et al. (2011) doi:10.1016/j.jsg.2011.07.002

    PARAMETERS

    areas:
    A numpy array or Python list with the sectional areas of the grains

    diameters:
    A numpy array or Python list with the estimated diameters of the grains

    binsize:
    the bin size, an integer or float
    """

    # calculate the area weighted arithmetic mean
    areatotal = float(sum(areas))
    weightedAreas = areas / areatotal
    weigtedDiameters = diameters * weightedAreas
    weightedMean = sum(weigtedDiameters)

    # sort arrays
    areas.sort()
    diameters.sort()

    minVal = 0
    maxVal = max(diameters)

    # Create a Python dictionary with diameters as keys and the corresponding areas as values
    values = dict(zip(diameters, areas))

    #  estimate the bin size when using automatic plug-in methods
    if type(binsize) is str:
        histogram, bin_edges = np.histogram(diameters, bins=binsize, range=(0.0, diameters.max()))
        h = bin_edges[1]

    # Initialize variables
    x = int(minVal)
    y = x + h
    cumulativeAreas = []
    intValues = []

    intValues.append(x)

    while True:
        suma = 0
        if x < maxVal:
            for key in values:
                if key > x and key <= y:
                    suma += values[key]
            cumulativeAreas.append(round(suma, 1))  # append the sum of the areas for each interval defined
            x = y
            y = x + h
            intValues.append(round(x, 2))  # append the lower/left edge of the interval

        else:
            cumulativeAreas.append(0)  # add one element at the end of the list
            getIndex = cumulativeAreas.index(max(cumulativeAreas))  # get the index of the maximum value (the modal interval)
            print(' ')
            print('AREA WEIGHTED APPROACH:')
            print(' ')
            print('Area-weighted mean grain size =', round(weightedMean, 2), 'microns')
            print(' ')
            print('HISTOGRAM FEATURES')
            print('The modal interval is', intValues[getIndex], '-', (intValues[getIndex] + round(h, 2)), 'microns')
            print('Midpoint (of modal interval) =', round((intValues[getIndex] + (intValues[getIndex] + h)) / 2.0, 1), 'microns')
            print('The number of classes are', len(cumulativeAreas) - 1)
            if type(binsize) is str:
                print('The bin size is', round(h, 2), 'according to the', binsize, 'rule')
            print(' ')

            return area_weighted_plot(intValues, cumulativeAreas, h, weightedMean)


def wicksell_eq(D, d1, d2):
    """ This is the equation that calculates the cross-section size probability
    for a sphere based on Wicksell (1925) and later used by Scheil (1931),
    Schwartz (1934) and Saltykov (1967) to develop the Scheil-Schwartz-Saltykov
    method. This is the generalization by Sahagian and Proussevitch (1998).

    P(r1<r<r2) = 1/R * (sqrt(R^2-r1^2) - sqrt(R^2-r2^2))

    where R is the sphere radius and r the cross-section radius. Specifically r1
    and r2 are the user-defined lower and upper bounds, respectively.

    REFERENCES

    Sahagian and Proussevitch (1998) doi:10.1029/95JB02500
    Saltykov (1967) doi:10.1007/978-3-642-88260-9_31
    Scheil (1931) doi:10.1002/zaac.19312010123
    Schwartz (1934) Met. Alloy 5:139
    Wicksell (1925) doi:10.2307/2332027

    PARAMETERS

    D:
    the midpoint of the actual class, which corresponds with the diameter

    d1:
    the lower limit of the bin/class

    d2:
    the upper limit of the bin/class
    """

    # convert diameters to radii
    R = D / 2.0
    r1 = d1 / 2.0
    r2 = d2 / 2.0

    return 1 / R * (sqrt(R**2 - r1**2) - sqrt(R**2 - r2**2))


def Saltykov(freq, bin_edges, binsize, mid_points, normalize=True):
    """ Applies the Scheil-Schwartz-Saltykov method to unfold the population of
    apparent 2D diameters into the actual 3D population of grain sizes.
    Following the reasoning of Higgins (2000), R (or D) is placed at the center
    of the classes (i.e. the midpoints). It returns the normalized frequencies
    of the unfolded population such that the integral over the range considered
    is one.

    REFERENCES

    Higgins (2000) doi:10.2138/am-2000-8-901

    PARAMETERS

    freq:
    an array or Python list with the frequency of the classes or bins

    bin_edges:
    an array or Python list with the edges of the classes or bins

    mid_points:
    the midpoints of the classes

    normalize:
    when set to True, frequency negative values are set to zero and the
    distribution is normalized. It is set to True by default.
    """

    d_values = np.copy(bin_edges)
    midpoints = np.copy(mid_points)
    i = len(midpoints) - 1

    while i > 0:
        j = i
        D = d_values[-1]
        Pi = wicksell_eq(D, d_values[i], d_values[i + 1])

        if freq[i] > 0:
            while j > 0:
                D = midpoints[-1]
                Pj = wicksell_eq(D, d_values[j - 1], d_values[j])
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
        freq = np.clip(freq, 0., 2**20)  # replacing all negative values with zero
        freq_norm = freq / sum(freq)  # normalize to one
        freq_norm = freq_norm / binsize  # normalize such that the integral over the range is one
        return freq_norm

    elif normalize is False:
        return freq


def fit_function(x, shape, scale):
    """ Defines a custom function so that scipy curve_fit routine will use to fit
    the data. In this case, it is the two-parameter equation that describes a lognormal
    distribution using the mean and the standard deviation of the log(x) with base e.

    PARAMETERS

    x:
    the x-values

    shape:
    the shape parameter; it relates to the sigma parameter: s = log(shape)

    scale:
    the scale parameter; it relates to the mean of log(x): m = log(scale)
    """

    s = log(shape)
    m = log(scale)

    return 1 / (x * s * sqrt(2 * pi)) * exp(-1 / 2. * ((log(x) - m)**2 / s**2))


print(' ')
print('Welcome to the GrainSizeTools script v1.3')
print('Your current working directory is', os.getcwd())
print("To change the working directory use: os.chdir('new path')")
print(' ')
print('Please to avoid problems check that your Numpy version below is 1.11 or higher:')
print('The installed Numpy version in your system is', np.__version__)
print(' ')

# ============================================================================ #
# Make it correct, make it clear, make it concise, make it fast. In that order.#
#                                                                     Wes Dyer #
# ============================================================================ #
