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
# Functions to generate the plots using the Python matplotlib library.         #
# It uses hex color codes to set colors.                                       #
# Save this file in the same directory as GrainSizeTools                       #
# ============================================================================ #

# imports
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler

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
def freq_plot(diameters, binList, xgrid, y_values, y_max, x_peak, mean_GS, median_GS, plot, gmean=None):
    """ Generate a frequency vs grain size plot"""

    fig, ax = plt.subplots()

    ax.hist(diameters,
            bins=binList,
            range=(0, diameters.max()),
            density=True,
            color='#80419d',
            edgecolor='#C59fd7',
            alpha=0.7)
    ax.plot([mean_GS, mean_GS], [0, y_max],
            linestyle='-',
            color='#2F4858',
            label='arith. mean',
            linewidth=2.5)
    ax.plot([median_GS, median_GS], [0, y_max],
            linestyle='--',
            color='#2F4858',
            label='median',
            linewidth=2.5)

    ax.set_ylabel('density', color='#252525')

    if plot == 'linear':
        ax.plot([gmean, gmean], [0, y_max],
                linestyle='-',
                color='#fec44f',
                label='geo. mean')
        ax.set_xlabel(r'apparent diameter ($\mu m$)', color='#252525')

    elif plot == 'log':
        ax.set_xlabel(r'apparent diameter $\log_e{(\mu m)}$', color='#252525')

    elif plot == 'log10':
        ax.set_xlabel(r'apparent diameter $\log_{10}{(\mu m)}$', color='#252525')

    elif plot == 'norm':
        ax.set_xlabel(r'normalized apparent diameter $\log_e{(\mu m)}$', color='#252525')

    elif plot == 'sqrt':
        ax.set_xlabel(r'Square root apparent diameter ($\sqrt{\mu m}$)', color='#252525')

    ax.plot(xgrid, y_values,
            color='#2F4858')

    ax.vlines(x_peak, 0, y_max,
              linestyle=':',
              color='#2F4858',
              label='kde peak',
              linewidth=2.5)

    ax.legend(loc='best', fontsize=16)
    ax.set_ylim(bottom=-0.001)

    fig.tight_layout()

    return plt.show()


def area_weighted_plot(intValues, cumulativeAreas, h, weightedMean):
    """ Generate the area-weighted frequency vs grain size plot"""

    # normalize the y-axis values to percentage of the total area
    totalArea = sum(cumulativeAreas)
    cumulativeAreasNorm = [(x / float(totalArea)) * 100 for x in cumulativeAreas]
    maxValue = max(cumulativeAreasNorm)

    fig, ax = plt.subplots()

    # figure aesthetics
    ax.bar(intValues, cumulativeAreasNorm, width=h,
           color='#55A868',
           edgecolor='#FEFFFF',
           align='edge')
    ax.plot([weightedMean, weightedMean], [0.0001, maxValue],
            linestyle='--',
            color='#1F1F1F',
            label='area weighted mean',
            linewidth=2)
    ax.set_ylabel('% of area fraction', fontsize=15)
    ax.set_xlabel(r'apparent diameter ($\mu m$)', fontsize=15)
    ax.legend(loc='best', fontsize=15)

    fig.tight_layout()

    return plt.show()


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


def qq_plot(theoretical_data, obs_data):
    """ Return a q-q plot"""

    min_val, max_val = theoretical_data.min(), theoretical_data.max()

    fig, ax = plt.subplots()

    ax.plot([min_val, max_val], [min_val, max_val], '-', color='#2F4858', label='perfect lognormal')
    ax.plot(theoretical_data, obs_data, 'o', color='C0', alpha=0.5)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.set_xlabel('theoretical', fontsize=16)
    ax.set_ylabel('observed', fontsize=16)
    ax.legend(loc='best', fontsize=15)

    fig.tight_layout()

    return fig, ax
