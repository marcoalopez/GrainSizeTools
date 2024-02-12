# Quantifying grain size populations using GrainSizeTools Script

TODO

> [!CAUTION]
> The instructions given here are for the version of the script referred above, if you get errors following these instructions, make sure you are using the latest version of the script before reporting them.

[TOC]

## 1. How to import datasets



## 2. Statistical description of grain size populations

TODO

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

> [!IMPORTANT]
> Key information users need to know to achieve their goal.



### 3.x Testing lognormality or normality

TODO

> [!TIP]
> To know more about the q-q plot see https://serialmentor.com/dataviz/



### 3.x The area-weighted distribution

TODO

> [!IMPORTANT]
> _**When to use and not to use the area-weighted approach?**_
> You **should not use** the area-weighted mean for the calibration of paleopiezometers or for the comparison of grain size populations, as this is a poorly optimised central tendency measure ([Lopez-Sanchez, 2020](https://doi.org/10.1016/j.jsg.2020.104042)). On the other hand, the area-weighted distribution is useful to visualize the coarser size range, since in number-weighted distributions these sizes are diluted but can represent a significant area or volume.


### 3.3 Normalized grain size distributions

TODO

### 3.x. Saving your figures

TODO



## 4. Comparing different grain size populations

TODO