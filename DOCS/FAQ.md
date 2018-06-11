Frequently Asked Questions
-------------

***Who is this script for?***  
This script is targeted at anyone who wants to: i) visualize the grain size distribution, ii) obtain a set of apparent grain size measures to estimate the magnitude of differential stress (or rate of mechanical work) in dynamically recrystallized rocks, and iii) estimate the actual (3D) distribution of grain sizes from thin sections using stereological methods. The latter includes an estimate of the volume occupied by a particular grain size fraction and a parameter to characterize the shape of the population of grain sizes (assuming that the distribution of grain sizes follows a lognormal distribution). The stereological methods assume that grains have equant or near-equant (AR < 2.0) shapes, which mostly include all recrystallized grains produced during static and dynamically recrystallization. For igneous studies involving tabular grains far from near-equant objects, we recommend other approaches such as those implemented in the *CSDCorrections* software (Higgins 2000). See the references list section for details.

***Why use apparent grain size measures instead of measures estimated from unfolded 3D grain size distributions in paleopiezometry studies?***  
One may be tempted to use a stereological method to estimate the midpoint of the modal interval or any other unidimensional parameter based on the actual grain size distribution rather than using the mean, median, or frequency peak of the apparent grain size distribution. We think that there is no advantage in doing this but serious drawbacks. The rationale behind this is that 3D grain size distributions are estimated using a stereological model and, hence, the accuracy of the estimates depends not only in the introduction of errors during measuring but also on the robustness of the model. Unfortunately, stereological methods are built on "weak" geometric assumptions and the results will always be, at best, [only approximate](http://doi.wiley.com/10.1111/j.1365-2818.1983.tb04255.x). This means that the precision of the estimated 3D size distribution is **much poorer** than the precision of the original distribution of grain profiles since the latter is based on real data. To sum up, use stereological methods only when you need to estimate the volume occupied by a particular grain size fraction or investigating the shape of the actual grain size distribution, otherwise use estimates based on the apparent grain size distribution.

***What measure of central tendency (mean, median, peak/mode) do I have to use?***

This depends on the features of the grain size distribution. In the case of unimodal distributions the following rule of thumb should be considered:

- use **mean and standard deviation (SD)** when your **distribution is normal-like or moderate-tailed**. In such cases, the position of the mean, median and frequency peak ("mode") should be fairly similar. This is expected to occur when using logarithmic or square-root scales.
- use **median and interquartile (or interprecentil) range** when your **distribution is skewed (non-normal)**. In such cases, the position of the mean, median and frequency peak should be well differentiated.
- use the **location of the frequency peak (KDE peak grain size)** when grain size in different specimens was measured with very different conditions (e.g. different resolutions, cut-offs, etc.) or when the distribution show complex or multimodal patterns (in that case only for comparative purposes). See more details in the [Scope](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Scope.md) section.

Last, as a rule of thumb and for future comparatives always report all of them.

***What is an MSD value? What is it used for?***  
MSD stands for *Multiplicative Standard Deviation* and it is a parameter that allows to define the shape of the grain size distribution using a single value assuming that it follows a lognormal distribution. In plain language, the MSD value gives a measure of the asymmetry (or skewness) of the grain size distribution. For example, an MSD value equal to one corresponds to a normal (Gaussian) distribution and values greater than one with log-normal distributions of different shapes, being the higher the MSD value the greater the asymmetry of the distribution (Figure a). The advantage of this approach is that by using a single parameter we can define the shape of the grain size distribution independently of its scale (Fig. b), which is very convenient for comparing the shape of two or more grain size distributions.

![Figura](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/MSD_value.png)

*Probability density functions of selected lognormal distributions taken from [Lopez-Sanchez and Llana-Fúnez (2016)](http://www.sciencedirect.com/science/article/pii/S0191814116301778). (a) Lognormal distributions with different MSD values (shapes) and the same median (4). (b) Lognormal distributions with the same shape corresponding to an MSD value (1.5) and different medians (note that different medians imply different scales in the horizontal and vertical directions).*

***Why the grain size distribution plots produced by the GST script and the classic CSD charts do not use the same units on the y axis?***  
As you may noticed classic CSDs charts (Marsh, 1988) show in the vertical axis the logarithmic variation in population density or log(frequency) in mm<sup>-4</sup>, while the stereological methods put in the GrainSizeTools (GST) script returns plots with a linear frequency (per unit volume). This is due to the different aims of the CSDs and the plots returned by the GST script. Originally, CSDs were built for deriving two things in magmatic systems: i) nucleation rates and ii) crystal growth rates. In these systems, small grains are more abundant than the large ones and the increase in quantity is typically exponential. The use of the logarithm in the vertical axis helps to obtain a straight line with the slope being the negative inverse of the crystal growth times the time of crystallization. Further, the intercept of the line at grain size equal to zero allows estimating the nuclei population density. In recrystallized rocks, there is no grain size equal to zero and we usually unknown the crystallization time, so the use of the CSDs are not optimal. Furthermore, the use of the logarithm in the vertical axis has two main disadvantages for microstructural studies: (i) it obscures the reading of the volume of a particular grain fraction, a common target in microtectonic studies, and (ii) it prevents the easy identification of the features of grain size distribution, which is relevant for applying the two-step method.

***Why the sum of all frequencies in the histograms is not equal to one?***  
This is because the script normalized the frequencies of the different classes so that the integral over the range is one. In other words, once the frequencies are normalized to one, the frequency values are divided by the bin size. This means that the sum of all frequency values will not be equal to one unless the bin size is one. We have chosen this normalization method because it allows comparing similar distributions using a different number of classes or bin size, and it is required to properly apply the two-step method.

***Is it necessary to specify the version of the script used in a publication? How can this be indicated?***  

Yes, it is always desirable to indicate the version of the script used. The rationale behind this is that codes may contain bugs and versioning allow to track them and correct the results of already published studies in case a bug is discovered later. The way to indicate the version is twofold:

- The  way we advise you to follow is by explicitly indicating the version in your manuscript as follows: "*...we used the GrainSizeTools script version 1.4.4...*" and then use the general citation in the reference list.

- The other way is by adding a termination in the form *.v plus a number* in the general DOI link. This is, instead of using the general reference of the script:

  Lopez-Sanchez, Marco A. (2018): GrainSizeTools script. figshare.

  https://doi.org/10.6084/m9.figshare.1383130

  You can modify the doi link as follows:

  Lopez-Sanchez, Marco A. (2017): GrainSizeTools script. figshare.

  https://doi.org/10.6084/m9.figshare.1383130.v15 (Note the termination *.v15*)

  To get the specific doi link, go to the script repository at https://figshare.com/articles/GrainSizeTools_script/1383130 , find the version you used in your study, and then click on "Cite" to obtain the full citation.

***Does the script work with Python 2.7.x and 3.x versions? Which version do I choose?***  
Despite both Python versions are not fully compatible, *GrainSizeTools script* has been written to run on both. As a rule of thumb, if you do not have previous experience with the Python language go with 3.x versions, which is the present and future of the language. Python 2.7.x versions are still maintained for legacy reasons, but keep in mind that their support [will be discontinued in 2020](https://pythonclock.org/). Also note that since version 1.3, the script is only tested by the maintainer using Python 3. 

***I get the results but not the plots when using the Spyder IDE***  
This issue is produced because the size of the figures returned by the script are too large to show them inside the console using the **inline** mode. To fix this go to the Spyder menu bar and in  ```Tools>Preferences>IPython console>Graphics``` find *Graphics backend* and select *Automatic* and then restart Spyder. An alternative without needing to restart Spyder type ```%matplotlib auto``` in the console

***Can I report bugs or submit ideas to improve the script?***  
Sure. If you have any problem using the script or found a bug please just let me know open an issue [here](https://github.com/marcoalopez/GrainSizeTools/issues) or drop me an email (my email address here: https://github.com/marcoalopez ). Feedback from users is always welcome and important to develop a better and reliable script. Lastly, you can also fork the project and develop your own based on the GST script since it is open source and free.

[table of contents](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/tableOfContents.md)
