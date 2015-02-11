# GrainSizeTools

*GrainSizeTools* is a free cross-platform script written in [Julia][1] that provides a robust method to obtain a single measure of dynamically recrystallized grain size in deformed rocks. There is no need of prior knowledge of Julia language to use the script and get the results. The script only requires the previous measurement of the grain sectional areas from a thin section. The aim of the script is to use this value in paleopiezometry and paleowattometry studies. A full paper describing the method applied by the script can be found here: http://www.solid-earth-discuss.net/6/3141/2014/sed-6-3141-2014.html . At the moment there is only a version of the script implemented in [Python][2], but it is planned to release a Julia version soon. Thank you for your patience.

You can find the Python version of the script here: https://sourceforge.net/projects/grainsizetools/
and a brief tutorial on the use of the script here: http://sourceforge.net/p/grainsizetools/wiki/Home/

### **Features**

- The script is free, open-source and cross-platform
- It allows to load text files -txt or csv- with the sectional areas of the grains
- It allows to calculate the apparent diameters of the grains from the sectional areas via the equivalent circular diameter
- It allows to correct the diameters calculated by adding the perimeter of the grains
- It returns the mean, median and area-weighted grain size of the apparent population of grain sizes.
- It returns the peak of the frequency grain size via the Gaussian kernel density estimator
- It produces ready-to-publish number- and area-weighted grain size plots, allowing to save the graphical - -output as a bitmap or vector images
- It returns the modal intervals and their central values in the number- and area-weighted approaches
- The script implements several algorithms to estimate the optimal bin size of the histogram and the bandwidth of the Gaussian KDE
- The script is organized in a modular way using Python functions, which facilitates to modify, reuse or extend the code.

 
[1]: http://julialang.org/
[2]: https://www.python.org/
