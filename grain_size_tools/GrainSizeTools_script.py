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
#    Version 2024.02.xx                                                        #
#    For details see: http://marcoalopez.github.io/GrainSizeTools/             #
#    download at https://github.com/marcoalopez/GrainSizeTools/releases        #
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
    print(f'Mean = {amean:0.2f} ± {err:0.2f}')
    print(f'Confidence set at {confidence * 100} %')
    print(f'Max / min = {high:0.2f} / {low:0.2f}')
    print(f'Coefficient of variation = ±{100 * err / amean:0.1f} %')

    return amean, err, (low, high)


def weighted_mean_and_se(means, standard_errors):
    """
    Calculate the weighted mean and standard error of averages
    using the Mantel-Haenszel method.

    Parameters
    ----------
    means : numpy.ndarray
        1-D array containing the averages.
    standard_errors : numpy.ndarray
        1-D array containing the standard errors associated
        with each average.

    Returns
    -------
    float
        The weighted mean of averages.
    float
        The standard error of the weighted mean.

    Raises
    ------
    ValueError
        If input arrays have different shapes.

    Notes
    -----
    The function uses the Mantel-Haenszel method to calculate
    the weighted mean, where each average is weighted by the
    inverse of its squared standard error. The standard error
    of the weighted mean is also calculated.
    """
    # Ensure the input arrays have the same shape
    if means.shape != standard_errors.shape:
        raise ValueError("Input arrays must have the same shape")

    # Calculate the weights based on the inverse of squared standard errors
    weights = 1 / standard_errors**2

    # Calculate the weighted mean
    weighted_mean = np.sum(means * weights) / np.sum(weights)

    # Calculate the standard error of the weighted mean
    se_weighted_mean = 1 / np.sqrt(np.sum(1 / standard_errors**2))

    return weighted_mean, se_weighted_mean


def summarize(data, avg=('amean', 'gmean', 'median', 'mode'), ci_level=0.95,
              bandwidth='silverman', precision=0.1):
    """ Estimate different grain size statistics. This includes different means,
    the median, the frequency peak grain size via KDE, the confidence intervals
    using different methods, and the distribution features.

    Parameters
    ----------
    data : array_like
        the size of the grains

    avg : string, tuple or list; optional
        the averages to be estimated

        | Types:
        | 'amean' - arithmetic mean
        | 'gmean' - geometric mean
        | 'median' - median
        | 'mode' - the kernel-based frequency peak of the distribution

    ci_level : scalar between 0 and 1; optional
        the certainty of the confidence interval (default = 0.95)

    bandwidth : string {'silverman' or 'scott'} or positive scalar; optional
        the method to estimate the bandwidth or a scalar directly defining the
        bandwidth. It uses the Silverman plug-in method by default.

    precision : positive scalar or None; optional
        the maximum precision expected for the "peak" kde-based estimator.
        Default is 0.1. Note that this is not related with the confidence
        intervals

    Call functions
    --------------
    - amean, gmean, median, and freq_peak (from averages)

    Examples
    --------
    >>> summarize(dataset['diameters'])
    >>> summarize(dataset['diameters'], ci_level=0.99)
    >>> summarize(np.log(dataset['diameters']), avg=('amean', 'median', 'mode'))

    Returns
    -------
    None
    """

    # remove missing and infinite values
    data = data[~np.isnan(data) & ~np.isinf(data)]

    # check for negative values and remove
    if data[data <= 0].size > 0:
        print('Warning: There were negative and/or zero values in your dataset!')
        data = data[data > 0]
        print('Negative/zero values were automatically removed')
        print('')

    # estimate Shapiro-Wilk test to check normality and lognormality
    # In Shapiro-Wilk tests, the chances of the null hypothesis being
    # rejected becomes larger for large sample sizes. We limit the
    # sample size to a maximum of 250
    if len(data) > 250:
        W, p_value = shapiro(np.random.choice(data, size=250))
        W2, p_value2 = shapiro(np.random.choice(np.log(data), size=250))
    else:
        W, p_value = shapiro(data)
        W2, p_value2 = shapiro(np.log(data))

    if 'amean' in avg:
        if p_value2 < 0.05:
            amean, __, ci, length = averages.amean(data, ci_level, method='ASTM')
        else:
            if len(data) > 99:
                amean, __, (low_ci, high_ci), length2 = averages.amean(data, ci_level, method='mCox')
            else:
                amean, __, (low_ci, high_ci), length2 = averages.amean(data, ci_level, method='GCI')

            # estimate coefficients of variation
            lower_cvar = 100 * (amean - low_ci) / amean
            upper_cvar = 100 * (high_ci - amean) / amean

        print(' ')
        print('============================================================================')
        print('CENTRAL TENDENCY ESTIMATORS')
        print('============================================================================')
        print(f'Arithmetic mean = {amean:0.2f} microns')
        print(f'Confidence intervals at {ci_level * 100:0.1f} %')
        if p_value2 < 0.05:
            print(f'CLT (ASTM) method: {ci[0]:0.2f} - {ci[1]:0.2f}, (±{100 * (ci[1] - amean) / amean:0.1f}%), length = {length:0.3f}')
        else:
            if len(data) > 99:
                print(f'mCox method: {low_ci:0.2f} - {high_ci:0.2f} (-{lower_cvar:0.1f}%, +{upper_cvar:0.1f}%), length = {length2:0.3f}')
            else:
                print(f'GCI method: {low_ci:0.2f} - {high_ci:0.2f} (-{lower_cvar:0.1f}%, +{upper_cvar:0.1f}%), length = {length2:0.3f}')

    if 'gmean' in avg:
        m = 'CLT' if len(data) > 99 else 'bayes'  # choose optimal method to estimate confidence intervals
        gmean, msd, (low_ci, high_ci), length = averages.gmean(data, ci_level, method=m)

        # estimate coefficients of variation
        lower_cvar = 100 * (gmean - low_ci) / gmean
        upper_cvar = 100 * (high_ci - gmean) / gmean

        print('============================================================================')
        print(f'Geometric mean = {gmean:0.2f} microns')
        print(f'Confidence interval at {ci_level * 100:0.1f} %')
        print(f'{m} method: {low_ci:0.2f} - {high_ci:0.2f} (-{lower_cvar:0.1f}%, +{upper_cvar:0.1f}%), length = {length:0.3f}')

    if 'median' in avg:
        median, iqr, (low_ci, high_ci), length = averages.median(data, ci_level)

        # estimate coefficients of variation
        lower_cvar = 100 * (median - low_ci) / median
        upper_cvar = 100 * (high_ci - median) / median

        print('============================================================================')
        print(f'Median = {median:0.2f} microns')
        print(f'Confidence interval at {ci_level * 100:0.1f} %')
        print(f'robust method: {low_ci:0.2f} - {high_ci:0.2f} (-{lower_cvar:0.1f}%, +{upper_cvar:0.1f}%), length = {length:0.3f}')

    if 'mode' in avg:
        _, mode, _, bw = averages.freq_peak(data, bandwidth, precision)

        print('============================================================================')
        print(f'Mode (KDE-based) = {mode:0.2f} microns')
        print(f'Maximum precision set to {precision}')

        if type(bandwidth) is str:
            print(f'KDE bandwidth = {bw} ({bandwidth} rule)')
        else:
            print(f'KDE bandwidth = {bandwidth}')

    print(' ')
    print('============================================================================')
    print('DISTRIBUTION FEATURES')
    print('============================================================================')
    print(f'Sample size (n) = {len(data)}')
    print(f'Standard deviation = {np.std(data):0.2f} (1-sigma)')
    if 'median' in avg:
        print(f'Interquartile range (IQR) = {iqr:0.2f}')
    if 'gmean' in avg:
        print(f'Lognormal shape (Multiplicative Standard Deviation) = {msd:0.2f}')
    print('============================================================================')
    print('Shapiro-Wilk test warnings:')
    if p_value < 0.05:
        print('Data is not normally distributed!')
        print(f'Normality test: {W:0.2f}, {p_value:0.2f} (test statistic, p-value)')
    if p_value2 < 0.05:
        print('Data is not lognormally distributed!')
        print(f'Lognormality test: {W2:0.2f}, {p_value2:0.2f} (test statistic, p-value)')
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
    grain_size : positive scalar or array-like
        the apparent grain size in microns

    phase : string {'quartz', 'olivine', 'calcite', or 'feldspar'}
        the mineral phase

    piezometer : string
        the piezometric relation

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

    else:
        diff_stress = B * grain_size**-m
        if correction is True:
            diff_stress = diff_stress * 2 / np.sqrt(3)

    print('============================================================================')
    if isinstance(diff_stress, (int, float)):
        print(f'differential stress = {diff_stress:0.2f} MPa')
        print('')
        print('INFO:')
        print(warn)
        if linear_interceps is True:
            print('ECD was converted to linear intercepts using de Hoff and Rhines (1968) correction')
        print('============================================================================')
        return None
    else:
        print('INFO:')
        print(warn)
        if linear_interceps is True:
            print('ECD was converted to linear intercepts using de Hoff and Rhines (1968) correction')
        print('Differential stresses in MPa')

        return np.around(diff_stress, 2)


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
