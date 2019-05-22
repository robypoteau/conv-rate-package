import numpy as np

def witherr(err):
    temp = np.abs(err)

    x = np.log10(temp[:-1])
    y = np.log10(temp[1:])

    r, C = np.polyfit(x, y, 1)
    return [r, np.power(10,C)]

def withsol(sol, L=None):
    temp = np.array(sol)
    if L == None:
        err = np.abs(temp[1:] - temp[:-1])
    else:
        err = np.abs(temp - L)

    x = np.log10(err[:-1])
    y = np.log10(err[1:])

    r, C = np.polyfit(x, y, 1)
    return [r, np.power(10,C)]
