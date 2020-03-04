import numpy as np
from scipy.stats import sem, t, norm


def confidence_interval(data, confidence=0.95):
    """Estimate the confidence interval using the t-distribution with n-1
    degrees of freedom t(n-1). This is the way to go when sample size is
    small (n < 30) and the standard deviation cannot be estimated accurately.
    For large datasets, the t-distribution approaches the normal distribution.

    Parameters
    ----------
    data : array-like
        the dataset

    confidence : float between 0 and 1, optional
        the confidence interval, default = 0.95

    Assumptions
    -----------
    the data follows a normal or symmetric distrubution (when sample size
    is large)

    call_function(s)
    ----------------
    Scipy's t.interval

    Returns
    -------
    None
    """

    dof = len(data) - 1
    sample_mean = np.mean(data)
    std_err = sem(data)  # Standard error of the mean SD / sqrt(n)
    low, high = t.interval(confidence, dof, sample_mean, std_err)
    err = high - sample_mean

    print(' ')
    print('Confidence set at {} %' .format(confidence * 100))
    print('Mean = {mean:0.2f} ± {err:0.2f}' .format(mean=sample_mean, err=err))
    print('Max / min = {max:0.2f} / {min:0.2f}' .format(max=high, min=low))
    print('Coefficient of variation = {:0.1f} %' .format(100 * err / sample_mean))

    return None

def area2diameter(areas, correct_diameter=None):
    """ Calculate the equivalent cirular diameter from sectional areas.

    Parameters
    ----------
    areas : array_like
        the sectional areas of the grains

    correct_diameter : None or positive scalar, optional
        add the width of the grain boundaries to correct the diameters. If
        correct_diameter is not declared no correction is considered.

    Returns
    -------
    A numpy array with the equivalent circular diameters
    """

    # calculate the equivalent circular diameter
    diameters = 2 * np.sqrt(areas / np.pi)

    # diameter correction adding edges (if applicable)
    if correct_diameter is not None:
        diameters += correct_diameter

    return diameters