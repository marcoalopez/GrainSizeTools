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
#    Version 3.2.0                                                             #
#    For details see: http://marcoalopez.github.io/GrainSizeTools/             #
#    download at https://github.com/marcoalopez/GrainSizeTools/releases        #
#                                                                              #
# ============================================================================ #

# import neccesary Python scientific modules
import numpy as np
from scipy.stats import shapiro


def summarize(
    data,
    avg=("amean", "gmean", "median", "mode"),
    ci_level=0.95,
    bandwidth="silverman",
    precision=0.1,
):
    """Estimate different grain size statistics. This includes different means,
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
        | 'mode' - the kde-based frequency peak of the distribution

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
                                                          ('Text files', '*.tsv'),
                                                          ('Text files', '*.csv'),
                                                          ('Excel files', '*.xlsx')])
    except ImportError:
        print('Requires Python 3.6+')

    return file_path


welcome = """
======================================================================================
Welcome to GrainSizeTools script
======================================================================================
A free open-source cross-platform script to visualize and characterize grain size
population and estimate differential stress via paleopizometers.

Version: 3.2.0
Documentation: https://github.com/marcoalopez/GrainSizeTools/wiki

Type function_list() to get a list of the main methods
"""

info = """
======================================================================================
List of main functions
======================================================================================
summarize              -> get the properties of the data population
conf_interval          -> estimate a robust confidence interval using the t-distribution
calc_diffstress        -> estimate diff. stress from grain size using piezometers

plot.distribution      -> visualize the distribution of grain sizes and locate the averages
plot.qq_plot           -> test the lognormality of the dataset (q-q plot + Shapiro-Wilk test)
plot.area_weighted     -> visualize the area-weighed distribution of grain sizes
plot.normalized        -> visualize a normalized distribution of grain sizes

stereology.Saltykov    -> approximate the actual grain size distribution via the Saltykov method
stereology.two_step    -> approximate the lognormal distribution to the actual distribution
======================================================================================

You can get more information about the methods using the following ways:
    (1) Typing ? or ?? after the function name, e.g. summarize?
    (2) Typing help plus the name of the function, e.g. help(summarize)
    (3) In JupyterLab by enabling the "Show contextual help"
"""

def function_list():
    print(info)
    return None


if __name__ == "__main__":
    print(welcome)
    # import grain_size_tools modules
    import plot
    import averages
    import stereology
    import template
