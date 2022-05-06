import numpy as np


def PDF_COS(x: np.array, lam: float = 3) -> np.array:
    """ returns the cos of x*lam think of lam as a squishification constant """
    return np.cos(x*lam)


def PDF_SIN(x: np.array, lam: float = 2) -> np.array:
    """ returns the sin of x*lam think of lam as a squishification constant """
    return np.sin(x*lam)


def func(x: np.array, lam: float = 1) -> np.array:
    """ returns x*lam think of lam as a squishification constant """
    return x*lam
