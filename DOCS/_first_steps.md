*last update 2020/04/26*

Installing Python for data science
-------------

GrainSizeTools script requires [Python](https://www.python.org/ ) 3.5+ or higher and the Python scientific libraries [*Numpy*](http://www.numpy.org/ ) [*Scipy*](http://www.scipy.org/ ), [*Pandas*](http://pandas.pydata.org ) and [*Matplotlib*](http://matplotlib.org/ ). If you have no previous experience with Python, I recommend downloading and installing the [Anaconda Python distribution](https://www.anaconda.com/distribution/ ) (Python 3.x version), as it includes all the required the scientific packages (requires > 5 GB disk space). In case you have a limited space in your hard disk, there is a distribution named [miniconda](http://conda.pydata.org/miniconda.html ) that only installs the Python packages you actually need. For both cases you have versions for Windows, MacOS and Linux.

Anaconda Python Distribution: https://www.anaconda.com/distribution/ 

Miniconda: http://conda.pydata.org/miniconda.html 

Once Anaconda is installed on your system, launch the Anaconda Navigator you will see that you have installed at least two different scientific-oriented integrated development systems (IDEs): **Spyder** and **Jupyter lab**. The GrainSizeTools documentation is written assuming that  carry out the work in one of these two IDEs. For more details see [Getting Started: A step-by-step tutorial](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/getting_started.md).



> 👉 The GrainSizeTools script is not designed to deal with microscopic images but to analyse and visualize grain size populations and estimate stresses via paleopiezometers. **It is therefore necessary to measure the grain diameters or the sectional areas/volumes of the grains in advance and store them in a txt/csv/excel file**. For this task, we highly encourage you to use the [*ImageJ*](http://rsbweb.nih.gov/ij/) application or one of their different flavours (see [here](http://fiji.sc/ImageJ)). ImageJ-type applications are public-domain image processing programs widely used for scientific research that runs on Windows, macOS, and Linux platforms. The documentation contains a quick tutorial on how to measure the areas of the grain profiles with ImageJ, see *Table of Contents*. The combined use of **ImageJ** and **GrainSizeTools script** is intended to ensure that all data processing steps are done through free and open-source programs/scripts that run under any operating system. If you are dealing with EBSD data instead, we encourage you to use the [MTEX toolbox](https://mtex-toolbox.github.io/) for grain reconstruction and the [export2file script](https://github.com/marcoalopez/export2file) for exporting the data (a tutorial on this will be available soon).



## Open and running the script

First of all, make sure you have the latest version of the GrainSizeTools (GST) script and a Python scientific distribution installed (see [Installing Python for data science](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/installing_Python.md) for more details). If you are not familiarized with Python, I propose two main options:

1. Use the [Spyder](https://www.spyder-ide.org/) integrated development environment (IDE) (Fig. 1), a MATLAB-like scientific IDE optimized for numerical computing and data analysis with Python. If you are familiar with MATLAB this is probably the easiest way to go.

2. Use the [Jupyter notebook](https://jupyter.org/) (Fig. 2), a browser-based environment that allows you to create and share documents that may contain live code, equations, visualizations and narrative text.

Make your choice and launch it from the Anaconda navigator or just by typing ``Spyder`` or ``jupyter lab`` in the terminal.

![Figure 1. The Python editor and the shell in the Enthought Canopy environment](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/IDEs.png)  *Figure 1. The [Spyder](https://www.spyder-ide.org/) v.4+ integrated development environment (IDE) showing the editor (left), the IPython shell or console (bottom right), and the help-variable explorer window (top right). This is a MATLAB-like IDE for Python that provides a variable explorer, a history log, MATLAB-like cells, code auto-completion, etc.*

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/Jupyter_lab.png?raw=true)

*Figure 2. The Jupyter Lab development environment, a browser-based notebook that allows creating documents that may contain live code, equations (using Latex), visualizations and narrative text*.

In Spyder, open the ``GrainSizeTools_script.py`` file using ```File>Open``` and then run the script clicking on the "play" green icon in the toolbar (or go to ```Run>Run file``` in the menu bar). After running, the following text will appear in the console:

```
module plot imported
module averages imported
module stereology imported
module piezometers imported
module template imported

======================================================================================
Welcome to GrainSizeTools script
======================================================================================
A free open-source cross-platform script to visualize and characterize grain size
population and estimate differential stress via paleopizometers.

Version: v3.0RC0 (2020-05-xx)
Documentation: https://marcoalopez.github.io/GrainSizeTools/

Type get.functions_list() to get a list of the main methods
```

Alternatively, if you are using Jupyter lab/notebook you have a similar step-by-step tutorial in the link below and within the ``grain_size_tools`` folder in your hard disk:

https://github.com/marcoalopez/GrainSizeTools/blob/master/grain_size_tools/notebook_example.ipynb

As indicated in the welcome message, we can get a list of the main methods at any time by typing in the console:

```python
get.functions_list()
```

![](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/function_list.png)

