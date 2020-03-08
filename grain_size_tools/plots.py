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
import matplotlib as mpl
from cycler import cycler
import numpy as np
from scipy.stats import norm, gaussian_kde

# Set the plot style
#mpl.rcParams['font.family'] = 'Helvetica Neue'  # set your own font family
mpl.rcParams['font.size'] = 14.0
mpl.rcParams['svg.fonttype'] = 'path'
mpl.rcParams['lines.linewidth'] = 3.0
mpl.rcParams['lines.markersize'] = 12.0
mpl.rcParams['lines.solid_capstyle'] = 'butt'
mpl.rcParams['legend.fancybox'] = True

mpl.rcParams['axes.prop_cycle'] = cycler(color=['#008fd5', '#fc4f30', '#e5ae38', '#6d904f', '#8b8b8b', '#810f7c'])
mpl.rcParams['axes.facecolor'] = 'ffffff'
mpl.rcParams['axes.labelsize'] = 'large'
mpl.rcParams['axes.axisbelow'] = True
mpl.rcParams['axes.grid'] = True
mpl.rcParams['axes.edgecolor'] = 'ffffff'
mpl.rcParams['axes.linewidth'] = 2.0
mpl.rcParams['axes.titlesize'] = 'x-large'

mpl.rcParams['patch.edgecolor'] = 'f0f0f0'
mpl.rcParams['patch.linewidth'] = 0.5

mpl.rcParams['grid.linestyle'] = '-'
mpl.rcParams['grid.linewidth'] = 1.0
mpl.rcParams['grid.color'] = 'cbcbcb'

mpl.rcParams['xtick.major.size'] = 0
mpl.rcParams['xtick.minor.size'] = 0
mpl.rcParams['ytick.major.size'] = 0
mpl.rcParams['ytick.minor.size'] = 0
mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.labelsize'] = 16
mpl.rcParams['xtick.color'] = '#252525'
mpl.rcParams['ytick.color'] = '#252525'

mpl.rcParams['savefig.edgecolor'] = 'ffffff'
mpl.rcParams['savefig.facecolor'] = 'ffffff'

mpl.rcParams['figure.subplot.left'] = 0.125
mpl.rcParams['figure.subplot.right'] = 0.9
mpl.rcParams['figure.subplot.bottom'] = 0.11
mpl.rcParams['figure.subplot.top'] = 0.88
mpl.rcParams['figure.facecolor'] = 'ffffff'


# plotting funtions
def distribution(data,
                 plot=('hist', 'kde'),
                 avg=('amean', 'gmean', 'median', 'mode'),
                 binsize='auto', bandwidth='silverman', precision=None):
    """ Return a plot with the ditribution of (apparent or actual) grain sizes
    in a dataset.

    Parameters
    ----------
    diameters : array_like
        the apparent diameters of the grains

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

    precision : positive scalar or None, optional
        the maximum precision expected for the "peak" kde-based estimator.
        Default is None

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
        ax.hist(data,
                bins=binsize,
                range=(data.min(), data.max()),
                density=True,
                color='#80419d',
                edgecolor='#C59fd7',
                alpha=0.7)

    if 'kde' in plot:
        # estimate kde first
        if isinstance(bandwidth, (int, float)):
            bw = bandwidth / np.std(data, ddof=1)
            kde = gaussian_kde(data, bw_method=bw)
        elif isinstance(bandwidth, str):
            kde = gaussian_kde(data, bw_method=bandwidth)
            bw = round(kde.covariance_factor() * data.std(ddof=1), 2)
        else:
            raise ValueError("bandwidth must be integer, float, or plug-in methods 'silverman' or 'scott'")

        x_values = np.linspace(data.min(), data.max(), num=1000)
        y_values = kde(x_values)

        if 'hist' in plot:
            ax.plot(x_values, y_values,
                    color='#2F4858',
                    label='KDE')
        else:
            ax.plot(x_values, y_values,
                    color='#C59fd7')
            ax.fill_between(x_values, y_values,
                            color='#80419d',
                            alpha=0.5,
                            label='KDE')

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

    if 'mode' in avg:
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

    return fig, ax


def area_weighted(diameters, areas, binsize='auto'):
    """ Generate the area-weighted histogram normalized so that
    the integral of the density over the range is one"""

    # estimate weighted mean
    area_total = np.sum(areas)
    weighted_areas = areas / area_total
    weighted_mean = np.sum(diameters * weighted_areas)

    #make plot
    fig, ax = plt.subplots()

    # figure aesthetics
    ax.hist(diameters,
            bins=binsize,
            range=(diameters.min(), diameters.max()),
            weights=weighted_areas,
            color='#55A868',
            edgecolor='#FEFFFF',
            alpha=0.8)
    ax.vlines(weighted_mean, ymin=0, ymax=np.mean(weighted_mean) * 2,
              linestyle='--',
              color='#1F1F1F',
              label='area weighted mean',
              linewidth=2)
    ax.set_ylabel('normalized area fraction (%)', fontsize=15)
    ax.set_xlabel(r'apparent diameter ($\mu m$)', fontsize=15)
    ax.legend(loc='best', fontsize=15)

    fig.tight_layout()

    return fig, ax


def normalized_distribution(data, binsize='auto'):
    pass


def log_distribution(data, binsize='auto'):
    pass


def sqrt_distribution(data, binsize='auto'):
    pass


def Saltykov_plot(left_edges, freq3D, binsize, mid_points, cdf_norm):
    """ Generate two plots once the Saltykov method is applied:

    i)  a bar plot (ax1)
    ii) a volume-weighted cumulative frequency plot (ax2)
    """

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(13, 5))

    # frequency vs grain size plot
    ax1.bar(left_edges, freq3D,
            width=binsize,
            color='#404040',
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

    return plt.show()


def twostep_plot(xgrid, mid_points, frequencies, best_fit, fit_error):
    """ Generate a plot with the best fitting lognormal distribution (two-step method)"""

    # matplotlib stuff
    fig, ax = plt.subplots()

    # bar plot from Saltykov method
    ax.bar(mid_points, frequencies,
           width=mid_points[1] - mid_points[0],
           edgecolor='#1F1F1F',
           hatch='//',
           color='#fff2ae',
           fill=False,
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

    return plt.show()


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
    ax.set_xlabel('theoretical', fontsize=16)
    ax.set_ylabel('observed', fontsize=16)
    ax.legend(loc='best', fontsize=15)

    fig.tight_layout()

    return fig, ax
