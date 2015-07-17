![](https://github.com/marcoalopez/GrainSizeTools/blob/05837e74bb371c34c5257e869bfd363c069b9c4d/FIGURES/header_fig.png?raw=true)

[GrainSizeTools](https://sourceforge.net/projects/grainsizetools/) is a free open-source cross-platform script written in [Python][1] that provides a number of tools with the aim of characterizing the population of grain sizes in dynamically recrystallized mylonites. The script is suitable to use in paleopiezometry studies using different parameters as well as to derive the actual population of grain sizes from thin sections. The script requires the previous measurement of the grain sectional areas from a thin section. There is **no need** of previous knowledge of Python language to use the script and get the results (see the step-by-step manual). For advanced users, the script is organized in a modular way using Python functions, which facilitates to modify, reuse or extend the code if needed.

Features
-------------

- It allows to load text files -txt or csv- with the sectional areas of the grains
- It allows to calculate the apparent diameters of the grains from the sectional areas via the equivalent circular diameter
- It allows to correct the diameters calculated by adding the perimeter of the grains
- It returns the mean, the median and the area-weighted grain size of the apparent population of grain sizes.
- It returns the peak of the frequency grain size via the Gaussian kernel density estimator and the central values of the modal intervals in the number- and area-weighted approaches
- The script implements several algorithms to estimate the optimal bin size of the histogram and the bandwidth of the Gaussian KDE based on population features
- It estimates the actual 3D populations of grains from the population of apparent (2D) grain sizes using a variant of the Scheil-Schwartz-Saltykov method to unfold the 2D population. Similar to what the *StripStar* script does.
- It produces ready-to-publish plots, allowing to save the graphical output as a bitmap or vector images.

You can download the script [here](http://figshare.com/articles/GrainSizeTools_script/1383130)

You can get a manual in pdf [here](http://figshare.com/articles/GrainSizeTools_script_manual/1371025)

Table of contents
-------------

  * [Requirements](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Requirements.md)
  * [A brief tutorial on how to use the script]()
  * [Installation]()
    * [Running the script]()
    * [Organization of the script]()
    * [Using the script to estimate the grain size]()
    * [Obtaining a single value of grain size (paleopiezometry)]()
    * [Derive the actual 3D population of grains]()
      * [Other methods of interest]()
  * [Specifications of main functions in the GrainSizeTools script]()
    * [importdata]()
    * [calc_diameters]()
    * [find_grain_size]()
    * [derive3D]()
  * [References]()
  
Citation guidelines
-------------

###Software reference
Lopez-Sanchez, Marco A. (2015): GrainSizeTools script. figshare. http://dx.doi.org/10.6084/m9.figshare.1383130

###Technique reference: Peak grain size based on Gaussian KDE
Lopez-Sanchez MA and Llana-Fúnez S (2015) An evaluation of different measures of dynamically recrystallized grain size for paleopiezometry or paleowattometry studies. Solid Earth 6, 475-495. doi:[10.5194/se-6-475-2015](http://dx.doi.org/10.5194/se-6-475-2015)




 [1]: https://www.python.org/
