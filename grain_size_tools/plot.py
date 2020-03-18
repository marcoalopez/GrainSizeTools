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
# Functions to generate the plots using the Python matplotlib library.         #
# It uses hex color codes to set colors.                                       #
# Save this file in the same directory as GrainSizeTools                       #
# ============================================================================ #

# import Python scientific modules
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, gaussian_kde, shapiro


# plotting funtions
def distribution(data,
                 plot=('hist', 'kde'),
                 avg=('amean', 'gmean', 'median', 'mode'),
                 binsize='auto', bandwidth='silverman'):
    """ Return a plot with the ditribution of (apparent or actual) grain sizes
    in a dataset.

    Parameters
    ----------
    diameters : array_like
        the apparent diameters of the grains

    plot : string, tuple or list
        the type of plot, either histogram ('hist'), kernel density estimate
        ('kde') or both ('hist', 'kde'). Default is both.

    avg : string, tuple or list
        the central tendency measures o show, either the arithmetic ('amean')
        or geometric ('gmean') means, the median ('median'), and/or the
        KDE-based mode ('mode'). Default all averages.

    binsize : string or positive scalar, optional
        If 'auto', it defines the plug-in method to calculate the bin size.
        When integer or float, it directly specifies the bin size.
        Default: the 'auto' method.

        | Available plug-in methods:
        | 'auto' (fd if sample_size > 1000 or Sturges otherwise)
        | 'doane' (Doane's rule)
        | 'fd' (Freedman-Diaconis rule)
        | 'rice' (Rice's rule)
        | 'scott' (Scott rule)
        | 'sqrt' (square-root rule)
        | 'sturges' (Sturge's rule)

    bandwidth : string {'silverman' or 'scott'} or positive scalar, optional
        the method to estimate the bandwidth or a scalar directly defining the
        bandwidth. It uses the Silverman plug-in method by default.

    Call functions
    --------------
    - gaussian_kde (from Scipy stats)

    Examples
    --------
    >>> distribution(data['diameters'])

    Returns
    -------
    A plot showing the distribution of (apparent) grain sizes and
    the location of the averages defined.
    """

    fig, ax = plt.subplots()

    if 'hist' in plot:
        y_values, bins, __ = ax.hist(data,
                                     bins=binsize,
                                     range=(data.min(), data.max()),
                                     density=True,
                                     color='#80419d',
                                     edgecolor='#C59fd7',
                                     alpha=0.7)
        print('=======================================')
        print('Number of classes = ', len(bins) - 1)
        print('binsize = ', round(bins[1], 2))
        print('=======================================')

    if 'kde' in plot:
        # estimate kde first
        if isinstance(bandwidth, (int, float)):
            fixed_bw = bandwidth / np.std(data, ddof=1)
            kde = gaussian_kde(data, bw_method=fixed_bw)
        elif isinstance(bandwidth, str):
            kde = gaussian_kde(data, bw_method=bandwidth)
            bandwidth = round(kde.covariance_factor() * data.std(ddof=1), 2)
        else:
            raise ValueError("bandwidth must be integer, float, or plug-in methods 'silverman' or 'scott'")

        x_values = np.linspace(data.min(), data.max(), num=1000)
        y_values = kde(x_values)

        print('=======================================')
        print('KDE bandwidth = ', round(bandwidth, 2))
        print('=======================================')

        if 'hist' in plot:
            ax.plot(x_values, y_values,
                    color='#2F4858')
        else:
            ax.plot(x_values, y_values,
                    color='#2F4858')
            ax.fill_between(x_values, y_values,
                            color='#80419d',
                            alpha=0.65)

    # plot the location of the averages
    if 'amean' in avg:
        amean = np.mean(data)
        ax.vlines(amean, 0, np.max(y_values),
                  linestyle='solid',
                  color='#2F4858',
                  label='arith. mean',
                  linewidth=2.5)

    if 'gmean' in avg:
        gmean = np.exp(np.mean(np.log(data)))
        ax.vlines(gmean, 0, np.max(y_values),
                  linestyle='solid',
                  color='#fec44f',
                  label='geo. mean')

    if 'median' in avg:
        median = np.median(data)
        ax.vlines(median, 0, np.max(y_values),
                  linestyle='dashed',
                  color='#2F4858',
                  label='median',
                  linewidth=2.5)

    if 'mode' in avg and 'kde' in plot:
        mode = x_values[np.argmax(y_values)]
        ax.vlines(mode, 0, np.max(y_values),
                  linestyle='dotted',
                  color='#2F4858',
                  label='mode',
                  linewidth=2.5)

    ax.set_ylabel('density', color='#252525')
    ax.set_xlabel(r'apparent diameter ($\mu m$)', color='#252525')
    ax.legend(loc='best', fontsize=16)
#    ax.set_ylim(bottom=-0.001)

    fig.tight_layout()

    return None


def area_weighted(diameters, areas, binsize='auto'):
    """ Generate the area-weighted histogram"""

    # estimate weighted mean
    area_total = np.sum(areas)
    weighted_areas = areas / area_total
    weighted_mean = np.sum(diameters * weighted_areas)

    # estimate mode interval
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

    # get the the modal interval and the midpoint
    getIndex = np.argmax(cumulativeAreas)
    mode = bin_edges[getIndex] + (bin_edges[getIndex] + h) / 2.0

    print('=======================================')
    print('DESCRIPTIVE STATISTICS')
    print('Area-weighted mean grain size = {:0.2f} microns' .format(weighted_mean))
    print('=======================================')
    print('HISTOGRAM FEATURES')
    print('The modal interval is {left:0.2f} - {right:0.2f} microns' .format(left=bin_edges[getIndex],
                                                                             right=bin_edges[getIndex] + h))
    print('Midpoint (of modal interval) = {:0.2f} microns' .format(mode))
    print('The number of classes are {}' .format(len(histogram)))
    if type(binsize) is str:
        print('The bin size is {bin:0.2f} according to the {rule} rule' .format(bin=h, rule=binsize))
    print('=======================================')

    # normalize the y-axis values to percentage of the total area
    totalArea = sum(cumulativeAreas)
    cumulativeAreasNorm = [(x / float(totalArea)) * 100 for x in cumulativeAreas]
    maxValue = max(cumulativeAreasNorm)

    #make plot
    fig, ax = plt.subplots()

    # figure aesthetics
    ax.bar(bin_edges, cumulativeAreasNorm, width=h,
           color='#55A868',
           edgecolor='#FEFFFF',
           align='edge',
           alpha=0.9)
    ax.vlines(weighted_mean, ymin=0, ymax=maxValue,
              linestyle='--',
              color='#1F1F1F',
              label='area weighted mean',
              linewidth=2)
    ax.set_ylabel('normalized area fraction (%)', fontsize=15)
    ax.set_xlabel(r'apparent diameter ($\mu m$)', fontsize=15)
    ax.legend(loc='best', fontsize=15)

    fig.tight_layout()

    return None


def normalized(data, avg='amean', bandwidth='silverman'):
    """Return a log-transformed normalized ditribution of the grain
    population. This is useful to compare grain size distributions
    beween samples with different average values.

    Parameters
    ----------
    data : array-like
        the dataset
    avg : str, optional
        the normalization factor, either 'amean', 'median', or
        'mode'. Default: 'amean'
    bandwidth : str, optional
        the bandwidth of the KDE, by default 'silverman'
    """

    data = np.log(data)
    amean = np.mean(data)
    median = np.median(data)

    # normalize
    if avg == 'amean':
        norm_factor = amean
        norm_data = data / norm_factor
    elif avg == 'median':
        norm_factor = median
        norm_data = data / median
#    elif avg == 'mode':
#        __, __, mode, __, __ = avrages.freq_peak(data, bandwidth)
#        norm_data = data / mode
    else:
        raise ValueError('Normalization factor has to be defined as amean, median, or mode')

    # estimate kde
    if isinstance(bandwidth, (int, float)):
        fixed_bw = bandwidth / np.std(norm_data, ddof=1)
        kde = gaussian_kde(norm_data, bw_method=fixed_bw)
    elif isinstance(bandwidth, str):
        kde = gaussian_kde(norm_data, bw_method=bandwidth)
        bandwidth = round(kde.covariance_factor() * norm_data.std(ddof=1), 2)
    else:
        raise ValueError("bandwidth must be integer, float, or plug-in methods 'silverman' or 'scott'")

    x_values = np.linspace(norm_data.min(), norm_data.max(), num=1000)
    y_values = kde(x_values)

    print('=======================================')
    print('KDE bandwidth = ', round(bandwidth, 2))
    print('=======================================')

    #make plot
    fig, ax = plt.subplots()

    ax.plot(x_values, y_values,
            color='#2F4858')
    ax.fill_between(x_values, y_values,
                    color='#d1346b',
                    alpha=0.5)
    ax.vlines(amean / norm_factor, 0, np.max(y_values),
              linestyle='solid',
              color='#2F4858',
              label='arith. mean',
              linewidth=2.5)
    ax.vlines(median / norm_factor, 0, np.max(y_values),
              linestyle='dashed',
              color='#2F4858',
              label='median',
              linewidth=2.5)

    ax.set_ylabel('density', fontsize=18)
    ax.set_xlabel(r'normalized log grain size ($\mu m$)', fontsize=18)
    ax.legend(loc='best', fontsize=15)

    fig.tight_layout()

    return fig, ax


def qq_plot(data, percent=2):
    """ Plot quantile–quantile (q-q) plot to test whether the
    the underlying distribution follows a lognormal distribution.

    Parameters
    ----------
    data : array-like
        the apparent diameters or any other type of data

    percent : scalar between 0 and 100
        the percentil interval to estimate, default is 2 %

    Call functions
    --------------
    probplot from scipy's stats
    """

    data = np.sort(np.log(data))

    # estimate percentiles in the actual data
    percentil = np.arange(1, 100, percent)
    actual_data = np.percentile(data, percentil)

    # estimate percentiles for theoretical data
    mean, std = np.mean(data), np.std(data)
    theoretical_data = norm.ppf(percentil / 100, loc=mean, scale=std)

    min_val, max_val = theoretical_data.min(), theoretical_data.max()

    # make the plot
    fig, ax = plt.subplots()

    ax.plot([min_val, max_val], [min_val, max_val],
            '-',
            color='#2F4858',
            label='perfect lognormal')
    ax.plot(theoretical_data, actual_data,
            'o',
            color='C0',
            alpha=0.5)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel('theoretical', fontsize=18)
    ax.set_ylabel('observed', fontsize=18)
    ax.legend(loc='best', fontsize=18)

    fig.tight_layout()

    # Shapiro-Wilk test
    W, p_value = shapiro(data)
    print('=======================================')
    print('Shapiro-Wilk test (lognormal):')
    print('{:0.2f}, {:0.2f} (test statistic, p-value)' .format(W, p_value))
    if p_value >= 0.1:
        print('It looks like a lognormal distribution')
        print('(⌐■_■)')
    else:
        print('It doesnt look like a lognormal distribution (p-value > 0.1)')
        print('(╯°□°）╯︵ ┻━┻')
    print('=======================================')

    return None


if __name__ == '__main__':
    pass
else:
    print('module plot imported')
