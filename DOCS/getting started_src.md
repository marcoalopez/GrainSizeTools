# Getting started

The aims of this section are

- How to install Python using the Anaconda or Miniconda distributions.
- How to install GrainSizeTools.
- How to use Python with tools like Jupyter Notebook or JupyterLab.
- How to interact with the script and import data.

## Installing Python for data science

TODO

## Downloading the GrainSizeTools script and script organization

Once Python is installed, the next step is to download GrainSizeTools. Click on the download link below (there is also a direct link on the website).

https://github.com/marcoalopez/GrainSizeTools/releases

and download the latest version of the script by clicking in the the zip file as shown below

TODO-> figure

The GrainSizeTools folder contains the Python script code (several .py files) a folder named DATA, and various Jupyter notebooks (.ipynb files), which are templates for performing different types of grain size data analysis, either (i) quantifying grain size populations (apparent or real), (ii) performing stereological methods to approximate a true grain size distribution, or (iii) performing palaeopiezometry using the GrainSizeTools database. 

TODO

## Run Jupyter notebooks and JupyterLab

In order to improve the reproducibility of studies working with grain size populations, we suggest that the user works from the Jupyter notebooks templates provided by the script, especially if you have no previous experience with the Python language. To do this, it is necessary to open the notebooks either through the Jupyter notebooks application or through JupyterLab.

Briefly, [JupyterLab (or Jupyter Notebook)](https://jupyter.org/) (Fig. 2) provides an easy-to-use data science environment that allows you to create and share documents that may contain live code, equations, visualizations and narrative text. This is also ideal for generating reports and including them as supplementary material in your publications, so that any researcher can reproduce your data. JupyterLab is just the next generation of the “classic” Jupyter Notebook so you can use either one interchangeably (Fig. X).

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/Jupyter_lab.png?raw=true)

*Figure X. The JupyterLab development environment is an interactive data science environment that allows creating documents mixing code, equations (using Latex), visualizations and narrative text*.

TODO

## Importing data and interacting with the script

The script is organised in a modular way using different Python files and functions, both of which are intended to help modify, reuse and extend the code as necessary. In short, the script consists of seven Python files that must be in the same directory. These are the Python files and their main function:

- ``GrainSizeTools.py``: This file takes care of importing all the submodules needed for the script to work. It is the Python file that is executed directly from the Jupyter Notebook templates.
- ``averages.py``: This sub-module contains a set of functions for calculating different types of averages and margins of error.
- ``plot.py``: This sub-module contains a set of functions for generating different types of ad hoc plots used by the script.
- ``stereology.py``: This sub-module contains a set of functions to approximate true grain size distributions from sectional measurements using stereological methods.
- ``piezometric_database.py``: This file contains the database of the various piezometers used by the script.
- ``template.py``: This file contains the default options used by the Python Matplotlib library to generate plots.
- ``get.py``: This file contains the welcome message of the script.

### Importing data using the Pandas library

The way we propose to import the data to be analysed by the script is to use [Pandas](https://pandas.pydata.org/), which is the de facto standard Python library for data analysis and manipulation of tabular data (including CSV, Excel or text files). The library includes several tools for reading files and handling missing data. Once the GrainSizeTools script is run, all the Pandas methods are imported as ``pd`` and available once you write in a cell ``pd.``. TODO

TODO

> [!TIP]
> Although you can use the ``get_filepath()`` function to get a file path through a file selection window as follows
>
> ```python
> >>> filepath = get_filepath()
> ```
> for reproducibility it is best to specify the file path explicitly in the notebook.