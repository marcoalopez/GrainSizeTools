Requirements
-------------

The scripts requires [Python][1] 2.7.x or 3.4.x and the scientific libraries [*Numpy*][2], [*Scipy*][3] and [*Matplotlib*][4] installed in the system. We recommend installing the [Continuum Anaconda][5] or the [Enthought Canopy][6] (maybe more easy-friendly for newbies) distributions, since they are free (at least the basic versions) and provide the most popular Python scientific packages including those named above. Both packages also provide academic free licenses for more advanced versions. In case you have space problems, there is a distribution named [miniconda][7] that only installs the packages that you choose/need.

Since the approach of the script is based on the estimation of the grain sectional areas from thin sections, it is necessary to measure in advance the areas of the grains and store them in a text file to use the script and derive the grain size. To measure the grain sectional areas, we highly encourage you to use the [*ImageJ*][8] program or similar since there are public-domain java-based image processing programs widely used for scientific research that runs on Windows, Mac OS X and Linux platforms. The aim of this text is not to describe how to measure the grain areas with the *ImageJ* application but how to treat the data obtained from these applications. If you are not familiarized with the *ImageJ* application don't worry, there are many tutorials on the web. Just search the terms *'ImageJ'* and *'areas'* in your favorite search engine and you will find your answers.

[1]: https://www.python.org/
[2]: http://www.numpy.org/
[3]: http://www.scipy.org/
[4]: http://matplotlib.org/
[5]: https://store.continuum.io/cshop/anaconda/
[6]: https://www.enthought.com/products/canopy/
[7]: http://conda.pydata.org/miniconda.html
[8]: http://rsbweb.nih.gov/ij/