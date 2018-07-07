*last update 2018/07/06*

Requirements
-------------

GrainSizeTools script requires [Python][1] 3.5+ or higher and the Python scientific libraries [*Numpy*][2], [*Scipy*][3], [*Pandas*][9] and [*Matplotlib*][4]. We recommend installing the [Anaconda][5] or the [Enthought Canopy][6] distributions. Both distributions include all the required the scientific packages plus scientific-oriented integrated development systems. In case you have space problems in your hard disk, there is a distribution named [miniconda][7] that only installs the packages you actually need.

The approach of the script is based on the estimation of the areas of the grain profiles obtained from thin sections. It is therefore necessary to measure them in advance and save the results in a txt/csv/xlsx file. For this task, we highly encourage you to use the [*ImageJ*](http://rsbweb.nih.gov/ij/) application or one of their different flavours (see [here](http://fiji.sc/ImageJ)). ImageJ-type applications are public-domain image processing programs widely used for scientific research that runs on Windows, macOS, and Linux platforms. The documentation contains a quick tutorial on how to measure the areas of the grain profiles with ImageJ, see the *Table of Contents*. The combined use of **ImageJ** and **GrainSizeTools script** is intended to ensure that all data processing steps are done through free and open-source programs/scripts that run under any operating system. If you are dealing with EBSD data, we encourage you to use the [MTEX toolbox](https://mtex-toolbox.github.io/) for grain reconstruction and the [export2file script](https://github.com/marcoalopez/export2file) for exporting the data (a tutorial on this will be available soon).



[next section](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Scope.md)  
[table of contents](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/tableOfContents.md)



[1]: https://www.python.org/

[2]: http://www.numpy.org/

[3]: http://www.scipy.org/

[4]: http://matplotlib.org/

[5]: https://www.anaconda.com/download/

[6]: https://www.enthought.com/products/canopy/

[7]: http://conda.pydata.org/miniconda.html

[8]: http://rsbweb.nih.gov/ij/

[9]: http://pandas.pydata.org
