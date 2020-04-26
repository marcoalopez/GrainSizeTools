# The plot module: visualizing grain size distributions

To visualize the grain size distribution there are several methods implemented in the module named ```plot```.  All methods of the *plot* module can be invoked by writing ```plot.*```, where * refers to the plot to be used.

> 👉 If you write ``plot.`` and then press the tab key a menu will pop up with all the methods implemented in the plot module

The main method is ```plot.distribution()```. This method allows to visualize the grain size population through the histogram and/or the kernel density estimate (KDE), as well as the location of the different averages in the distribution (Fig. 7). To use it we call this function and pass as an argument the population of grain sizes as follows:

```python
plot.distribution(dataset['diameters'])
```

    =======================================
    Number of classes =  45
    binsize =  3.41
    =======================================
    =======================================
    KDE bandwidth =  4.01
    =======================================

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_distribution.png?raw=true)

*Figure 7. The ```plot.distribution()``` return with default options. This shows the histogram, the kernel density estimate (KDE) of the distribution, and the location of the different averages*

The method returns a plot, the number of classes and bin size of the histogram, and the bandwidth (or kernel) of the KDE. The ```plot.distribution()``` method contains different options that we will commented on in turn:

```python
def distribution(data,
                 plot=('hist', 'kde'),
                 avg=('amean', 'gmean', 'median', 'mode'),
                 binsize='auto', bandwidth='silverman'):
    """ Return a plot with the ditribution of (apparent or actual) grain sizes
    in a dataset.

    Parameters
    ----------
    data : array_like
        the size of the grains

    plot : string, tuple or list; optional
        the type of plot, either histogram ('hist'), kernel density estimate
        ('kde') or both ('hist', 'kde'). Default is both.

    avg : string, tuple or list; optional
        the central tendency measures o show, either the arithmetic ('amean')
        or geometric ('gmean') means, the median ('median'), and/or the
        KDE-based mode ('mode'). Default all averages.

    binsize : string or positive scalar; optional
        If 'auto', it defines the plug-in method to calculate the bin size.
        When integer or float, it directly specifies the bin size.
        Default: the 'auto' method.

        | Available plug-in methods:
        | 'auto' (fd if sample_size > 1000 or Sturges otherwise)
        | 'doane' (Doane's rule)
        | 'fd' (Freedman-Diaconis rule)
        | 'rice' (Rice's rule)
        | 'scott' (Scott rule)
        | 'sqrt' (square-root rule)
        | 'sturges' (Sturge's rule)

    bandwidth : string {'silverman' or 'scott'} or positive scalar, optional
        the method to estimate the bandwidth or a scalar directly defining the
        bandwidth. It uses the Silverman plug-in method by default.
    ...
    """
```

The only mandatory parameter is ```data``` which corresponds to the populations of grain sizes. The ``plot`` parameter allows you to define the method to visualize the population, either the histogram, the kernel density estimate or both (the default option). If we want to plot only the KDE or the histogram we do it as follows:


```python
plot.distribution(dataset['diameters'], plot='kde')
```

    =======================================
    KDE bandwidth =  4.01
    =======================================

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_distribution_kde.png?raw=true)

```python
plot.distribution(dataset['diameters'], plot='hist', binsize='doane')
```

    =======================================
    Number of classes =  17
    binsize =  9.02
    =======================================



![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_distribution_hist.png?raw=true)

In the example above using the histogram we passed as input the optional argument ```binsize```. This parameter allows us to use different plug-in methods implemented in the Numpy package to estimate "optimal" bin sizes for the construction of the histograms. The default mode, called ```'auto'```, uses the Freedman-Diaconis rule for large datasets and the Sturges rule otherwise. Other available plug-in methods are the Freedman-Diaconis ```'fd'```, Scott ```'scott'```, Rice ```'rice'```, Sturges ```'sturges'```, Doane ```'doane'```, and square-root ```'sqrt'```. For more details on these methods see [here](https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges).  We encourage you to use the default method ```'auto'```. Empirical experience indicates that the ```'doane'``` and ```'scott'``` methods work also pretty well when you have lognormal- and normal-like distributions, respectively. You can also define an ad-hoc bin size if you pass as input a positive scalar, for example:

```python
plot.distribution(dataset['diameters'], plot='hist', binsize=10.5)
```

The  ```avg``` parameter allows us to define which central tendency measure to show, either the arithmetic mean ```amean```, the geometric mean ```gmean``` means, the median ```median```, and/or the KDE-based mode ```mode```. By default, all averages are displayed.

Lastly, the parameter ``bandwidth`` allows you to define a method to estimate an optimal bandwidth to construct the KDE, either the ``'silverman'`` (the default) or the ``scott`` rules. The ``'silverman'`` and the ``'scott'`` rules, are both optimized for normal-like distributions, so they perform better when using over log-transformed grain sizes. You can also define your own bandwidth/kernel value by declaring a positive scalar instead. For example:

```python
plot.distribution(dataset['diameters'], plot='kde', bandwidth=5.0)
```

Note, however, that the bandwidth affects the location of the KDE-based mode. For consistency, you should use the same method or bandwidth used when calling the ```summarize``` method.



### Plotting the area-weighted distribution

The plot module also allows plotting the area-weighted distribution of grain sizes using the function ``area_weighted()``. This function also returns some basic statistics such as the area-weighted mean and the histogram features. For example: 

```python
plot.area_weighted(dataset['diameters'], dataset['Area'])
```

    =======================================
    DESCRIPTIVE STATISTICS
    Area-weighted mean grain size = 53.88 microns
    =======================================
    HISTOGRAM FEATURES
    The modal interval is 40.85 - 44.26 microns
    The number of classes are 46
    The bin size is 3.40 according to the auto rule
    =======================================



![png](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_area_weighted.png?raw=true)

*Figure X. The area-weighted apparent grain size distribution and the location of the area-weighted mean*

>  👉 ***When to use and not to use the area-weighted approach?***
>
> You **should not use** the area-weighted mean for the calibration of paleopiezometers or for the comparison of grain size populations, as this is a poorly optimised central tendency measure ([Lopez-Sanchez, 2020](https://doi.org/10.1016/j.jsg.2020.104042)). On the other hand, the area-weighted distribution is useful to visualize...TODO

### Testing lognormality

Sometimes can be helpful to test whether the data follows or deviates from a lognormal distribution. For example, to find out if the data set is suitable for applying the two-step stereological method or which confidence interval method is best for the arithmetic mean. The script use two methods to test whether the distribution of grain size follows a lognormal distribution. One is a visual method named [quantile-quantile (q-q) plots]([https://en.wikipedia.org/wiki/Q%E2%80%93Q_plot](https://en.wikipedia.org/wiki/Q–Q_plot)) and the other is a quantitative test named the [Shapiro-Wilk test](https://en.wikipedia.org/wiki/Shapiro–Wilk_test). For this we use the GrainSizeTools function ```test_lognorm``` as follows :

```python
plot.qq_plot(dataset['diameters'])
```

```
=======================================
Shapiro-Wilk test (lognormal):
0.99, 0.03 (test statistic, p-value)
It doesnt look like a lognormal distribution (p-value < 0.05)
(╯°□°）╯︵ ┻━┻
=======================================
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_qqplot.png?raw=true)

*Figure X. The q-q plot of the test dataset. Note that the distribution of apparent grain sizes deviates from the logarithmic at the ends*.

The Shapiro-Wilk test will return two different values, the test statistic and the p-value. This test considers the distribution to be lognormally distributed when the p-value is greater than 0.05. The q-q plot is a visual test that when the points fall right onto the reference line it means that the grain size values are lognormally distributed. The q-q plot has the advantage over the Shapiro-Wilk test that it shows where the distribution deviates from lognormality. 

> 👉 To know more about the q-q plot see https://serialmentor.com/dataviz/



### Normalized grain size distributions

Standardized grain size distributions are representations of the entire grain population standardized using an average, usually the arithmetic mean or median. The advantage of standardized distributions is that they allow comparison of whether or not the grain size distribution is similar to others when the average grain size between the different distributions differs significantly. For example, to check whether two or more grain size distributions have similar shapes we can compare their standard deviations (SD) or their interquartile ranges (IQR).  In this case, to facilitate the comparison, the standardized method shows the normalized distribution on a logarithmic scale based on *e* and provides the SD or IQR of the normalized population depending on the chosen normalizing factor.

```python
plot.normalized(dataset['diameters'], avg='amean')
```

```
=======================================
Normalized SD = 0.165
KDE bandwidth =  0.04
=======================================
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_normalized.png?raw=true)

*Figure X. KDE of the log-transformed grain size distribution normalized to the arithmetic mean (note that amean = 1).*