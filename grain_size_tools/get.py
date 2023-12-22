welcome = """
======================================================================================
Welcome to GrainSizeTools script
======================================================================================
A free open-source cross-platform script to visualize and characterize grain size
population and estimate differential stress via paleopizometers.

Version: 2024.02.xx
Documentation: https://marcoalopez.github.io/GrainSizeTools/

Type get.functions_list() to get a list of the main methods
"""

info = """
======================================================================================
List of main functions
======================================================================================
summarize              -> get the properties of the data population
conf_interval          -> estimate a robust confidence interval using the t-distribution
calc_diffstress        -> estimate diff. stress from grain size using piezometers

plot.distribution      -> visualize the distribution of grain sizes and locate the averages
plot.qq_plot           -> test the lognormality of the dataset (q-q plot + Shapiro-Wilk test)
plot.area_weighted     -> visualize the area-weighed distribution of grain sizes
plot.normalized        -> visualize a normalized distribution of grain sizes

stereology.Saltykov    -> approximate the actual grain size distribution via the Saltykov method
stereology.calc_shape  -> approximate the lognormal shape of the actual distribution
======================================================================================

You can get more information about the methods using the following ways:
    (1) Typing ? or ?? after the function name, e.g. summarize?
    (2) Typing help plus the name of the function, e.g. help(summarize)
    (3) In the Spyder IDE by writing the name of the function and clicking Ctrl + I
    (4) In Jupyter lab/notebook by enabling the "Show contextual help", the info
    will pop up as soon as you write the name of the function.
"""


def functions_list():
    print(info)
    return None


if __name__ == '__main__':
    pass
else:
    print(welcome)
