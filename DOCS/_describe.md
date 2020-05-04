# Describing the population of grain sizes

The method to describe the properties of the grain size population is named ``summarize()``. Before we get into the details of the method, let's run the GrainSizeTools script, load the example dataset, and create a toy dataset with known parameters.

```python
# Load the example dataset
filepath = 'C:/Users/marco/Documents/GitHub/GrainSizeTools/grain_size_tools/DATA/data_set.txt'
dataset = pd.read_csv(filepath, sep='\t')

# estimate equivalent circular diameters (ECDs)
dataset['diameters'] = 2 * np.sqrt(dataset['Area'] / np.pi)
dataset.head()
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/dataframe_output_newcol.png?raw=true)

```python
# Set the population properties for the toy dataset
scale = np.log(20)  # set sample geometric mean to 20
shape = np.log(1.5)  # set the lognormal shape to 1.5

# generate a random lognormal population of size 500
np.random.seed(seed=1)  # this is for reproducibility
toy_dataset = np.random.lognormal(mean=scale, sigma=shape, size=500)
```

We are now ready to check what we can get from the function `summarize()`. The simplest example of use would be to pass the data containing the diameters. For simplicity's sake, let's do it with the toy dataset first.

```python
summarize(toy_dataset)
```

```
============================================================================
CENTRAL TENDENCY ESTIMATORS
============================================================================
Arithmetic mean = 22.13 microns
Confidence intervals at 95.0 %
mCox method: 21.35 - 22.98 (-3.5%, +3.8%), length = 1.623
============================================================================
Geometric mean = 20.44 microns
Confidence interval at 95.0 %
CLT method: 19.73 - 21.17 (-3.5%, +3.6%), length = 1.441
============================================================================
Median = 20.32 microns
Confidence interval at 95.0 %
robust method: 19.33 - 21.42 (-4.9%, +5.4%), length = 2.096
============================================================================
Mode (KDE-based) = 17.66 microns
Maximum precision set to 0.1
KDE bandwidth = 2.78 (silverman rule)
 
============================================================================
DISTRIBUTION FEATURES
============================================================================
Sample size (n) = 500
Standard deviation = 9.07 (1-sigma)
Interquartile range (IQR) = 11.44
Lognormal shape (Multiplicative Standard Deviation) = 1.49
============================================================================
Shapiro-Wilk test warnings:
Data is not normally distributed!
Normality test: 0.88, 0.00 (test statistic, p-value)
============================================================================
```

By default, the `summarize()` function returns:

- Different **central tendency estimators** ("averages") including the arithmetic and geometric means, the median, and the KDE-based mode (i.e. frequency peak).
- The **confidence intervals** for the different means and the median at 95% of certainty in absolute value and percentage relative to the average (*a.k.a* coefficient of variation). The meaning of these intervals is that, given the observed data, there is a 95% probability (one in 20) that the true value of grain size falls within this credible interval. The function provides the lower and upper bounds of the confidence interval, the error in percentage respect to the average, and the interval length.
- The methods used to estimate the confidence intervals for each average (excepting for the mode). The function `summarize()` automatically choose the optimal method depending on distribution features (see below)
- The sample size and two population dispersion measures: the (Bessel corrected) [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) and the [interquartile range](https://en.wikipedia.org/wiki/Interquartile_range).
- The shape of the lognormal distribution using the multiplicative standard deviation (MSD)
- A Shapiro-Wilk test warning indicating when the data deviates from normal and/or lognormal (when p-value < 0.05).

In the example above, the Shapiro-Wilk test tells us that the distribution is not normally distributed, which is to be expected since we know that this is a lognormal distribution. Note that the geometric mean and the lognormal shape are very close to the values used to generate the synthetic random dataset, 20 and 1.5 respectively. Now, let's do the same using the dataset that comes from a real rock, for this, we have to pass the column with the diameters:

```python
summarize(dataset['diameters'])
```

```
============================================================================
CENTRAL TENDENCY ESTIMATORS
============================================================================
Arithmetic mean = 34.79 microns
Confidence intervals at 95.0 %
CLT (ASTM) method: 34.09 - 35.48, (±2.0%), length = 1.393
============================================================================
Geometric mean = 30.10 microns
Confidence interval at 95.0 %
CLT method: 29.47 - 30.75 (-2.1%, +2.2%), length = 1.283
============================================================================
Median = 31.53 microns
Confidence interval at 95.0 %
robust method: 30.84 - 32.81 (-2.2%, +4.1%), length = 1.970
============================================================================
Mode (KDE-based) = 24.31 microns
Maximum precision set to 0.1
KDE bandwidth = 4.01 (silverman rule)
 
============================================================================
DISTRIBUTION FEATURES
============================================================================
Sample size (n) = 2661
Standard deviation = 18.32 (1-sigma)
Interquartile range (IQR) = 23.98
Lognormal shape (Multiplicative Standard Deviation) = 1.75
============================================================================
Shapiro-Wilk test warnings:
Data is not normally distributed!
Normality test: 0.94, 0.00 (test statistic, p-value)
Data is not lognormally distributed!
Lognormality test: 0.99, 0.03 (test statistic, p-value)
============================================================================
```

Leaving aside the different numbers, there are some subtle differences compared to the results obtained with the toy dataset. First, the confidence interval method for the arithmetic mean is no longer the modified Cox (mCox) but the one based on the central limit theorem (CLT) advised by the [ASTM](https://en.wikipedia.org/wiki/ASTM_International). As previously noted, the function ```summarize()``` automatically choose the optimal confidence interval method depending on distribution features. We show below the decision tree flowchart for choosing the optimal confidence interval estimation method, which is based on [Lopez-Sanchez (2020)](https://doi.org/10.1016/j.jsg.2020.104042).

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/avg_map.png?raw=true)

The reason why the CLT method applies in this case is that the grain size distribution not enough lognormal-like (note the Shapiro-Wilk test warning with a p-value < 0.05), and this might cause an inaccurate estimate of the arithmetic mean confidence interval.

Now, let's focus on the different options of the ``summarize()`` method.

```python
def summarize(data,
              avg=('amean', 'gmean', 'median', 'mode'),
              ci_level=0.95,
              bandwidth='silverman',
              precision=0.1):
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
```



> **TODO:**
- explain the different options of ``summarize()`` through examples
- examples using log-transformed populations
