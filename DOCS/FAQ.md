# Frequently Asked Questions

- [Who is this script for?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#who-is-this-script-for)
- [What is paleopizometry?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#what-is-paleopizometry)
- [Why use apparent grain size measures instead of measures estimated from unfolded 3D grain size distributions in paleopiezometry studies?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#why-use-apparent-grain-size-measures-instead-of-measures-estimated-from-unfolded-3d-grain-size-distributions-in-paleopiezometry-studies)
- [What measure of central tendency (i.e. average) do I have to use?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#what-measure-of-central-tendency-ie-average-do-i-have-to-use)
- [When to use the standard deviation and the confidence interval for the average?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#when-to-use-the-standard-deviation-and-the-confidence-interval-for-the-average)
- [What is an MSD value? What is it used for?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#what-is-an-msd-value-what-is-it-used-for)
- [Why the grain size distribution plots produced by the GST script and the classic CSD charts do not use the same units on the y axis?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#why-the-grain-size-distribution-plots-produced-by-the-gst-script-and-the-classic-csd-charts-do-not-use-the-same-units-on-the-y-axis)
- [Why the sum of all frequencies in the histograms is not equal to one?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#why-the-sum-of-all-frequencies-in-the-histograms-is-not-equal-to-one-)
- [Is it necessary to specify the version of the script used in a publication? How can this be indicated?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#is-it-necessary-to-specify-the-version-of-the-script-used-in-a-publication-how-can-this-be-indicated)
- [Does the script work with Python 2.7.x and 3.x versions? Which version do I choose?](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#does-the-script-work-with-python-27x-and-3x-versions-which-version-do-i-choose)
- [I get the results but not the plots when using the Spyder IDE: ValueError: _Image size of ... is too large_](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md#i-get-the-results-but-not-the-plots-when-using-the-spyder-ide-valueerror-image-size-of--is-too-large)

### Who is this script for?
The script pursues three different goals:

- promoting best practices and reproducibility in grain size analysis using robust statistics, avoiding manual steps during data processing, and promoting standard procedures for grain size characterization
- maintain a curated and up-to-date database of grain-size-based paleopiezometers for different mineral phases
- provide a platform to implement and test new methods for grain size characterization in recrystallized materials

More specifically, the script is targeted at anyone who wants to: i) visualize grain size distributions, ii) obtain a set of apparent grain size measures to estimate the magnitude of differential stress in dynamically recrystallized rocks, and iii) approximate the actual (3D) distribution of grain sizes from thin sections using stereological methods. The latter includes an estimate of the volume occupied by a particular grain size fraction and a parameter to characterize the shape of the population of grain sizes (assuming that the distribution of grain sizes follows a lognormal distribution). The stereological methods assume that grains have equant or near-equant (AR < 2.0) shapes, which mostly include all recrystallized grains produced during static and dynamic recrystallization. See more details [here](http://joss.theoj.org/papers/10.21105/joss.00863). For igneous studies involving tabular grains far from near-equant objects, we recommend other approaches such as those implemented in the *CSDCorrections* software (Higgins 2000). See the references list section for details.

### What is paleopizometry?

Paleopiezometers are microstructural features of deformed rocks that vary with the magnitude of the applied differential stress under which they formed (Twiss and Moores, 2006). They serve to infer differential stresses in the geological past, hence the name paleopiezometry, and they are an essential tool for validating rheological models of the lithosphere. The most common microstructure is the average recrystallized (apparent) grain size as it is the easiest microstructure to measure in recrystallized rocks.

### Why use apparent grain size measures instead of measures estimated from unfolded 3D grain size distributions in paleopiezometry studies?  

One might be tempted to use a stereological method to estimate the midpoint of the modal interval or some other unidimensional parameter based on the actual grain size distribution rather than using the mean, median, or frequency peak of the apparent grain size distribution. We believe that there is no advantage to doing this, but there are serious disadvantages. The reason is that 3D grain size distributions are estimated using a stereological model and thus the accuracy of the estimates depends not only on the introduction of errors during the measurement but also on the robustness of the model. Unfortunately, stereological methods are based on weak geometric assumptions and the results will always be approximate at best. This means that the precision and accuracy of the average values estimated from 3D size distributions will be **much poorer** than those based on the original distribution of grain profiles, which, although estimating an apparent grain size are based on real data, not a model.  In summary, use stereological methods only when you need to estimate the volume occupied by a particular grain size fraction or investigate the shape of the true grain size distribution, otherwise use estimates based on the apparent grain size distribution.

### What measure of central tendency (i.e. average) do I have to use?

That depends on your target and your dataset. First, if you want to use a specific piezometer you must use the same average used in the piezometric calibration. Otherwise, if you want to establish a new piezometric calibration or just summarize your distribution these are the guidelines based on [Lopez-Sanchez (2020)](https://doi.org/10.1016/j.jsg.2020.104042):

- **Use the geometric mean**. It performs better than other central tendency measures in lognormal-like populations regardless of asymmetry and sample size.
- The **median** is the preferred option when data contamination (outliers and/or observations from mixed distributions) could be an issue.
- The **arithmetic mean** is the most backwards-compatible average due to its common use in the past. Theoretically, it outperforms the median in low to moderately skewed distributions (MSD < 1.7) as long the presence of extreme values (outliers) remains small. The estimation of error margins for the arithmetic mean remains problematic in real samples (Lopez-Sanchez, 2020) and thus the geometric mean or the median is preferred.
- The **KDE-based mode** usually performs worse than other central tendency measures. This average is, however, the only one that remains robust in some specific situations that are likely to occur in grain size studies such as notable different resolution limits and size cut-offs.
- **Avoid the use of root mean squared (RMS) or the area-weighted mean**, both perform poorly.

More details [here](https://github.com/marcoalopez/marcoalopez.github.io/blob/master/docs/2020_JSG_SG_104042.pdf)

### When to use the standard deviation and the confidence interval for the average?

That depends on the information you want to provide. If the message is on the spread of the grain size population (e.g. to compare between different grain size distributions) the standard deviation or, alternatively, the interquartile range is the metric you want. If the interest is in the precision of the average or in comparing averages between different grain size populations the confidence interval is your metric (e.g., when using paleopiezometers). More precisely:

The **standard deviation** (s.d.) is the typical difference between each value and the mean value. So, in this case, it describes how broadly the grain size values are distributed within the sample.

The **standard error of the mean** (s.e.m.) is an estimate of how variable the means will be if the experiment or measure is repeated multiple times. The s.e.m. may serve to check whether sets of samples are likely to come from the same or a similar population.

The **95 % confidence interval** (C.I., 95%) means that the population mean will lie in this interval with 95% confidence.

### What is an MSD value? What is it used for? 

MSD stands for _Multiplicative Standard Deviation_ and it is a parameter that allows defining the shape of the grain size distribution using a single value assuming that it follows a lognormal distribution. In plain language, the MSD value gives a measure of the asymmetry (or skewness) of the grain size distribution. For example, an MSD value equal to one corresponds to a normal (Gaussian) distribution and values greater than one with log-normal distributions of different shapes, being the higher the MSD value the greater the asymmetry of the distribution (Figure a). The advantage of this approach is that by using a single parameter we can define the shape of the grain size distribution independently of its scale (Fig. b), which is very convenient for comparing the shape of two or more grain size distributions.

![Figura](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/MSD_value.png)

_Probability density functions of selected lognormal distributions taken from [Lopez-Sanchez and Llana-Fúnez (2016)](http://www.sciencedirect.com/science/article/pii/S0191814116301778). (a) Lognormal distributions with different MSD values (shapes) and the same median/geometric mean (4). (b) Lognormal distributions with the same shape corresponding to an MSD value (1.5) and different medians/geometric means (note that different medians/geometric means imply different scales in the horizontal and vertical directions)._

### Why the grain size distribution plots produced by the GST script and the classic CSD charts do not use the same units on the y axis? 

As you may notice, classic CSDs charts (Marsh, 1988) show in the vertical axis the logarithmic variation in population density or log(frequency) in mm<sup>-4</sup>, while the stereological methods put in the GrainSizeTools (GST) script returns plots with a linear frequency (per unit volume). This is due to the different aims of the CSDs and the plots returned by the GST script. Originally, CSDs were built for deriving two things in magmatic systems: i) nucleation rates and ii) crystal growth rates. In these systems, small grains are more abundant than large ones and the increase in quantity is typically exponential. The use of the logarithm in the vertical axis helps to obtain a straight line with the slope being the negative inverse of the crystal growth times the time of crystallization. Further, the intercept of the line at grain size equal to zero allows for estimating the nuclei population density. In recrystallized rocks, there is no grain size equal to zero and we usually unknown the crystallization time, so the use of the CSDs is not optimal. Furthermore, the use of the logarithm in the vertical axis has two main disadvantages for microstructural studies: (i) it obscures the reading of the volume of a particular grain fraction, a common target in microtectonic studies, and (ii) it prevents the easy identification of the features of grain size distribution, which is relevant for applying the two-step method.

### Why the sum of all frequencies in the histograms is not equal to one?

This is because after the frequencies are normalized to one (i.e. the integral over the range equals one), the procedure divides them by the bin size. This means that the sum of all frequency values will not be equal to one unless the bin size is one. We have chosen this normalization method because it allows comparing distributions using different bin sizes, and it is required to properly apply the two-step method.

### Is it necessary to specify the version of the script used in a publication? How can this be indicated?  

Yes, it is always desirable to indicate the version of the script used. The rationale behind this is that codes may contain bugs and versioning allow us to track them and correct the results of already published studies in case a bug is discovered later. The way we advise you to follow is by explicitly indicating the version in your manuscript as follows: _"...we used the GrainSizeTools script version x..."_ and then use the general citation in the reference list as follows:

Lopez-Sanchez, Marco A. (2018). GrainSizeTools: a Python script for grain size analysis and paleopiezometry based on grain size. _Journal of Open Source Software_, 3(30), 863, https://doi.org/10.21105/joss.00863

### Does the script work with Python 2.7.x ?  

No. Python 2.7.x versions have been discontinued in 2020 and it is time to move on. GrainSizeTools script v1.4.5 or earlier are compatible, but these older versions have fewer features and bugs will not be fixed if found.

### I get the results but not the plots when using the Spyder IDE: ValueError: _Image size of ... is too large_

This issue is produced because the size of the figures returned by the script are too large to show them inside the console using the **inline** mode. To fix this go to the Spyder menu bar and in  ```Tools>Preferences>IPython console>Graphics``` find _Graphics backend_, select _Automatic_, and then restart Spyder. As an alternative you can type ``%matplotlib auto`` in the console without needing to restart Spyder but this change will be temporary (i.e. only valid for the current session).



[return me to the home page](https://marcoalopez.github.io/GrainSizeTools/)  