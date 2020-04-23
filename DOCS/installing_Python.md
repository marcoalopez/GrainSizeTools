*last update 2020/04/25*

Installing Python for data science
-------------

### GrainSizeTools requirements

GrainSizeTools script requires [Python][1] 3.5+ or higher and the Python scientific libraries [*Numpy*][2], [*Scipy*][3], [*Pandas*][9] and [*Matplotlib*][4].

- Python (>= 3.6)
- Numpy (>=1.11)
- Scipy (>=0.13)
- Pandas (>=0.16)
- Matplotlib (>= 2.0.2)



### Installing Anaconda

If you do not have any experience with Python, I recommend that you download and install the [Anaconda Python distribution][5] with Python 3.x version, as it includes all the required the scientific packages plus several scientific-oriented integrated development systems (requires > 5 GB disk space). In case you have a limited space in your hard disk, there is a distribution named [miniconda][7] that only installs the packages you actually need. For both cases you have versions for Windows, MacOS and Linux

Anaconda: https://www.anaconda.com/distribution/ 

Miniconda: http://conda.pydata.org/miniconda.html 

Once Anaconda is installed on your system, launch the Anaconda Navigator you will see that you have installed **Spyder** and **Jupyter lab**, 



### Philosophy

he GrainSizeTools script was designed to deal with microscopic images but to analyse and visualize grain size populations and estimate stresses via paleopiezometers. **It is therefore necessary to measure the diameters, the sectional areas or the volumes of the grains in advance and store them in a txt/csv/excel file**. For this task, we highly encourage you to use the [*ImageJ*](http://rsbweb.nih.gov/ij/) application or one of their different flavours (see [here](http://fiji.sc/ImageJ)). ImageJ-type applications are public-domain image processing programs widely used for scientific research that runs on Windows, macOS, and Linux platforms. The documentation contains a quick tutorial on how to measure the areas of the grain profiles with ImageJ, see *Table of Contents*. The combined use of **ImageJ** and **GrainSizeTools script** is intended to ensure that all data processing steps are done through free and open-source programs/scripts that run under any operating system.

If you are dealing with EBSD data instead, we encourage you to use the [MTEX toolbox](https://mtex-toolbox.github.io/) for grain reconstruction and the [export2file script](https://github.com/marcoalopez/export2file) for exporting the data (a tutorial on this will be available soon).