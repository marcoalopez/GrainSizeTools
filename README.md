![](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/new_header.webp)

*Maintained by [Marco A. Lopez-Sanchez](https://marcoalopez.github.io/) - This website was last modified: 2020/04/16*

[GrainSizeTools](https://doi.org/10.21105/joss.00863) is a free, open-source, cross-platform script written in [Python](https://www.python.org/) that provides several tools for (1) Characterizing and visualizing grain size populations, (2) estimating differential stress for different mineral phases via paleopizometers and (3) apply stereology methods to approximate the actual distribution (3D) of grain size from sections. The script requires as the input the diameters of the grain profiles measured grain-by-grain on planar sections and **does not require previous experience with Python programming language** (see documentation below and [FAQ](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md)). For users with coding skills, the script is organized in a modular (functional) way facilitating the reuse and code extension.

**NEW!**
**Latest (beta) release: v3.0beta3** (still in development)  
**Date: 2020/04/16**  
See: https://github.com/marcoalopez/GrainSizeTools/releases/tag/v3.0-beta.3

**Latest stable release: v2.0.4**  
**Date: 2020/04/09**  


## Features at a glance

- Import and manipulate tabular-like files including txt, csv, or excel formats.
- Estimate different statistical descriptors to characterize grain size distributions. Average grain size measures include the arithmetic, geometric, RMS and area-weighted means, median, and frequency peak ("mode") via Gaussian Kernel Density Estimator. Grain size can be represented in linear, logarithmic, and square root scales.
- Estimate normalized apparent grain size distributions to compare between different grain size populations.
- Estimate differential stress via paleopiezometers including multiple piezometric relations for quartz, olivine, calcite, and feldspar (others planned!)
- Estimate robust confidence intervals using the student's *t*-Distribution
- Include several algorithms to estimate the optimal bin size of histograms and the optimal bandwidth of the Gaussian KDE based on population features.
- Approximate the actual 3D grain size distribution from data collected in plane sections (2D data) using the Saltykov method. This includes estimating the volume of a particular grain size fraction.
- Approximate the lognormal shape of the 3D grain size distribution via the two-step method and characterize the shape using a single parameter (the MSD - *Multiplicative Standard Deviation*) .
- Check lognormality using quantile-quantile plots and Shapiro-Wilk tests (**new in v3.0!**)
- Ready-to-publish plots in bitmap or vector format (see screenshots below for examples).

## Download

You can download the script at the following sites:  
https://github.com/marcoalopez/GrainSizeTools/releases  
http://figshare.com/articles/GrainSizeTools_script/1383130  
https://sourceforge.net/projects/grainsizetools/

[View project on GitHub](https://github.com/marcoalopez/GrainSizeTools)

## Documentation

* [FAQs](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md)
* [Requirements & Development](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Requirements.md)
* [Scope](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Scope.md)
* [Getting started: A step-by-step tutorial](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md) (for version 3.0beta see [here](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/getting_started.md))
* [How to measure the areas of the grain profiles with ImageJ](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/imageJ_tutorial.md)
* [How to reconstruct the grains from SEM-EBSD data using the MTEX toolbox (available soon!)](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/ebsd_mtex_tutorial.md)
* [References](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/references.md)

## Screenshots (v3.0+)

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/summarize_output.png?raw=true)

*Comprehensive description of grain size distributions*

  

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_distribution.png?raw=true)

*Apparent (2D) or actual (3D) grain size distribution using histograms and kernel density estimates*

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_qqplot.png?raw=true)  

*Quantile-quantile plots*

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_area_weighted.png?raw=true)  
*Area-weighted grain size distribution*

![](![new_normalized.png](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_normalized.png?raw=true)  
*Normalized apparent grain size distributions*

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/figure_2.png?raw=true)  
*Estimate of the actual (3D) grain size distribution and volume of a particular grain size fraction using the Saltykov method*

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/2step.png?raw=true)   
*Estimate of the shape of the grain size distribution using the two-step method*

![](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/readme05.png)  
*Boxplots comparing different unimodal grain size distributions*

## Citation guidelines

***Script reference***  ![DOI](http://joss.theoj.org/papers/10.21105/joss.00863/status.svg)  
Lopez-Sanchez, Marco A. (2018). GrainSizeTools: a Python script for grain size analysis and paleopiezometry based on grain size. *Journal of Open Source Software*, 3(30), 863, https://doi.org/10.21105/joss.00863

## License

GrainSizeTools script is licensed under the [Apache License, Version 2.0 (the "License")](http://www.apache.org/licenses/LICENSE-2.0)

The documentation of GrainSizeTools script is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). 

## Community guidelines

- *Did you find a bug in the code or an error in the documentation?* Let me know by opening an [issue](https://github.com/marcoalopez/GrainSizeTools/issues).

- *Do you want to contribute with new ideas or do you miss a feature?* Let me know by sending me an email (see [here](https://github.com/marcoalopez )), or better open an [pull request](https://github.com/marcoalopez/GrainSizeTools/pulls) with the label ``enhancement`` and I'll see what I can do
- *Do you want to develop your own code based on the GrainSizeTools script?* Go ahead, clone the project and develop!



---
*Copyright © 2020 Marco A. Lopez-Sanchez*  

*Information presented on this website and the documentation of the script is provided without any express or implied warranty and may include technical inaccuracies or typing errors; the author reserve the right to modify or enhance the content of this website as well as the documentation of the script at any time without previous notice. This webpage and the documentation is not liable for the content of external links.*  

*Hosted on GitHub Pages — This website was created with [Typora](https://typora.io/)*

![](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/footer.webp)