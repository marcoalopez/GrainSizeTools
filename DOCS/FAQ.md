# Frequently Asked Questions

- [Who is this script for?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#who-is-this-script-for-)
- [What measure of central tendency (i.e. average) do I have to use?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#what-measure-of-central-tendency--ie-average--do-i-have-to-use-)
- [When to use the standard deviation and the confidence interval for the average?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#when-to-use-the-standard-deviation-and-the-confidence-interval-for-the-average-)
- [Why the grain size distribution plots produced by the GST script and the classic CSD charts do not use the same units on the y-axis?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#why-the-grain-size-distribution-plots-produced-by-the-gst-script-and-the-classic-csd-charts-do-not-use-the-same-units-on-the-y-axis-)
- [Why the sum of all frequencies in the histograms is not equal to one?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#why-the-sum-of-all-frequencies-in-the-histograms-is-not-equal-to-one-)
- [Specifying Script Version in Publications](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#specifying-script-version-in-publications)
- [Does the script work with Python 2.7.x?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#does-the-script-work-with-python-27x-)

## Who is this script for?
The script serves three primary goals:

- Promoting best practices and reproducibility in grain size analysis through robust statistics. It aims to avoid manual steps during data processing and advocates for standard procedures in grain size characterization.
- Maintaining a curated and up-to-date database of grain-size-based paleopiezometers for various mineral phases.
- Providing a platform for the implementation and testing of new methods  for grain size characterization in recrystallized materials

Specifically, this script is designed for individuals who:

- Want to visualize grain size distributions.

- Estimate the magnitude of differential stress in dynamically recrystallized rocks from apparent grain sizes.

- Aim to approximate the actual (3D) distribution of grain sizes from thin sections using stereological methods. This involves estimating the volume occupied by a particular grain size fraction and a parameter characterizing the shape of the grain size population (assuming a lognormal distribution). The stereological methods assume that grains have equant or near-equant shapes (AR < 2.0), which mostly include all recrystallized grains produced during static and dynamic recrystallization. Additional details are available [here](http://joss.theoj.org/papers/10.21105/joss.00863).

> For igneous studies involving tabular grains far from near-equant objects, we recommend other approaches such as those implemented in the *CSDCorrections* software (Higgins 2000). See the references list section for details.

## What measure of central tendency (i.e. average) do I have to use?

The choice of the measure depends on your specific goals and dataset. Here are some guidelines based on [Lopez-Sanchez (2020)](https://doi.org/10.1016/j.jsg.2020.104042):

- **Geometric mean:** This is recommended, especially for lognormal-like populations, showing superior performance across asymmetry and sample sizes.
- **Median:** Preferable when dealing with data contamination, such as outliers or observations from mixed distributions.
- **Arithmetic mean:** the most backwards-compatible average due to its common use in the past. Theoretically, it outperforms the median in low to moderately skewed distributions (MSD < 1.7) as long the presence of extreme values (outliers) is limited. However, the estimation of error margins for the arithmetic mean can be problematic in real samples, making the geometric mean or median preferable.
- **KDE-based mode:** Generally, this performs less effectively than other measures of central tendency. However, it remains robust in specific situations likely to occur in grain size studies, such as notable differences in resolution limits and size cut-offs. In these cases, it is the only useful measure of central tendency when comparing different sets of data.
- **Root mean squared (RMS) or Area-weighted mean:** Avoid them, both tend to perform poorly.

> For those aiming to use a specific piezometer, it is crucial to **use the same average used in the piezometric calibration**. If establishing a new calibration or summarizing the distribution, the provided guidelines can assist in selecting the most suitable measure. Additional details can be found [here](https://github.com/marcoalopez/marcoalopez.github.io/blob/master/docs/2020_JSG_SG_104042.pdf)

## When to use the standard deviation and the confidence interval for the average?

That depends on the information you want to provide. If the message is on the spread of the grain size population (e.g. to compare between different grain size distributions) the standard deviation or the interquartile range is the metric you want. If the interest is in the precision of the average or in comparing averages between different grain size populations the confidence interval is your metric (e.g., when using paleopiezometers). More precisely:

The **standard deviation** (s.d.) is the typical difference between each value and the mean value. So, in this case, it describes how broadly the grain size values are distributed within the sample. **Standard deviation describes a dataset**.

The **standard error of the mean** (s.e.m.) is an estimate of how variable the means will be if the experiment or measure is repeated multiple times. The s.e.m. may serve to check whether sets of samples are likely to come from the same or a similar population. **Standard error describes an estimate**.

The **95 % confidence interval** (C.I., 95%) means that the population mean will lie in this interval with 95% confidence. This metric is valuable when assessing the precision of the average or comparing averages between different grain size populations. It's like  saying, "We're 95% confident that the true average grain size falls  within this range." In simpler terms, it gives you a sense of how certain you can be about the average, considering the inherent variability in your data.

## Why the grain size distribution plots produced by the GST script and the classic CSD charts do not use the same units on the y-axis? 

As you may notice, classic CSDs charts (Marsh, 1988) show in the vertical axis the logarithmic variation in population density or log(frequency) in mm<sup>-4</sup>, while the stereological methods put in the GrainSizeTools (GST) script returns plots with a linear frequency (per unit volume). This distinction arises from their distinct purposes.

**Classic CSD charts** (Marsh, 1988) were originally designed for deriving two things in magmatic systems: i) nucleation rates and ii) crystal growth rates. In these systems, small grains are more abundant than large ones and the increase in quantity is typically exponential. The logarithmic scale aids in obtaining a straight line, facilitating the derivation of crystal growth rates and nucleation rates. Further, the intercept of the line at grain size equal to zero allows for estimating the nuclei population density.

In recrystallized rocks, there is no grain size equal to zero and we usually unknown the crystallization time, so the use of CSDs is not optimal. Furthermore, the use of the logarithm in the vertical axis has two main disadvantages for microstructural studies: (i) it obscures the reading of the volume of a particular grain fraction, a common target in microtectonic studies, and (ii) it prevents the easy identification of the features of grain size distribution, which is relevant for applying the two-step method. In summary, the difference in units reflects the specific aims and considerations of each method, with the GST script tailored to microstructural studies in recrystallized rocks.

## Why the sum of all frequencies in the histograms is not equal to one?

The sum of all frequencies in the histograms is not equal to one due to the normalization process. After the frequencies are initially normalized to one, indicating that the integral over the range equals one, the procedure divides them by the bin size. Consequently, the sum of all frequency values will not equal one unless the bin size is one. This normalization method was deliberately chosen for several reasons:

1. **Comparing Distributions:** It facilitates the comparison of distributions using different bin sizes, allowing for flexibility in the analysis.
2. **Two-Step Method Requirement:** This normalization method is necessary for the proper application of the two-step method, ensuring accurate and consistent results across various datasets.

In essence, the non-summing to one outcome is a consequence of a deliberate normalization strategy that enhances the versatility and applicability of the analysis, particularly in scenarios where different bin sizes are employed.

## Specifying Script Version in Publications  

Yes, it is highly recommended to specify the version of the script used in a publication. This practice helps ensure transparency and allows others to replicate your results. Bugs or updates in script versions may impact the outcomes, and version information aids in tracking and correcting any issues.

When indicating the version in your manuscript, consider the following format: *"...we used the GrainSizeTools script version x..."* and then refer to the general citation:

Lopez-Sanchez, Marco A. (2018). GrainSizeTools: a Python script for grain size analysis and paleopiezometry based on grain size. _Journal of Open Source Software_, 3(30), 863, https://doi.org/10.21105/joss.00863

## Does the script work with Python 2.7.x?  

No, the script does not work with Python 2 as this Python branch was officially discontinued in 2020, so it is time to move on.



[return me to the home page](https://marcoalopez.github.io/GrainSizeTools/)  