# Quantifying grain size populations using GrainSizeTools Script

TODO

> [!CAUTION]
> Please, if you get errors in the documentation open an issue and let us know. Make sure you are using the latest version of the script before reporting them.



## 1. How to import datasets



## 2. Statistical description of grain size populations

Let's first create a lognormal population using the function ``gen_lognorm_population()`` with a known shape and average to see how a population of grain sizes can be described statistically.

```python
toy_dataset = averages.gen_lognorm_population(scale=np.log(20),   # geomean to 20
                                              shape=np.log(1.5),  # lognormal shape =1.5
                                              n=500,              # sample size = 500
                                              seed=2)

plt.hist(toy_dataset, bins='fd')
```

![](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/lognorm_pop_random.png)

We then use the ``summarize()`` function to describe the population statistically.

```python
summarize(toy_dataset)
```

```reStructuredText
============================================================================
CENTRAL TENDENCY ESTIMATORS
============================================================================
Arithmetic mean = 21.33 microns
Confidence intervals at 95.0 %
mCox method: 20.51 - 22.11 (-3.8%, +3.7%), length = 1.601
============================================================================
Geometric mean = 19.57 microns
Confidence interval at 95.0 %
CLT method: 18.88 - 20.29 (-3.5%, +3.7%), length = 1.413
============================================================================
Median = 19.42 microns
Confidence interval at 95.0 %
robust method: 18.47 - 20.78 (-4.9%, +7.0%), length = 2.312
============================================================================
Mode (KDE-based) = 15.95 microns
Maximum precision set to 0.1
KDE bandwidth = 2.88 (silverman rule)
 
============================================================================
DISTRIBUTION FEATURES
============================================================================
Sample size (n) = 500
Standard deviation = 9.42 (1-sigma)
Interquartile range (IQR) = 11.42
Lognormal shape (Multiplicative Standard Deviation) = 1.51
============================================================================
Shapiro-Wilk test warnings:
Data is not normally distributed!
Normality test: 0.88, 0.00 (test statistic, p-value)
============================================================================
```

By default, the ```summarize()``` function returns:

- Different **central tendency estimators** ("averages") including the arithmetic and geometric means, the median, and the mode (i.e. frequency peak) based on the kernel density estimate method.

- The **confidence intervals** for the different means and the median at 95% of certainty in absolute value and percentage relative to the average (*a.k.a* coefficient of variation). The meaning of these intervals is that, given the observed data, there is a 95% probability (one in 20) that the true value of grain size falls within this credible interval. The function provides the lower and upper bounds of the confidence interval, the error in percentage respect to the average, and the interval length. 

- The methods used (e.g. mCox, CLT, robust, etc) to estimate the confidence intervals for each average excepting for the mode. The function ```summarize()``` automatically choose the optimal method depending on distribution features (see below)

- The sample size and two population dispersion measures: the Bessel corrected [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) and the [interquartile range](https://en.wikipedia.org/wiki/Interquartile_range).

- The shape of the lognormal distribution using the multiplicative standard deviation (MSD)

- A Shapiro-Wilk test warning indicating when the data deviates from normal and/or lognormal (when p-value < 0.05).

In the example above, the Shapiro-Wilk test tells us that the distribution is not normally distributed, which is to be expected since we know that this is a lognormal distribution. Note that the geometric mean and the lognormal shape are very close to the values used to generate the synthetic random dataset, 20 and 1.5 respectively.



![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/avg_map.png?raw=true)



> [!IMPORTANT]
> ### Choosing the Appropriate Measure of Central Tendency
> The choice of the measure of central tendency, often referred to as the “average,” depends on your specific goals and dataset. Here are some guidelines based on [Lopez-Sanchez (2020)](https://doi.org/10.1016/j.jsg.2020.104042):
> - **Geometric Mean**: This average is recommended for populations that follow a lognormal distribution. It shows superior performance across varying degrees of asymmetry and sample sizes.
> - **Median**: This is the preferable average when dealing with data contamination, such as outliers or few (<10%) observations from mixed distributions.
> - **Arithmetic Mean**: This is the most backwards-compatible average due to its common use in the past. Theoretically, it outperforms the median in low to moderately skewed distributions (MSD < 1.7) as long as the presence of extreme values (outliers) is limited. However, estimating error margins for the arithmetic mean can be problematic in real samples with asymmetric distributions, making the geometric mean or median preferable in such cases.
> - **Mode (KDE based)**: Although generally less effective than other measures of central tendency, this mode remains robust in situations common to grain size studies. It can be useful when comparing different data sets with significant differences in resolution limits and size cut-offs. In such cases it is the only meaningful measure of central tendency when comparing different data sets. The script calculates the mode (peak frequency) using the Kernel Density Estimate (KDE) technique, which is far superior to modes calculated from the histogram.
> - **Root mean squared (RMS) or Area-weighted mean:** Avoid them, as they tend to perform poorly and are not recommended for grain size studies.
>
> **TLDR**: With asymmetric distributions you should be probably using the median (plus the interquartile range) or the geometric mean, not the arithmetic mean. 



## 3. Representation of grain size populations

TODO



![linear_distribution](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/new_distribution.png)

> [!IMPORTANT]
> Key information users need to know to achieve their goal.



### 3.x Testing lognormality or normality

TODO

![qqplot](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/new_qqplot.png)



> [!TIP]
> To know more about the q-q plot see https://serialmentor.com/dataviz/



### 3.x The area-weighted distribution

TODO

![area_weighted](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/new_area_weighted.png)



> [!IMPORTANT]
> _**When to use and not to use the area-weighted approach?**_
> You **should not use** the area-weighted mean for the calibration of paleopiezometers or for the comparison of grain size populations, as this is a poorly optimised central tendency measure ([Lopez-Sanchez, 2020](https://doi.org/10.1016/j.jsg.2020.104042)). On the other hand, the area-weighted distribution is useful to visualize the coarser size range, since in number-weighted distributions these sizes are diluted but can represent a significant area or volume.


### 3.3 Normalized grain size distributions

TODO

![normalized](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/new_normalized.png)

### 3.x. Saving your figures

TODO



## 4. Comparing different grain size populations

TODO