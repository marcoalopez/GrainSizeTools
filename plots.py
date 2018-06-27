# ============================================================================ #
#                                                                              #
#    This is part of the "GrainSizeTools Script"                               #
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
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#    See the License for the specific language governing permissions and       #
#    limitations under the License.                                            #
#                                                                              #
#    Version 2.0                                                               #
#    For details see: http://marcoalopez.github.io/GrainSizeTools/             #
#    download at https://github.com/marcoalopez/GrainSizeTools/releases        #
#                                                                              #
# ============================================================================ #

# ============================================================================ #
# Functions to generate the plots using the Python matplotlib library.         #
# It uses hex color codes to set colors.                                       #
# Save this file in the same directory as GrainSizeTools                       #
# ============================================================================ #

import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy import array, std
from tools import gen_xgrid, log_function

# Set the plot style. To see the different styles available in Matplotlib see:
# https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
mpl.style.use('ggplot')
mpl.rcParams['font.family'] = 'Verdana'
mpl.rcParams['xtick.labelsize'] = 11.
mpl.rcParams['ytick.labelsize'] = 11.


def freq_plot(diameters, binList, xgrid, y_values, y_max, x_peak, mean_GS, median_GS, plot):
    """ Generate a frequency vs grain size plot"""

    fig, ax = plt.subplots()

    ax.hist(diameters,
            bins=binList,
            range=(0, diameters.max()),
            density=True,
            color='#4C72B0',
            edgecolor='#F7FFFF',
            alpha=0.6)
    ax.plot([mean_GS, mean_GS], [0.0001, y_max],
            linestyle='-',
            color='#1F1F1F',
            label='mean',
            linewidth=2)
    ax.plot([median_GS, median_GS], [0.0001, y_max],
            linestyle='--',
            color='#1F1F1F',
            label='median',
            linewidth=2)
    ax.plot(xgrid, y_values,
            color='#2E5A95',
            linewidth=2)

    ax.set_ylabel('density',
                  fontsize=13)

    if plot == 'linear':
        ax.set_xlabel(r'apparent diameter ($\mu m$)',
                      fontsize=13)

    elif plot == 'log':
        ax.set_xlabel(r'apparent diameter $\log_e{(\mu m)}$',
                      fontsize=13)

    elif plot == 'log10':
        ax.set_xlabel(r'apparent diameter $\log_{10}{(\mu m)}$',
                      fontsize=13)

    elif plot == 'norm':
        ax.set_xlabel(r'normalized apparent diameter ($\mu m$)',
                      fontsize=13)

    elif plot == 'sqrt':
        ax.set_xlabel(r'Square root apparent diameter ($\sqrt{\mu m}$)',
                      fontsize=13)

    ax.plot([x_peak], [y_max],
            'o',
            color='#2E5A95',
            label='kde peak')
    ax.vlines(x_peak, 0.0001, y_max,
              linestyle=':',
              color='#1F1F1F',
              linewidth=2)
    ax.annotate('Gaussian KDE peak',
                xy=(x_peak, y_max),
                xytext=(+10, +30),
                label='peak')
    ax.legend(loc='upper right',
              fontsize=11)

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
    ax.set_ylabel('% of area fraction',
                  fontsize=13)
    ax.set_xlabel(r'apparent diameter ($\mu m$)',
                  fontsize=13)
    ax.legend(loc='upper right',
              fontsize=11)

    fig.tight_layout()

    return plt.show()


def Saltykov_plot(left_edges, freq3D, binsize, mid_points, cdf_norm):
    """ Generate two plots once the Saltykov method is applied:

    i)  a bar plot (ax1)
    ii) a volume-weighted cumulative frequency plot (ax2)
    """

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(13, 5))

    # frequency plot
    ax1.bar(left_edges, freq3D,
            width=binsize,
            color='#404040',
            edgecolor='#d9d9d9',
            align='edge')
    ax1.set_ylabel('density',
                   fontsize=13)
    ax1.set_xlabel(r'diameter ($\mu m$)',
                   fontsize=13)
    ax1.set_title('estimated 3D grain size distribution',
                  color='#1F1F1F',
                  fontsize=13.5,
                  y=1.02)

    # volume-weighted cumulative frequency curve
    ax2.set_ylim([-2, 105])
    ax2.plot(mid_points, cdf_norm,
             'o-',
             color='#ed4256',
             label='volume weighted CFD',
             linewidth=2)
    ax2.set_ylabel('cumulative volume (%)',
                   fontsize=13)
    ax2.set_xlabel(r'diameter ($\mu m$)',
                   fontsize=13)
    ax2.set_title('volume-weighted cumulative freq. distribution',
                  color='#1F1F1F',
                  fontsize=13.5,
                  y=1.02)

    fig.tight_layout()

    return plt.show()


def twostep_plot(diameters, mid_points, frequencies, optimal_params, sigma_err):
    """ Generate a plot with the best fitting lognormal distribution (two-step method)
    
    Call functions
    --------------
    - gen_xgrid (tools)
    - log_function (tools)
    """

    # Generate a mesh of x-values
    xgrid = gen_xgrid(diameters, 0.1, max(diameters))

    # Calculate the curve of the best fit
    best_fit = log_function(xgrid, optimal_params[0], optimal_params[1])

    # Estimate all the combinatorial posibilities for fit curves taking into account the uncertainties
    values = array([log_function(xgrid, optimal_params[0] + sigma_err[0], optimal_params[1] + sigma_err[1]),
                    log_function(xgrid, optimal_params[0] - sigma_err[0], optimal_params[1] - sigma_err[1]),
                    log_function(xgrid, optimal_params[0] + sigma_err[0], optimal_params[1] - sigma_err[1]),
                    log_function(xgrid, optimal_params[0] - sigma_err[0], optimal_params[1] + sigma_err[1])])

    # Estimate the standard deviation of the all values obtained
    fit_error = std(values, axis=0)

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

    ax.set_ylabel('freq. (per unit vol.)',
                  fontsize=13)
    ax.legend(loc='upper right',
              fontsize=11)
    ax.set_xlabel(r'diameter ($\mu m$)',
                  fontsize=13)

    fig.tight_layout()

    return plt.show()
