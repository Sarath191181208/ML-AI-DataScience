import numpy as np


def PDF_COS(x, lam=3):
    """ returns the cos of x*lam think of lam as a squishification constant """
    return np.cos(x*lam)
