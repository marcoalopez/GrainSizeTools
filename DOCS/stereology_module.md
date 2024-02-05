# Using the steorology module

Stereology is a set of methods that provide quantitative information about a three-dimensional structure based on measurements made on two-dimensional sections. Unlike tomography, which aims to reconstruct the 3D geometry of a material, stereology is used to estimate specific 3D features. In this context, we use stereology to approximate the actual three-dimensional grain size distribution from the apparent two-dimensional grain size distribution observed in sections.

The GrainSizeTools script incorporates two stereological methods: 1) the Saltykov method, and 2) the two-step method.

## The Saltykov method

> **What is it?**
> The Saltykov method is a stereological technique used to approximate the actual three-dimensional grain size distribution from the histogram of the apparent two-dimensional grain size distribution. The method is versatile as it doesn’t assume a specific type of statistical distribution.
>
> **What do I use it for?**
> In geosciences, the Saltykov method is primarily used to estimate the volume fraction of a specific range of grain sizes.
>
> **What are its limitations?**
> Despite its utility, the Saltykov method has several limitations, particularly when applied to rocks:
>
> - **Assumption of Non-Touching Spheres**. The method assumes non-touching spheres uniformly distributed in a matrix (e.g. bubbles within a piece of glass), a condition seldom met in polycrystalline rocks. To apply the method, the grains should be at least approximately equiaxed, which is typically the case for recrystallized grains.
> - **Dependence on Histogram Classes**. The accuracy of the method is influenced by the number of classes in the histogram. There’s a trade-off: fewer classes improve the numerical stability of the method, but worsen the approximation of the targeted distribution, and vice versa. Currently, there is no exact method for finding the optimal number of classes, and this must be set by the user or determined by a rule of thumb. Using the histogram also means that we cannot obtain a complete description of the grain size distribution.
> - **Lack of Error Estimation Formulation**. The Saltykov method lacks a formulated procedure for estimating errors during the unfolding process, limiting the ability to assess the  reliability of the results
> - **Inability to Estimate Actual Average Grain Size**. It’s impossible to obtain an estimate of the true average grain size (3D) as individual data is lost when using the histogram. In other words, the Saltykov method reconstructs the 3D histogram, not every apparent diameter in the actual one. While there are methods to estimate an average from the resulting histogram, it's important to emphasize that **this estimation is derived from a stereological model, not actual empirical data**.

> [!CAUTION]
>
> ### Why Prefer Apparent Grain Size Measures Over Unfolded 3D Grain Size Distributions in Paleopiezometry?
>
> While one might be tempted to use a stereological method to estimate the midpoint of the modal interval or another unidimensional parameter based on the calculated grain size distribution, we argue that this approach offers no advantages and comes with serious disadvantages.
>
> The rationale behind this is that 3D grain size distributions are estimated using a stereological model. This means the accuracy of the estimates is dependent not only on measurement errors but also on the robustness of the model itself. Unfortunately, stereological methods are based on weak geometric assumptions, and their results will always be, at best, approximate. This implies that the precision and accuracy of average values estimated from 3D size distributions will be **significantly inferior** compared to those based on the original distribution of grain profiles. The latter, although estimating an apparent grain size, relies on real data rather than a model.
>
> **Recommendation**. In summary, it’s advisable to use stereological methods only when there’s a need to estimate the volume occupied by a specific grain size fraction, to investigate the shape of the true grain size distribution. or if you really need to use an average based on actual grain sizes (e.g. when you need to compare the average grain size calculated with a tomographic technique and from a section). Otherwise, for better precision and accuracy, opt for averages based on the apparent grain size distribution.



## The two-step method

> **What is it?**
> The Two-Step Method is a stereological technique used to approximate the actual three-dimensional grain size distribution. This method is **distribution-dependent**, meaning it assumes that the grain sizes follow a lognormal distribution. The method fits a lognormal distribution on top of the output from the Saltykov method, hence the name "Two-Step Method".
>
> **What do I use it for?**
> The Two-Step Method is primarily used to estimate the lognormal distribution of grain sizes, which includes determining the shape and location of the distribution. Additionally, it can be utilized to estimate the volume fraction of a specific range of grain sizes.
>
> **What are its limitations?**
> - **Distribution Dependency**. The method assumes a lognormal distribution for grain sizes, which might not accurately represent certain materials.
> - **Inherited Limitations from Saltykov**. The method is partially based on the Saltykov method and therefore inherits some of its limitations. The method however do not require to define a specific number of classes. 

TODO

> [!NOTE]
> **Understanding MSD Value and its Purpose**
> MSD, or _Multiplicative Standard Deviation_, is a parameter that characterizes the shape of a grain size distribution using a single value, under the assumption that the distribution follows a lognormal pattern. In simpler terms, the MSD value provides a measure of the asymmetry or skewness of the grain size distribution.
> **Shape Characterization**. An MSD value equal to one corresponds to a normal (Gaussian) distribution, while values greater than one indicate log-normal distributions with varying degrees of asymmetry (Figure a).
> **Scale-Independent Comparison**. The advantage of this approach is that a single parameter, the MSD, can define the shape of the grain size distribution independently of its scale (Figure b). This makes it very convenient for comparing the shape of two or more grain size distributions.
>
> ![Figura](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/MSD_value.png)
> **Figure**. Probability density functions of selected lognormal distributions taken from [Lopez-Sanchez and Llana-Fúnez (2016)](http://www.sciencedirect.com/science/article/pii/S0191814116301778). (a) Lognormal distributions with different MSD values (shapes) and the same median/geometric mean (4). (b) Lognormal distributions with the same shape corresponding to an MSD value (1.5) and different medians/geometric means (note that different medians/geometric means imply different scales in the horizontal and vertical directions).




> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

