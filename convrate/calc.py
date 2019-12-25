import numpy as np

def witherr(err):
    """Convergence rate calculator.

    Calculate the convergence rate using a vector of error values from a
    given algorithm.

    Parameters
    ----------
    err :  array_like
        list (or vector) of error values in order.

    Returns
    -------
    ndarray, shape (2,1)
        order of convergence and rate of convergence

    """
    temp = np.abs(err)

    x = np.log10(temp[:-1])
    y = np.log10(temp[1:])

    r, C = np.polyfit(x, y, 1)
    return [r, np.power(10,C)]

def withsol(sol, L=None):
    """Convergence rate calculator.

    Calculate the convergence rate using a vector of solutions from a
    given algorithm at each iteration.

    Parameters
    ----------
    err :  array_like
        list (or vector) of values outputted by the given algorithm in order
    L : float, optional
        the true solution to the algorithm

    Returns
    -------
    ndarray, shape (2,1)
        order of convergence and rate of convergence

    """
    temp = np.array(sol)
    if L == None:
        err = np.abs(temp[1:] - temp[:-1])
    else:
        err = np.abs(temp - L)

    x = np.log10(err[:-1])
    y = np.log10(err[1:])

    r, C = np.polyfit(x, y, 1)
    return [r, np.power(10,C)]
