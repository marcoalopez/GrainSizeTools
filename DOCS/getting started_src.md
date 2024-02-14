# Getting started

> [!CAUTION]
> This wiki is not complete and will be the official documentation for the new version of the script to be released in 2024.

The aims of this section are

- How to install Python using the Anaconda or Miniconda distributions.
- How to install GrainSizeTools.
- How to use Python with tools like Jupyter Notebook or JupyterLab.
- How to interact with the script and import data.

## Step 1. Install Python for data science

TODO

## Step 2. Download the GrainSizeTools

Once Python is installed, the next step is to download GrainSizeTools. Click on the download link below (there is also a direct link on the website).

https://github.com/marcoalopez/GrainSizeTools/releases

and download the latest version of the script by clicking on the zip file as shown below

TODO-> figure

### Script organization

The GrainSizeTools folder contains the Python script code (several .py files) a folder named DATA, and various Jupyter notebooks (.ipynb files), which are templates for performing different types of grain size data analysis, either (i) quantifying grain size populations (apparent or real), (ii) performing stereological methods to approximate a true grain size distribution, or (iii) performing palaopiezometry using the GrainSizeTools database. 

TODO

## Step 3. How to open and work with Jupyter Notebooks 

To improve the reproducibility of the granulometric population studies, we suggest that the user works with the Jupyter Notebooks templates provided in the script, especially if he/she has no previous experience with the Python language. To do this, it is necessary to open the Jupyter notebooks through the application. We suggest JupyterLab or Vscode (see above), but you can also use others.

The [Jupyter Notebook](https://jupyter.org/) is a document that can contain live code, equations, visualisations and narrative text, ideal for generating reports and including as supplementary material in your publications so that any researcher can reproduce your data.

TODO -> Figure showing a Jupyter Notebook

*Figure X. An example of a Jupyter notebok with code, equations (using Latex), visualizations and narrative text*.

JupyterLab and VSCode with the Jupyter Notebook extension are the next generation of the Classic Jupyter Notebook application interface, providing an easy-to-use environment focused on data science.

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/Jupyter_lab.png?raw=true)

*Figure X. The JupyterLab interface...TODO. More info: https://jupyterlab.readthedocs.io/en/latest/user/interface.html#the-jupyterlab-interface

TODO

## Understanding the script and the workflow

The script is organised in a modular way using different Python files and functions, both of which are intended to help modify, reuse and extend the code if necessary. In short, the script consists of seven Python files that must be in the same directory. These are the Python files and their main function:

- ``GrainSizeTools.py``: This file imports all the modules needed for the script to work. This is the only executed Python file in the Jupyter Notebook templates.
- ``averages.py``: This module contains a set of functions for calculating different types of averages and margins of error.
- ``plot.py``: This module contains a set of functions for generating different types of ad hoc plots used by the script.
- ``stereology.py``: This module contains a set of functions to approximate true grain size distributions from sectional measurements using stereological methods.
- ``piezometric_database.py``: This file contains the database of piezometers the script uses.
- ``template.py``: This file contains the default (Matplotlib) parameters used by the script to generate plots.
- ``get.py``: This file contains the welcome message of the script.

For non-advanced users, we recommend the use of the Jupyter notebooks provided with the script. There are three different notebooks depending on the type of study you want to perform: (i) quantification of grain size distributions, (ii) approximation of grain size distributions using stereological methods, and (iii) paleopiezometry. These notebooks contain all the necessary instructions on how to use them through practical examples. The user will only has to change some parameters to adapt them to his practical case and delete everything that is not needed. Once this has been done, all the analyses are contained in a single, fully reproducible document that can be exported to other formats (pdf, html, etc.) if necessary. If you use this workflow, ideally you should copy the entire contents of the script (<<1 MB), i.e. the code and notebooks, for each study you conduct.

## Importing data using the Pandas library

The way we propose to import the data to be analysed by the script is to use [Pandas](https://pandas.pydata.org/), which is the de facto standard Python library for data analysis and manipulation of tabular data (including CSV, Excel or text files). The library includes several tools for reading files and handling missing data. Once the GrainSizeTools script is run, all the Pandas methods are imported as ``pd`` and available once you write in a cell ``pd.``. TODO

TODO

> [!TIP]
> Although you can use the ``get_filepath()`` function to get a file path through a file selection window as follows
>
> ```python
> >>> filepath = get_filepath()
> ```
> for reproducibility it is best to specify the file path explicitly in the notebook.