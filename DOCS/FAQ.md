Frequently Asked Questions
-------------

***Who this script is for?***  
This script is targeted at anyone who wants to: i) obtain a set of single 1D measures of grain size to estimate the magnitude of differential stress (or rate of mechanical work) in dynamically recrystallized rocks and ii) to estimate the actual 3D distribution of grain sizes from the population of apparent grain sizes measured in thin sections. These features include the estimation of the volume occupied by a particular grain size fraction and the estimation of the parameters that best describe the population of grain sizes (assuming that the distribution of grain sizes follows a lognormal distribution). The stereolocal methods implemented within the script assume that grains have near-equant or not to far from near-equant shapes, which seems acceptable most of the time for some of the most common dynamically recrystallized non-tabular grains in crustal and mantle shear zones such as olivine, quartz, feldspar, calcite or even ice when bulging (BLG) or sub-grain rotation (SGR) are the main recrystallization processes. For studies involving objects geometrically more complex than near-equant objects, we recommend other approaches such as those implemented in the *CSDCorrections* (Higgins 2000). See the references section for details.

***Does the script work with Python 2.7.x and 3.x versions?***  
The code has been written to run on both versions. If you run into any problem using the script with Python 3.4.x or also 2.7.x or above please let me know (see an email address here: http://marcoalopez.github.io/ ). Feedback from users is always welcome and important to develop a better script.

***Why the sum of all frequencies in the histograms is not equal to one?***  
This is because the script normalized the frequencies of the different classes so that the integral over the range is one. In other words, once the frequencies are normalized to one the values obtained are divided by the estimated bin size. This means that the sum of the histogram values will not be equal to one unless the bin size is one. We have chosen this normalization method because is useful to compare the same distribution using different bin sizes (or number of classes) and is required to properly apply the two-step method.

[table of contents](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/tableOfContents.md)
