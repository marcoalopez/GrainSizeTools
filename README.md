![](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/new_header.png)

*This project is maintained by [Marco A. Lopez-Sanchez](https://marcoalopez.github.io/) - Last update (website): 2018/07/09*  

**GrainSizeTools** is a free, open-source, cross-platform script written in [Python](https://www.python.org/) that provides several tools to estimate the average grain size in polycrystalline materials, characterize the nature of the distribution of grain sizes (apparent and approximate 3D grain size distributions via stereology), and estimate the differential stress via paleopizometers. The script requires as the input the areas of the grain profiles measured grain-by-grain on planar sections and **does not require previous experience with Python programming language** (see documentation below and [FAQ](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md)). For users with coding skills, the script is organized in a modular way facilitating its reuse and code extension.

**IMPORTANT!: v2.0 released (2018/07/07). It includes new features and changes that make it incompatible with previous versions. The new version is only compatible with Python 3.5 or higher versions. PLEASE UPDATE** 


## Features at a glance

- Extract data automatically from tabular-like files including txt, csv, or xls/slxs formats.
- Estimate different statistical descriptors to characterize grain size distributions. Average grain size measures include the mean, RMS mean, median, area-weighted mean, and frequency peak using a Gaussian Kernel Density Estimator. Grain size scales can be in linear, logarithmic, or square root.
- Estimate normalized grain size distributions to compare between different grain size populations.
- Estimate differential stress via paleopiezometers including multiple piezometric relations for quartz, olivine, calcite, and feldspar.
- Estimate robust confidence intervals using the student's t-distribution
- Include several algorithms to estimate the optimal bin size of histograms and the optimal bandwidth of the Gaussian KDE based on population features.
- Approximate the actual 3D grain size distribution from data collected in plane sections (2D data) using the Saltykov method. This includes estimating the volume of a particular grain size fraction.
- Approximate the lognormal shape of the 3D grain size distribution via the two-step method and characterize the shape using a single parameter (the MSD - *Multiplicative Standard Deviation*) .
- Ready-to-publish plots in bitmap or vector format (see screenshots below for examples).

## Download

You can download the script at the following sites:  
https://github.com/marcoalopez/GrainSizeTools/releases  
http://figshare.com/articles/GrainSizeTools_script/1383130  
https://sourceforge.net/projects/grainsizetools/

[View project on GitHub](https://github.com/marcoalopez/GrainSizeTools)

## Documentation

* [Requirements](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Requirements.md)
* [Scope](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Scope.md)
* [Getting started: A step-by-step tutorial](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md)
    - [Open and running the script](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md#open-and-running-the-script)
    - [A brief note on the organization of the script](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md#a-brief-note-on-the-organization-of-the-script)
    - [Loading and extracting the data](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md#loading-and-extracting-the-data)
    - [Estimate equivalent circular diameters using the areas of the grain profiles](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md#estimate-the-equivalent-circular-diameters-from-the-areas-of-the-grain-profiles)
    - [Estimate different average grain size values and characterize the apparent grain size distribution](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md#estimate-different-average-grain-size-values-and-characterize-the-apparent-grain-size-distribution)
      - [Normalized apparent grain size distributions](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md#normalized-apparent-grain-size-distributions)
    - [Differential stress estimation using piezometric relations (paleopiezometry)](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md#differential-stress-estimation-using-piezometric-relations-paleopiezometry)
    - [Estimating a robust confidence interval](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md#estimating-a-robust-confidence-interval)
    - [Approximate the actual 3D grain size distribution and estimate the volume of a specific grain size fraction using the Saltykov method](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md#approximate-the-actual-3d-grain-size-distribution-and-estimate-the-volume-of-a-specific-grain-size-fraction-using-the-saltykov-method)
    - [Approximate the lognormal shape of the actual grain size distribution using the two-step method](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md#approximate-the-lognormal-shape-of-the-actual-grain-size-distribution-using-the-two-step-method)
    - [Comparing different grain size populations using box plots](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md#comparing-different-grain-size-populations-using-box-plots)
    - [Merging datasets](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/brief_tutorial.md#merging-datasets)
* [How to measure the areas of the grain profiles with ImageJ](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/imageJ_tutorial.md)
* [How to reconstruct the grains from SEM-EBSD data using the MTEX toolbox](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/ebsd_mtex_tutorial.md)
* [References](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/references.md)
* [FAQs](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/FAQ.md)

## Screenshots

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/diff_scales_tre.png?raw=true)  
*Estimate the distribution of apparent grain size using linear, logarithmic, or square root scales.*

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/area_weighted.png?raw=true)  
*Estimate the area-weighted apparent grain size distribution*

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/norm_median.png?raw=true)  
*Estimate normalized apparent grain size distributions using the mean, the median, or the frequency peak as normalized factor. In the example above normalized to median =1*

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/figure_2.png?raw=true)  
*Estimate of the actual (3D) grain size distribution and volume of a particular grain size fraction using the Saltykov method*

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/2step.png?raw=true)   
*Estimate of the shape of the grain size distribution using the two-step method*

![](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/readme05.png)  
*Boxplots comparing different unimodal grain size distributions*

## Citation guidelines

In case you need references, the following are available:

***Script reference***   
Lopez-Sanchez, Marco A. (2018): GrainSizeTools script. figshare. http://dx.doi.org/10.6084/m9.figshare.1383130

***Frequency peak apparent grain size based on Gaussian kernel density estimator***  
Lopez-Sanchez MA and Llana-Fúnez S (2015) An evaluation of different measures of dynamically recrystallized grain size for paleopiezometry or paleowattmetry studies. *Solid Earth* 6, 475-495. doi:[10.5194/se-6-475-2015](http://dx.doi.org/10.5194/se-6-475-2015)

***Two-step method***  
Lopez-Sanchez MA and Llana-Fúnez (2016) An extension of the Saltykov method to quantify 3D grain size distributions in mylonites. *Journal of Structural Geology*, 93, 149-161. doi:[10.1016/j.jsg.2016.10.008](http://dx.doi.org/10.1016/j.jsg.2016.10.008).

***Saltykov method***  
The procedure implemented in the GrainSizeTools script is partially based on general formulation developed by Sahagian and Proussevitch (1998) *J. Volcanol. Geotherm. Res.* 84, 173–196. [http://dx.doi.org/10.1016/S0377-0273(98)00043-2](http://dx.doi.org/10.1016/S0377-0273(98)00043-2) and is described in the Appendix A in Lopez-Sanchez and Llana-Fúnez (2016) http://dx.doi.org/10.5194/se-6-475-2015

## License

GrainSizeTools script is licensed under the [Apache License, Version 2.0 (the "License")](http://www.apache.org/licenses/LICENSE-2.0)

The documentation of GrainSizeTools script is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).  

# 
*Copyright © 2018 Marco A. Lopez-Sanchez*  

*Information presented on this website and the documentation of the script is provided without any express or implied warranty and may include technical inaccuracies or typing errors; the author reserve the right to modify or enhance the content of this website as well as the documentation of the script at any time without previous notice. This webpage and the documentation is not liable for the content of external links.*  

*Hosted on GitHub Pages — This website was created with [Typora](https://typora.io/)*