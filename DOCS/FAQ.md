# Frequently Asked Questions

- [Who is this script for?](#who-is-this-script-for-)
- [What is paleopizometry?](#what-is-paleopizometry-)
- [Why use apparent grain size measures over measures estimated from unfolded 3D grain size distributions in paleopiezometry studies?](#why-use-apparent-grain-size-measures-over-measures-estimated-from-unfolded-3d-grain-size-distributions-in-paleopiezometry-studies-)
- [What measure of central tendency (i.e. average) do I have to use?](#what-measure-of-central-tendency--ie-average--do-i-have-to-use-)
- [When to use the standard deviation and the confidence interval for the average?](#when-to-use-the-standard-deviation-and-the-confidence-interval-for-the-average-)
- [What is an MSD value? Understanding MSD Value and its Purpose](#what-is-an-msd-value--understanding-msd-value-and-its-purpose)
- [Why the grain size distribution plots produced by the GST script and the classic CSD charts do not use the same units on the y-axis?](#why-the-grain-size-distribution-plots-produced-by-the-gst-script-and-the-classic-csd-charts-do-not-use-the-same-units-on-the-y-axis-)
- [Why the sum of all frequencies in the histograms is not equal to one?](#why-the-sum-of-all-frequencies-in-the-histograms-is-not-equal-to-one-)
- [Specifying Script Version in Publications](#specifying-script-version-in-publications)
- [Does the script work with Python 2.7.x?](#does-the-script-work-with-python-27x-)
- [I get the results but not the plots when using the Spyder IDE: ValueError: _Image size of ... is too large_](#i-get-the-results-but-not-the-plots-when-using-the-spyder-ide--valueerror---image-size-of--is-too-large-)

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

## What is paleopizometry?

Paleopiezometers refer to microstructural features of deformed rocks that vary with the magnitude of the applied differential stress under which they formed (Twiss and Moores, 2006). They serve to infer differential stresses in the geological past, hence the name paleopiezometry, and they are an essential tool for validating rheological models of the lithosphere. The most prevalent microstructure used for this purpose is the average recrystallized (apparent) grain size. This choice is due to its ease of measurement in recrystallized rocks.

## Why use apparent grain size measures over measures estimated from unfolded 3D grain size distributions in paleopiezometry studies?  

One might be tempted to use a stereological method to estimate the midpoint of the modal interval or another unidimensional parameter based on the actual grain size distribution rather than relying on the mean, median, or frequency peak of the apparent grain size distribution. However, we assert that there is no advantage to this approach and it comes with serious disadvantages.

The reason is that 3D grain size distributions are estimated using a stereological model, making the accuracy of the estimates dependent not only on errors introduced during measurement but also on the robustness of the model itself. Unfortunately, stereological methods are founded on weak geometric assumptions, and their results will always be, at best, approximate. This implies that the precision and accuracy of average values estimated from 3D size distributions will be **significantly inferior** compared to those based on the original distribution of grain profiles. The latter, although estimating an apparent grain size, relies on real data rather than a model.

In summary, utilize stereological methods only when there is a need to estimate the volume occupied by a specific grain size fraction or to investigate the shape of the true grain size distribution. Otherwise, opt for estimates based on the apparent grain size distribution for better precision and accuracy.

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

The **standard deviation** (s.d.) is the typical difference between each value and the mean value. So, in this case, it describes how broadly the grain size values are distributed within the sample.

The **standard error of the mean** (s.e.m.) is an estimate of how variable the means will be if the experiment or measure is repeated multiple times. The s.e.m. may serve to check whether sets of samples are likely to come from the same or a similar population.

The **95 % confidence interval** (C.I., 95%) means that the population mean will lie in this interval with 95% confidence. This metric is valuable when assessing the precision of the average or comparing averages between different grain size populations. It's like  saying, "We're 95% confident that the true average grain size falls  within this range." In simpler terms, it gives you a sense of how certain you can be about the average, considering the inherent variability in your data.

## What is an MSD value? Understanding MSD Value and its Purpose

MSD, or *Multiplicative Standard Deviation*, is a parameter used to characterize the shape of a grain size distribution using a single value, assuming the distribution follows a lognormal pattern. In simpler terms, the MSD value provides a measure of the asymmetry or skewness of the grain size distribution. For example:

- an MSD value equal to one corresponds to a normal (Gaussian) distribution

- Values greater than one indicate log-normal distributions of varying shapes, being the higher the MSD value the greater the asymmetry of the distribution (Figure a).

This approach is advantageous because a single parameter can define the shape of the grain size distribution independently of its scale (Fig. b), which is very convenient for comparing the shape of two or more grain size distributions.

![Figura](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/MSD_value.png)

_Probability density functions of selected lognormal distributions taken from [Lopez-Sanchez and Llana-Fúnez (2016)](http://www.sciencedirect.com/science/article/pii/S0191814116301778). (a) Lognormal distributions with different MSD values (shapes) and the same median/geometric mean (4). (b) Lognormal distributions with the same shape corresponding to an MSD value (1.5) and different medians/geometric means (note that different medians/geometric means imply different scales in the horizontal and vertical directions)._

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

No, the script does not work with Python 2.7.x. Python 2.7.x versions were officially discontinued in 2020 so it is time to move on.

## I get the results but not the plots when using the Spyder IDE: ValueError: _Image size of ... is too large_

This issue is produced because the size of the figure returned by the script is too large to show them inside the console using the **inline** mode. To fix this go to the Spyder menu bar and in  ```Tools>Preferences>IPython console>Graphics``` find _Graphics backend_, select _Automatic_, and then restart Spyder. As an alternative you can type ``%matplotlib auto`` in the console without needing to restart Spyder but this change will be temporary (i.e. only valid for the current session).



[return me to the home page](https://marcoalopez.github.io/GrainSizeTools/)  