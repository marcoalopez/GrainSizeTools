# Using the steorology module

Stereology is a set of mathematical methods designed to provide quantitative information about a three-dimensional feature from measurements made on two-dimensional sections. Unlike tomography, which aims to reconstruct the 3D geometry of a material, stereology is used to estimate specific 3D features. Here we will use stereological methods to approximate the true grain size distribution from the grain size distribution observed in the sections.

The GrainSizeTools script includes two stereological methods for this purpose: 1) the Saltykov method, and 2) the two-step method.

## The Saltykov method

> **What is it?**  
> The Saltykov method is a stereological technique that approximates the true grain size distribution from the histogram of the distribution of apparent grain size sections. The method is versatile as it does not assume any particular type of statistical distribution.
>
> **What do I use it for?**  
> In the geosciences, the Saltykov method is used primarily to estimate the volume fraction of a given range of grain sizes, but also to estimate the actual average grain size (see cautionary note below).
>
> **What are its limitations?**  
> Despite its utility, the Saltykov method has several limitations when applied to rocks:
>
> - **Assumption of Non-Touching Spheres**. The method assumes non-touching spheres uniformly distributed in a matrix (e.g. bubbles in a piece of glass), a condition rarely met in polycrystalline rocks. To apply the method, the grains should be at least approximately equiaxed, which is typically the case for recrystallized grains.
> - **Dependence on Histogram Classes**. The accuracy of the method is affected by the number of classes in the histogram. There's a trade-off: fewer classes improve the numerical stability of the method, but worsen the approximation of the target distribution, and vice versa. Currently, there is no exact method for finding the optimal number of classes, and this must be set by the user or determined by a rule of thumb. Using the histogram also means that we cannot get a complete description of the grain size distribution.
> - **Lack of Error Estimation Formulation**. The Saltykov method lacks a formulated procedure for estimating errors during the unfolding process, which limits the ability to assess the reliability of the results
> - **Inability to Estimate True Average Grain Size**. It's impossible to obtain an estimate of the true average grain size (3D) because individual data is lost when using the histogram. In other words, the Saltykov method attempts to reconstruct the histogram of the true grain size population, not to convert each apparent diameter into the true one. While there are methods to estimate an average from the resulting histogram, it's important to emphasize that **this estimate is derived from a stereological model, not actual empirical data**.

TODO

> [!CAUTION]
>
> ### Why prefer averages from apparent grain size to those estimated from unfolded grain size distributions in palaeopiezometry?
>
> While one might be tempted to use a stereological method to estimate the midpoint of the modal interval or some other unidimensional parameter based on the calculated grain size distribution, we argue that this approach offers no advantages and comes with serious disadvantages.
>
> The rationale is that 3D grain size distributions are estimated using a stereological model. This means that the accuracy of the estimates depends not only on measurement errors but also on the robustness of the model itself. Unfortunately, stereological methods are based on weak geometric assumptions, and their results will always be, at best, approximate. This means that the precision and accuracy of averages estimated from 3D size distributions will be **significantly inferior in performance and reliability** to those based on the original distribution of grain sections. The latter, although estimating an apparent grain size, is based on real data rather than a model.
>
> **Recommendation**. In summary, it's advisable to use stereological methods only when there’s a need to estimate the volume occupied by a particular grain size fraction, to investigate the shape of the true grain size distribution. or when you need to use an average based on actual grain sizes (e.g. when you need to compare the average grain size calculated by a tomographic technique with that estimated from a section). Otherwise, for better precision and accuracy, opt for averages based on the apparent grain size distribution.



## The two-step method

> **What is it?**  
> The two-step method is a stereological technique that approximates the true grain size distribution from the histogram of the distribution of apparent grain size intervals. It differs from the Saltykov method in that the population is not described by a histogram but by a mathematical distribution. The method is thus **distribution dependent**, i.e. it assumes that the grain sizes follow a lognormal distribution. The method fits a lognormal distribution to the output of the Saltykov method, hence the name "two-step method".
>
> **What do I use it for? **  
> The Two-Step Method is primarily used to estimate the lognormal distribution of grain sizes, which includes determining the shape and location of the distribution. It can also be used to estimate the volume fraction of a particular range of grain sizes.
>
> **What are its limitations? ** 
>
> - **Distribution Dependency**. The method assumes a lognormal distribution for grain size, which may not accurately represent certain materials.
> - **Inherited Limitations from the Saltykov method**. The method is partially based on the Saltykov method and therefore inherits some of its limitations. The method however do not require to define a specific number of classes. 

TODO

> [!NOTE]
> **Understanding MSD Value and its Purpose**  
> MSD, or _Multiplicative Standard Deviation_, is a parameter that characterizes the shape of a grain size distribution using a single value, under the assumption that the distribution follows a lognormal pattern. In simpler terms, the MSD value provides a measure of the asymmetry or skewness of the grain size distribution. An MSD value equal to one corresponds to a normal (Gaussian) distribution, while values greater than one indicate log-normal distributions with varying degrees of asymmetry (Figure a). **Scale-Independent Comparison**. The advantage of this approach is that a single parameter, the MSD, can define the shape of the grain size distribution independently of its scale (Figure b). This makes it very convenient for comparing the shape of two or more grain size distributions.
> 
> ![Figura](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/MSD_value.png)
>**Figure**. Probability density functions of selected lognormal distributions taken from [Lopez-Sanchez and Llana-Fúnez (2016)](http://www.sciencedirect.com/science/article/pii/S0191814116301778). (a) Lognormal distributions with different MSD values (shapes) and the same median/geometric mean (4). (b) Lognormal distributions with the same shape corresponding to an MSD value (1.5) and different medians/geometric means (note that different medians/geometric means imply different scales in the horizontal and vertical directions).

