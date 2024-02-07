![](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/new_header.webp)

_Maintained by [Marco A. Lopez-Sanchez](https://marcoalopez.github.io/) - This website was last modified: 2024/02/07_

[GrainSizeTools](https://doi.org/10.21105/joss.00863) is a free, open-source, cross-platform script written in [Python](https://www.python.org/) that provides tools for (1) describing and visualizing grain size populations, (2) estimating differential stress for different mineral phases using paleopizometers and (3) applying stereological methods to approximate the true grain size distribution from 2D sections. The script **does not require any previous experience with the Python programming language** (see the documentation below and [FAQ](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md)). For users with programming skills, the script is organized in a modular (functional) way to facilitate reuse and code extension.

**Latest release: v3.0.2**  
**Date: 2020/12/31**  
See notes at https://github.com/marcoalopez/GrainSizeTools/releases/tag/v3.0.2


## Features at a glance

- Import and manipulate tabular data sets including text, CSV, or Excel formats.

- Fully automated descriptive statistics of grain size populations including:

  - Multiple averages (arithmetic and geometric means, median, and frequency peak ("mode") via Gaussian Kernel Density Estimator)
  - Estimation of robust confidence intervals (including some specific methods for lognormal populations such as the modified Cox or the GCI method)
  - Measures of dispersion and population shape
  - Normality and lognormality tests

- Estimation of differential stress using palaeopiezometers. Includes several piezometric relations for quartz, olivine, calcite and feldspar (more to come!)

- Ready-to-publish plots in bitmap or vector format (see screenshots below), including:

  - Histograms and kernel density estimates
  - Area or volume-weighted plots
  - Normalized plots
  - Quantile-quantile plots, and more

- Stereology methods (approximating the true 3D grain size distribution from data collected in flat sections):

  - Saltykov method
  - Two-step method (log-normal fitting, shape characterization)

## Download

You can download the script at the following sites:  
https://github.com/marcoalopez/GrainSizeTools/releases  (primary source)  
http://figshare.com/articles/GrainSizeTools_script/1383130  
https://sourceforge.net/projects/grainsizetools/

[View project on GitHub](https://github.com/marcoalopez/GrainSizeTools)

## Documentation

* [FAQs](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md)
* [Getting started: first steps using the GrainSizeTools script](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_first_steps.md)
* [Describing the population of grain sizes](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_describe.md)
* [The plot module: visualizing grain size distributions](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_Plot_module.md)
* [The stereology module](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/stereology_module.md) 🚨 **Recently updated!**
* [The paleopiezometry module](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_Paleopizometry.md)

**Supplementary material**

* [How to measure the areas of the grain profiles with ImageJ](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/imageJ_tutorial.md)

## Screenshots (v3.0+)

![](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/screenshots-01.webp)

## Citation guidelines

If you have used the script, please consider citing the following paper:

> Lopez-Sanchez, Marco A. (2018). GrainSizeTools: a Python script for grain size analysis and paleopiezometry based on grain size. *Journal of Open Source Software*, 3(30), 863, https://doi.org/10.21105/joss.00863

By citing this paper, you are giving proper credit to the author and acknowledging his work.

## License

GrainSizeTools script is licensed under the [Apache License, Version 2.0 (the "License")](http://www.apache.org/licenses/LICENSE-2.0)

The documentation of GrainSizeTools script is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). 

## Community guidelines

The GitHub site where the project is hosted offers several options (you'll need a GitHub account, it's free!)::

- Open a [discussion](https://github.com/marcoalopez/GrainSizeTools/discussions): This is a place to:
  - Ask questions you are wondering about.
  - Requests for specific features or share ideas.
  - Interact with the developers.
- Open an [issue](https://github.com/marcoalopez/GrainSizeTools/issues): This is a place to report or track bugs.
- Make a [pull request](https://github.com/marcoalopez/GrainSizeTools/pulls): You have modified, corrected or added a feature to one of the notebooks and send it to one of the developers to review it and add it to the main page.

---
*Copyright © 2017-2024 Marco A. Lopez-Sanchez*  

> [!WARNING]
> The information on this website and in the script documentation is provided without any warranty of any kind, either expressed or implied, and may include technical inaccuracies or typographical errors; the author reserves the right to make changes or improvements to the content of this website and the script documentation at any time without notice. This website and its documentation are not responsible for the content of external links. 

*Hosted on GitHub Pages — This website was created with [Typora](https://typora.io/)*

![](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/footer.webp)