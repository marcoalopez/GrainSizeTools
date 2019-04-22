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
# Set the plot style. To see the different styles available in Matplotlib see:
# https://matplotlib.org/gallery/style_sheets/style_sheets_reference.html
mpl.style.use('ggplot')
mpl.rcParams['font.family'] = 'Verdana'
mpl.rcParams['xtick.labelsize'] = 15.
mpl.rcParams['ytick.labelsize'] = 15.


def freq_plot(diameters, binList, xgrid, y_values, y_max, x_peak, mean_GS, median_GS, plot, gmean=None):
    """ Generate a frequency vs grain size plot"""

    fig, ax = plt.subplots()

    ax.hist(diameters,
            bins=binList,
            range=(0, diameters.max()),
            density=True,
            color='#4C72B0',
            edgecolor='#F7FFFF',
            alpha=0.7)
    ax.plot([mean_GS, mean_GS], [0.0001, y_max],
            linestyle='-',
            color='#252525',
            label='mean',
            linewidth=2)
    ax.plot([median_GS, median_GS], [0.0001, y_max],
            linestyle='--',
            color='#252525',
            label='median',
            linewidth=2)

    ax.set_ylabel('density',
                  fontsize=15)

    if plot == 'linear':
        ax.plot([gmean, gmean], [0.0001, y_max],
                linestyle='-',
                color='C0',
                label='geo. mean',
                linewidth=2)
        ax.set_xlabel(r'apparent diameter ($\mu m$)',
                      fontsize=15)

    elif plot == 'log':
        ax.set_xlabel(r'apparent diameter $\log_e{(\mu m)}$',
                      fontsize=15)

    elif plot == 'log10':
        ax.set_xlabel(r'apparent diameter $\log_{10}{(\mu m)}$',
                      fontsize=15)

    elif plot == 'norm':
        ax.set_xlabel(r'normalized apparent diameter $\log_e{(\mu m)}$',
                      fontsize=15)

    elif plot == 'sqrt':
        ax.set_xlabel(r'Square root apparent diameter ($\sqrt{\mu m}$)',
                      fontsize=15)

    ax.plot(xgrid, y_values,
            color='#2E5A95',
            linewidth=2.5)
    ax.plot([x_peak], [y_max],
            'o',
            color='#2E5A95')
    ax.vlines(x_peak, 0.0001, y_max,
              linestyle=':',
              color='#252525',
              linewidth=2,
              label='kde peak')

    ax.legend(loc='best', fontsize=15)

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

    ax.plot(mid_points, frequencies,  # datapoints used for the fitting procedure
            'o',
            color='#d53e4f',
            label='datapoints',
            linewidth=1.5)

    ax.set_ylabel('freq. (per unit vol.)', fontsize=15)
    ax.legend(loc='best', fontsize=15)
    ax.set_xlabel(r'diameter ($\mu m$)', fontsize=15)

    fig.tight_layout()

    return plt.show()


def qq_plot(theoretical_data, obs_data):
    """ Return a q-q plot"""

    min_val, max_val = theoretical_data.min(), theoretical_data.max()

    fig, ax = plt.subplots()

    ax.plot([min_val, max_val], [min_val, max_val], '-', color='C3', linewidth=2, label='perfect lognormal')
    ax.plot(theoretical_data, obs_data, 'o', color='C0')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.set_xlabel('theoretical', fontsize=16)
    ax.set_ylabel('observed', fontsize=16)
    ax.legend(loc='best', fontsize=15)

    fig.tight_layout()

    return fig, ax
