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


import numpy as np
import plots as plots


def areaweighted(areas, diameters, binsize):
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
        the sectional areas of the grains

    diameters: array_like
        the equivalent circular diameters of the grains

    binsize: a string (plug-in methods) or scalar
        the bin size
    """

    # calculate the area weighted arithmetic mean
    area_total = np.sum(areas)
    weighted_areas = areas / area_total
    weigted_diameters = diameters * weighted_areas
    weighted_mean = np.sum(weigted_diameters)

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
    print('Area-weighted mean grain size = {:0.2f} microns' .format(weighted_mean))
    print(' ')
    print('HISTOGRAM FEATURES')
    print('The modal interval is {left:0.2f} - {right:0.2f} microns' .format(left=bin_edges[getIndex],
                                                                             right=bin_edges[getIndex] + h))
    print('Midpoint (of modal interval) = {:0.2f} microns' .format(bin_edges[getIndex] + (bin_edges[getIndex] + h) / 2.0))
    print('The number of classes are {}' .format(len(histogram)))
    if type(binsize) is str:
        print('The bin size is {bin:0.2f} according to the {rule} rule' .format(bin=h, rule=binsize))
    print(' ')

    return plots.area_weighted_plot(bin_edges, cumulativeAreas, h, weighted_mean)



def get_filepath():
    """ Get a file path through a file selection dialog."""

    try:
        import os
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        file_path = tk.filedialog.askopenfilename(initialdir=os.getcwd(),
                                                  title="Select file",
                                                  filetypes=[('Text files', '*.txt'),
                                                             ('Text files', '*.csv'),
                                                             ('Excel files', '*.xlsx')])
    except ImportError:
        print('Requires Python 3.6+')

    return file_path


def normalized(diameters, binsize, bandwidth):
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
