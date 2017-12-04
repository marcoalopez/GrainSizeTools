Frequently Asked Questions
-------------

***Who is this script for?***  
This script is targeted at anyone who wants to: i) visualize grain size features, ii) obtain a set of apparent grain size measures to estimate the magnitude of differential stress (or rate of mechanical work) in dynamically recrystallized rocks, and iii) estimate features of the actual 3D distribution of grain sizes from the population of apparent grain sizes measured in thin sections. These features include the estimation of the volume occupied by a particular grain size fraction and the parameters that best describe the population of grain sizes (assuming that the distribution of grain sizes follows a lognormal distribution). The stereological methods implemented in the script assume that the grains have equant or near-equant (AR < 2.0) shapes, which includes most dynamically recrystallized grains typically found in crustal and mantle shear zones (olivine, quartz, feldspar or calcite) and ice when bulging (BLG) or sub-grain rotation (SGR) are the main recrystallization process. For studies involving tabular grains far from near-equant objects, we recommend other approaches such as those implemented in the *CSDCorrections* (Higgins 2000). See the references list section for details.

***Why use apparent grain size measures instead of measures estimated from the unfolded 3D grain size distribution in paleopiezometry studies?***  
One may be tempted to use a stereological method to estimate the midpoint of the modal interval or any other 1D parameter based on the actual grain size distribution rather than using the mean, median, or frequency peak of the apparent grain size distribution. We think that there is no advantage in doing this but serious drawbacks. The rationale behind this is that 3D grain size distributions are estimated using a stereological model and hence the accuracy of the estimates depends on the robustness of the model. Unfortunately, stereological methods are built on "weak" geometric assumptions and the results will always be, at best, only approximate. This means that the precision of the estimated 3D size distribution is **much poorer** than the precision of the original distribution of grain profiles since the latter is based on real data. In short, use stereological methods only when you need to estimate the volume occupied by a particular grain size fraction or investigating the shape of the actual grain size distributions, otherwise use measures based on the apparent grain size distribution.

***Why the grain size distribution plots produced by the GST script do not use the same units as the classic CSD charts?***  
As you may noticed classic CSDs charts (Marsh, 1988) show in the vertical axis the logarithmic variation in population density or log(frequency) in mm<sup>-4</sup>, while the stereological methods put in the GrainSizeTools (GST) script returns plots with a linear frequency (per unit volume). This is due to the different aims of the CSDs and the plots returned by the GST script. Originally, CSDs were built for deriving two things in magmatic systems: i) nucleation rates and ii) crystal growth rates. In these systems, small grains are more abundant than the large ones and the increase in quantity is typically exponential. The use of the logarithm in the vertical axis helps to obtain a straight line with the slope being the negative inverse of the crystal growth times the time of crystallization. Further, the intercept of the line at grain size equal to zero allows estimating the nuclei population density. In recrystallized rocks, there is no grain size equal to zero and we usually unknown the crystallization time, so the use of the CSDs are not optimal. Furthermore, the use of the logarithm in the vertical axis has two main disadvantages for microstructural studies: (i) it obscures the reading of the volume of a particular grain fraction, a common target in microtectonic studies, and (ii) it prevents the easy identification of the features of grain size distribution, which is relevant for applying the two-step method.

***Why the sum of all frequencies in the histograms is not equal to one?***  
This is because the script normalized the frequencies of the different classes so that the integral over the range is one. In other words, once the frequencies are normalized to one, the frequency values are divided by the bin size. This means that the sum of all frequency values will not be equal to one unless the bin size is one. We have chosen this normalization method because it allows comparing similar distributions using a different number of classes or bin size, and it is required to properly apply the two-step method.

***Is it necessary to specify the version of the script used in a publication? How can this be indicated?***  

Yes, it is always desirable to indicate the version of the script used. The rationale behind this is that codes may contain bugs and versioning allow to track this bugs and correct the results of already published studies in case a bug is discovered a posteriori. The way to indicate the version this is twofold:

- In the text by explicitly indicating it as follows: "*...we used the GrainSizeTools script version 1.4.1...*"

- In the reference list by adding a termination in the form *.v plus a number* in the general DOI link. For example:

  Lopez-Sanchez, Marco A. (2017): GrainSizeTools script. figshare.

  https://doi.org/10.6084/m9.figshare.1383130.v15 (Note the termination .v15)

  To know what termination to use go to the script repository at https://figshare.com/articles/GrainSizeTools_script/1383130 , find the version you used in your study, and then click on "Cite" to obtain the full citation.

***Does the script work with Python 2.7.x and 3.x versions? Which version do I choose?***  
Despite both Python versions are not fully compatible, *GrainSizeTools script* has been written to run on both. As a rule of thumb, if you do not have previous experience with the Python language go with 3.x versions, which is the present and future of the language. Python 2.7.x versions are still maintained for legacy reasons and they are widely used, but keep in mind that their support [will be discontinued in 2020](https://pythonclock.org/). Also note that since version 1.3, the script is only tested by the author using Python 3. 

***I get the results but not the plots when using the Spyder IDE***  
This issue is produced because the size of the figures returned by the script are too large to show them inside the console using the **inline** mode. To fix this go to the Spyder menu bar and in  ```Tools>Preferences>IPython console>Graphics``` find *Graphics backend* and select *Automatic*.

***Can I report bugs or submit ideas to improve the script?***  
Definitely. If you have any problem using the script please just let me know (see an email address here: http://marcoalopez.github.io/ ). Feedback from users is always welcome and important to develop a better script. Lastly, you can also create a fork of the project and develop your own tools based on the GST script since it is open source and free.

[table of contents](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/tableOfContents.md)
