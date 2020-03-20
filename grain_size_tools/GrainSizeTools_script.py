# ============================================================================ #
#                                                                              #
#    GrainSizeTools Script                                                     #
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
#    Requirements:                                                             #
#        Python     v3.6 or higher                                             #
#        Numpy      v1.11 or higher                                            #
#        Matplotlib v2.0 or higher                                             #
#        Scipy      v1.0 or higher                                             #
#        Pandas     v0.16 or higher                                            #
#                                                                              #
# ============================================================================ #

# import grain_size_tools modules
import plot
import averages
import stereology
import piezometers
import template
import get

# import neccesary Python scientific modules
import numpy as np
import pandas as pd
from scipy.stats import sem, t, shapiro


def conf_interval(data, confidence=0.95):
    """Estimate the confidence interval using the t-distribution with n-1
    degrees of freedom t(n-1). This is the way to go when sample size is
    small (n < 30) and the standard deviation cannot be estimated accurately.
    For large datasets, the t-distribution approaches the normal distribution.

    Parameters
    ----------
    data : array-like
        the dataset

    confidence : float between 0 and 1, optional
        the confidence interval, default = 0.95

    Assumptions
    -----------
    the data follows a normal or symmetric distrubution (when sample size
    is large)

    call_function(s)
    ----------------
    Scipy's t.interval

    Returns
    -------
    the arithmetic mean, the error, and the limits of the confidence interval
    """

    dof = len(data) - 1
    amean = np.mean(data)
    std_err = sem(data)  # Standard error of the mean SD / sqrt(n)
    low, high = t.interval(confidence, dof, amean, std_err)
    err = high - amean

    print(' ')
    print('Confidence set at {} %' .format(confidence * 100))
    print('Mean = {mean:0.2f} ± {err:0.2f}' .format(mean=amean, err=err))
    print('Max / min = {max:0.2f} / {min:0.2f}' .format(max=high, min=low))
    print('Coefficient of variation = {:0.1f} %' .format(100 * err / amean))

    return amean, err, (low, high)


def summarize(data, avg=('amean', 'gmean', 'median', 'mode'), ci_level=0.95,
              bandwidth='silverman', precision=0.1):
    """ Estimate different grain size statistics. This includes different means,
    the median, the frequency peak grain size via KDE, the confidence intervals
    using different methods, and the distribution features.

    Parameters
    ----------
    data : array_like
        the diameters (apparent or not) of the grains

    avg : string, tuple or list. Optional
        the averages to be estimated

        | Types:
        | 'amean' - arithmetic mean
        | 'gmean' - geometric mean
        | 'median' - median
        | 'mode' - the kernel-based frequency peak of the distribution

    ci_level : scalar between 0 and 1, optional
        the certainty of the confidence interval (default = 0.95)

    bandwidth : string {'silverman' or 'scott'} or positive scalar, optional
        the method to estimate the bandwidth or a scalar directly defining the
        bandwidth. It uses the Silverman plug-in method by default.

    precision : positive scalar or None, optional
        the maximum precision expected for the "peak" kde-based estimator.
        Default is None

    Call functions
    --------------
    - amean, gmean, median, and freq_peak (from averages)

    Examples
    --------
    >>> summarize(dataset['diameters'])
    >>> summarize(dataset['diameters'], ci_level=0.99)
    >>> summarize(dataset['diameters'], ci_method='GCI')
    >>> summarize(np.log(dataset['diameters']), avg=('amean', 'median', 'mode'))

    Returns
    -------
    TODO
    """

    # check and remove for negative values
    if data[data < 0].size > 0:
        print('Warning: I found negative and/or zero values in your dataset!')
        data = data[data > 0]
        print('Negative/zero values automatically removed')
        print('')

    std = np.std(data)

    if 'amean' in avg:
        amean, __, ci, length = averages.amean(data, ci_level, method='ASTM')
        if len(data) > 99:
            __, __, (low_ci, high_ci), length2 = averages.amean(data, ci_level, method='mCox')
        else:
            __, __, (low_ci, high_ci), length2 = averages.amean(data, ci_level, method='GCI')

        # estimate coefficients of variation
        lower_cvar = 100 * (amean - low_ci) / amean
        upper_cvar = 100 * (high_ci - amean) / amean

        print(' ')
        print('============================================================================')
        print('CENTRAL TENDENCY ESTIMATORS')
        print('============================================================================')
        print('Arithmetic mean = {:0.2f} microns' .format(amean))
        print('Confidence intervals at {:0.1f} %' .format(ci_level * 100))
        print('ASTM method: {:0.2f} - {:0.2f}, (±{:0.1f}%), length = {:0.3f}'
              .format(ci[0], ci[1], 100 * (ci[1] - amean) / amean, length))
        if len(data) > 99:
            print('mCox method: {:0.2f} - {:0.2f} (-{:0.1f}%, +{:0.1f}%), length = {:0.3f}'
                  .format(low_ci, high_ci, lower_cvar, upper_cvar, length2))
        else:
            print('GCI method: {:0.2f} - {:0.2f} (-{:0.1f}%, +{:0.1f}%), length = {:0.3f}'
                  .format(low_ci, high_ci, lower_cvar, upper_cvar, length2))

    if 'gmean' in avg:
        m = 'CLT' if len(data) > 99 else 'bayes'  # choose optimal method to estimate confidence intervals
        gmean, msd, (low_ci, high_ci), length = averages.gmean(data, ci_level, method=m)

        # estimate coefficients of variation
        lower_cvar = 100 * (gmean - low_ci) / gmean
        upper_cvar = 100 * (high_ci - gmean) / gmean

        print('============================================================================')
        print('Geometric mean = {:0.2f} microns' .format(gmean))
        print('Confidence interval at {:0.1f} %' .format(ci_level * 100))
        print('{} method: {:0.2f} - {:0.2f} (-{:0.1f}%, +{:0.1f}%), length = {:0.3f}'
              .format(m, low_ci, high_ci, lower_cvar, upper_cvar, length))

    if 'median' in avg:
        median, iqr, (low_ci, high_ci), length = averages.median(data, ci_level)

        # estimate coefficients of variation
        lower_cvar = 100 * (median - low_ci) / median
        upper_cvar = 100 * (high_ci - median) / median

        print('============================================================================')
        print('Median = {:0.2f} microns' .format(median))
        print('Confidence interval at {:0.1f} %' .format(ci_level * 100))
        print('robust method: {:0.2f} - {:0.2f} (-{:0.1f}%, +{:0.1f}%), length = {:0.3f}'
              .format(low_ci, high_ci, lower_cvar, upper_cvar, length))

    if 'mode' in avg:
        __, mode, __, bw = averages.freq_peak(data, bandwidth, precision)

        print('============================================================================')
        print('Mode (KDE-based) = {:0.2f} microns' .format(mode))
        print('Maximum precision set to', precision)

        if type(bandwidth) is str:
            print('KDE bandwidth = {} ({} rule)' .format(bw, bandwidth))
        else:
            print('KDE bandwidth =', bandwidth)

    # estimate Shapiro-Wilk test to check normality and lognormality
    W, p_value = shapiro(data)
    W2, p_value2 = shapiro(np.log(data))

    print(' ')
    print('============================================================================')
    print('DISTRIBUTION FEATURES')
    print('============================================================================')
    print('Standard deviation = {:0.2f} (1-sigma)' .format(std))
    if 'median' in avg:
        print('Interquartile range (IQR) = {:0.2f}' .format(iqr))
    if 'gmean' in avg:
        print('Lognormal shape (Multiplicative Standard Deviation) = {:0.2f}' .format(msd))
    print('============================================================================')
    print('Shapiro-Wilk test warnings:')
    if p_value < 0.05:
        print('Data is not normally distributed!')
        print('Normality test: {:0.2f}, {:0.2f} (test statistic, p-value)' .format(W, p_value))
    if p_value2 < 0.05:
        print('Data is not lognormally distributed!')
        print('Lognormality test: {:0.2f}, {:0.2f} (test statistic, p-value)' .format(W2, p_value2))
    print('============================================================================')

    return None


def calc_diffstress(grain_size, phase, piezometer, correction=False):
    """ Apply different piezometric relations to estimate the differential
    stress from average apparent grain sizes. The piezometric relation has
    the following general form:

    df = B * grain_size**-m

    where df is the differential stress in [MPa], B is an experimentally
    derived parameter in [MPa micron**m], grain_size is the aparent grain
    size in [microns], and m is an experimentally derived exponent.

    Parameters
    ----------
    grain_size : positive scalar
        the apparent grain size in microns

    phase : string {'quartz', 'olivine', 'calcite', or 'feldspar'}
        the mineral phase

    piezometer : string
        the piezometric relation to be use

    correction : bool, default False
        correct the stress values for plane stress (Paterson and Olgaard, 2000)

     References
    -----------
    Paterson and Olgaard (2000) https://doi.org/10.1016/S0191-8141(00)00042-0
    de Hoff and Rhines (1968) Quantitative Microscopy. Mcgraw-Hill. New York.

    Call functions
    --------------
    piezometers.quartz
    piezometers.olivine
    piezometers.calcite
    piezometers.albite

    Assumptions
    -----------
    - Independence of temperature (excepting Shimizu piezometer), total strain,
    flow stress, and water content.
    - Recrystallized grains are equidimensional or close to equidimensional when
    using a single section.
    - The piezometer relations requires entering the grain size as "average"
    apparent grain size values calculated using equivalent circular diameters
    (ECD) with no stereological correction. See documentation for more details.
    - When required, the grain size value will be converted from ECD to linear
    intercept (LI) using a correction factor based on de Hoff and Rhines (1968):
    LI = (correction factor / sqrt(4/pi)) * ECD
    - Stress estimates can be corrected from uniaxial compression (experiments)
    to plane strain (nature) multiplying the paleopiezometer by 2/sqrt(3)
    (Paterson and Olgaard, 2000)

    Returns
    -------
    The differential stress in MPa (a float)
    """

    if phase == 'quartz':
        B, m, warn, linear_interceps, correction_factor = piezometers.quartz(piezometer)
    elif phase == 'olivine':
        B, m, warn, linear_interceps, correction_factor = piezometers.olivine(piezometer)
    elif phase == 'calcite':
        B, m, warn, linear_interceps, correction_factor = piezometers.calcite(piezometer)
    elif phase == 'feldspar':
        B, m, warn, linear_interceps, correction_factor = piezometers.feldspar(piezometer)
    else:
        raise ValueError('Phase name misspelled. Please choose between valid mineral names')

    # Special cases (convert from ECD to linear intercepts)
    if linear_interceps is True:
        grain_size = (correction_factor / (np.sqrt(4 / np.pi))) * grain_size

    # Estimate differential stress
    if piezometer == 'Shimizu':
        T = float(input("Please, enter the temperature [in C degrees] during deformation: "))
        diff_stress = B * grain_size**(-m) * np.exp(698 / (T + 273.15))
        if correction is True:
            diff_stress = diff_stress * 2 / np.sqrt(3)
        print(' ')
        print('differential stress = {:0.2f} MPa' .format(diff_stress))
        print(warn)
    else:
        diff_stress = B * grain_size**-m
        if correction is True:
            diff_stress = diff_stress * 2 / np.sqrt(3)
        print(' ')
        print('differential stress = {:0.2f} MPa' .format(diff_stress))
        print(warn)
        print(' ')

    return None


def get_filepath():
    """ Get a file path through a file selection dialog."""

    try:
        import os
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
        print('Requires Python 3.6+')

    return file_path


if float(np.__version__[0:4]) < 1.11:
    print('The installed Numpy version', np.__version__, 'is too old.')
    print('Please upgrade to v1.11 or higher')
