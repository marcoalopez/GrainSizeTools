![](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/new_header.webp)

*Maintained by [Marco A. Lopez-Sanchez](https://marcoalopez.github.io/) - This website was last modified: 2020/05/08*

[GrainSizeTools](https://doi.org/10.21105/joss.00863) is a free, open-source, cross-platform script written in [Python](https://www.python.org/) that provides several tools for (1) Describing and visualizing grain size populations, (2) estimating differential stress for different mineral phases via paleopizometers and (3) apply stereology methods to approximate the actual distribution (3D) of grain size from sections. The script **does not require previous experience with Python programming language** (see documentation below and [FAQ](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md)). For users with coding skills, the script is organized in a modular (functional) way facilitating the reuse and code extension.

**Latest release: v3.0RC0**  
**Date: 2020/05/04**  
See: https://github.com/marcoalopez/GrainSizeTools/releases/tag/v3.0RC

> **Important note**: The script has been completely reorganized in v3.x, including new modules and features. **Its use is no longer compatible with previous versions (v2.x).** Check the new documentation for use.


## Features at a glance

- Import and manipulate tabular-like datasets including txt, csv, or excel formats.

- Full automatic descriptive statistics of grain size populations including:

  - Several averages (arithmetic and geometric means, median, and frequency peak ("mode") via Gaussian Kernel Density Estimator)
  - Estimation of robust confidence intervals (including some specific methods for lognormal populations such as the modified Cox or the GCI method)
  - Measures of dispersion and shape of the population
  - Normality and lognormality test

- Estimate differential stress using paleopiezometers. It includes multiple piezometric relations for quartz, olivine, calcite, and feldspar (others planned!)

- Ready-to-publish plots in bitmap or vector format (see screenshots below), including:

  - Histograms and kernel density estimates
  - Area- or volume-weighted plots
  - Normalized plots
  - Quantile-quantile plots, and more

- Stereology methods (approximate the actual 3D grain size distribution from data collected in plane sections):

  - Saltykov method
  - Two-step method (lognormal fitting, shape characterization)

## Download

You can download the script at the following sites:  
https://github.com/marcoalopez/GrainSizeTools/releases  
http://figshare.com/articles/GrainSizeTools_script/1383130  
https://sourceforge.net/projects/grainsizetools/

[View project on GitHub](https://github.com/marcoalopez/GrainSizeTools)

## Documentation

* [FAQs](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md)
* [Getting started: first steps using the GrainSizeTools script](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_first_steps.md)
* [Describing the population of grain sizes](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_describe.md)
* [The plot module: visualizing grain size distributions](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_Plot_module.md)
* [The paleopiezometry module](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_Paleopizometry.md)
* [The stereology module](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_Stereology_module.md)

***Others***

* [Documentation for old versions (v2.0.4)](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md)
* [How to measure the areas of the grain profiles with ImageJ](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/imageJ_tutorial.md)
* [How to reconstruct the grains from SEM-EBSD data using the MTEX toolbox (available soon!)](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/ebsd_mtex_tutorial.md)

## Screenshots (v3.0+)

![](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/screenshots-01.webp)

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