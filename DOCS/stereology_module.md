# Using the steorology module

Stereology is a set of mathematical methods designed to provide quantitative information about a three-dimensional feature from measurements made on two-dimensional sections. Unlike tomography, which aims to reconstruct the 3D geometry of a material, stereology is used to estimate specific 3D features. Here we will use two stereological methods to approximate the true grain size distribution from the apparent grain size distribution measured on a section: 1) the Saltykov method, and 2) the two-step method.

## The Saltykov method

> **What is it?**  
> The Saltykov method is a stereological technique that approximates the true grain size distribution from the histogram of the distribution of apparent grain size sections. The method is versatile as it does not assume any particular type of statistical distribution.
>
> **What do I use it for?**  
> In the geosciences, the Saltykov method is used primarily to estimate the volume fraction of a given range of grain sizes, but also to estimate the actual average grain size (see cautionary note on this later).
>
> **What are its limitations?**  
> Despite its utility, the Saltykov method has several limitations when applied to rocks:
>
> - **Assumption of Non-Touching Spheres**. The method assumes non-touching spheres uniformly distributed in a matrix (e.g. bubbles in a piece of glass), a condition rarely met in polycrystalline rocks. To apply the method, the grains should be at least approximately equiaxed, which is typically the case for recrystallized grains.
> - **Dependence on Histogram Classes**. The accuracy of the method is affected by the number of classes in the histogram. There's a trade-off: fewer classes improve the numerical stability of the method, but worsen the approximation of the target distribution, and vice versa. Currently, there is no exact method for finding the optimal number of classes, and this must be set by the user or determined by a rule of thumb. Using the histogram also means that we cannot get a complete description of the grain size distribution.
> - **Lack of Error Estimation Formulation**. The Saltykov method lacks a formulated procedure for estimating errors during the unfolding process, which limits the ability to assess the reliability of the results
> - **Inability to Estimate True Average Grain Size**. It's impossible to obtain an estimate of the true average grain size (3D) because individual data is lost when using the histogram. In other words, the Saltykov method attempts to reconstruct the histogram of the true grain size population, not to convert each apparent diameter into the true one. While there are methods to estimate an average from the resulting histogram, it's important to emphasize that **this estimate is derived from a stereological model, not actual empirical data**.

To apply this method, we use the ``Saltykov`` function of the stereology module. This function has the following parameters:

```reStructuredText
diameters : array_like
    the apparent diameters of the grains.

numbins : positive integer, optional
    the number of bins/classes of the histogram. If not declared,
    is set to 10 by default.

calc_vol : positive scalar or None, optional
    if the user specifies a diameter, the function will return the volume
    occupied by the grain fraction up to that diameter.

text_file : string or None, optional
    if the user specifies a name, the function will store a csv file
    with that name containing the Saltykov output.

return_data : bool, optional
   if True the function will return the position of the midpoints and
   the frequencies.

left_edge : positive scalar or 'min', optional
    set the left edge of the histogram. Default is zero.
```

The only input required is the distribution of apparent diameters (``diameters``). From here the user can specify the number of classes (``numbins``), calculate the volume occupied by a grain size fraction (``calc_vol``), generate a csv file with the data (``text_file``), retrieve some data for further calculations (return_data) and set the initial boundary of the histogram (``left_edge``). We will see examples of these below.

```python
# Import a dataset with grain sectional areas
filepath = 'C:/Users/marco/Documents/GitHub/GrainSizeTools/grain_size_tools/DATA/data_set.txt'
dataset = pd.read_csv(filepath, sep='\t')

# estimate equivalent circular diameters
dataset['diameters'] = 2 * np.sqrt(dataset['Area'] / np.pi)

# apply the Saltykov method from stereology module
stereology.Saltykov(dataset['diameters'], numbins=11, calc_vol=50)
```

```
=======================================
volume fraction (up to 50 microns) = 41.65 %
bin size = 14.24
=======================================
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/saltykov.png?raw=true)

TODO

## The two-step method

> **What is it?**  
> The two-step method is a stereological technique that approximates the true grain size distribution from the histogram of the distribution of apparent grain size intervals. It differs from the Saltykov method in that the population is not described by a histogram but by a mathematical distribution. The method is thus **distribution dependent**, i.e. it assumes that the grain sizes follow a lognormal distribution. The method fits a lognormal distribution to the output of the Saltykov method, hence the name "two-step method". More info [here](https://github.com/marcoalopez/marcoalopez.github.io/blob/master/docs/2016_JSG_Lopez-Sanchez.pdf).
>
> **What do I use it for?**  
> The Two-Step Method is primarily used to estimate the lognormal distribution of grain sizes, which includes determining the shape and location of the distribution. It can also be used to estimate the volume fraction of a particular range of grain sizes.
>
> **What are its limitations?** 
>
> - **Distribution Dependency**. The method assumes a lognormal distribution for grain size, which may not accurately represent certain materials. Besides, the method only works properly for unimodal grain size distributions.
> - **Inherited Limitations from the Saltykov method**. The method is partially based on the Saltykov method and therefore inherits some of its limitations. The method however do not require to define a specific number of classes. 

To apply this method, we use the ``calc_shape`` function of the stereology module. This function has the following parameters:

```reStructuredText
diameters : array_like
    the apparent diameters of the grains
    
class_range : tupe or list with two values, optional
    the range of classes considered. The algorithm will estimate the optimal
    number of classes within the defined range. Default = (10, 20)
```

The only data required is the distribution of apparent diameters (``diameters``). From here, the user can only specify a range of number of classes (``numbins``), if necessary, an algorithm will take care of estimating the optimal number of classes within this range.

```python
stereology.calc_shape(dataset['diameters'])
```

```reStructuredText
=======================================
OPTIMAL VALUES
Number of classes: 11
MSD (lognormal shape) = 1.63 ± 0.06
Geometric mean (scale) = 36.05 ± 1.27
=======================================
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/2step.png?raw=true)

The method returns the values of the lognormal distribution that best fits our model, in this case defined by two values: the geometric mean (scale) and its MSD (shape) with an estimate of their errors.

> [!NOTE]
> **Understanding the MSD Value and its Purpose**  
> MSD, or _Multiplicative Standard Deviation_, is a parameter that characterizes the shape of a grain size distribution using a single value, under the assumption that the distribution follows a lognormal pattern. In simpler terms, the MSD value provides a measure of the asymmetry or skewness of the grain size distribution. An MSD value equal to one corresponds to a normal (Gaussian) distribution, while values greater than one indicate log-normal distributions with varying degrees of asymmetry (Figure a). **Scale-Independent Comparison**. The advantage of this approach is that a single parameter, the MSD, can define the shape of the grain size distribution independently of its scale (Figure b). This makes it very convenient for comparing the shape of two or more grain size distributions.
> 
> ![Figura](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/MSD_value.png)
>**Figure**. Probability density functions of selected lognormal distributions taken from [Lopez-Sanchez and Llana-Fúnez (2016)](http://www.sciencedirect.com/science/article/pii/S0191814116301778). (a) Lognormal distributions with different MSD values (shapes) and the same median/geometric mean (4). (b) Lognormal distributions with the same shape corresponding to an MSD value (1.5) and different medians/geometric means (note that different medians/geometric means imply different scales in the horizontal and vertical directions). Let's see some examples.

### Estimate other averages

The lognormal distribution can also be used to calculate tother averages. For example, to estimate the arithmetic mean or the frequency peak we use the following formulation

$$
\overline{D} = e^{\mu + \sigma^2 / 2}
$$

$$
Mode = e^{\mu - \sigma^2}
$$

where $\mu$ and $\sigma$ are the log-transformed values of the geometric mean and the MSD, respectively. Thus:

```python
geo_mean = 36.05
msd = 1.63
mu = np.log(geo_mean)
sigma = np.log(msd)

amean = np.exp(mu + (sigma**2 / 2))
mode = np.exp(mu - sigma**2)
print(f'mean = {amean:.2f}')
print(f'mode = {mode:.2f}')
```

```reStructuredText
mean = 40.62
mode = 28.39
```

> [!NOTE]
> In a perfect lognormal distribution, the median and geometric mean coincide, so there is no need to calculate the median. In real distributions, which never match a perfect model, there is a difference between these two values.

> [!CAUTION]
>
> ### Why prefer averages from apparent grain size to those estimated from unfolded grain size distributions in palaeopiezometry?
>
> While one might be tempted to use a stereological method to estimate the midpoint of the modal interval or some other unidimensional parameter based on the calculated grain size distribution, we argue that this approach offers no advantages and comes with serious disadvantages.
>
> The rationale is that 3D grain size distributions are estimated using a stereological model. This means that the accuracy of the estimates depends not only on measurement errors but also on the robustness of the model itself. Unfortunately, stereological methods are based on weak geometric assumptions, and their results will always be, at best, approximate. This means that the precision and accuracy of averages estimated from 3D size distributions will be **significantly inferior in performance and reliability** to those based on the original distribution of grain sections. The latter, although estimating an apparent grain size, is based on real data rather than a model.
>
> **Recommendation**. In summary, it's advisable to use stereological methods only when there’s a need to estimate the volume occupied by a particular grain size fraction, to investigate the shape of the true grain size distribution or when you need to use an average based on actual grain sizes (e.g. when you need to compare the average grain size calculated by a tomographic technique with that estimated from a section). Otherwise, for better precision and accuracy, opt for averages based on the apparent grain size distribution.



### Estimate volume fractions from a lognormal distribution

To estimate a volume fraction occupied by a particular particle size range we will use the ``lognorm`` function from the  ``scipy.stats`` module as follows

```python
# import lognorm
from scipy.stats import lognorm

# Calculate the lognormal distribution
dist = lognorm(s=sigma, scale=geo_mean)

# Calculate the volume fraction between sizes 75 and 25
volume_fraction = dist.cdf(75) - dist.cdf(25)

print(f'volume fraction = {volume_fraction * 100:.1f} %')
```

```reStructuredText
volume fraction = 70.6 %
```

Basically, we determined the probability density function (PDF) of the lognormal distribution and then estimated the volume fraction occupied by a given range of grain size values (here 75 and 25) by integrating the PDF over that range. This is equivalent to finding the cumulative distribution function (CDF) values at 75 and 25 and subtracting them.

---

[Return me to the home page](https://marcoalopez.github.io/GrainSizeTools/)  
