import numpy as np


def PDF_COS(x, lam=3):
    """ returns the cos of x*lam think of lam as a squishification constant """
    return np.cos(x*lam)


def PDF_SIN(x, lam=2):
    """ returns the sin of x*lam think of lam as a squishification constant """
    return np.sin(x*lam)
