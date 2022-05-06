import numpy as np


def PDF_COS(x: np.array, lam: float = 3) -> np.array:
    """ returns the cos of x*lam think of lam as a squishification constant """
    return np.cos(x*lam)


def PDF_SIN(x: np.array, lam: float = 2) -> np.array:
    """ returns the sin of x*lam think of lam as a squishification constant """
    return np.sin(x*lam)


def PDF_LINEAR(x: np.array, lam: float = 1) -> np.array:
    """ returns x*lam think of lam as a squishification constant """
    return x*lam


def PDF_1BY_E(x: np.array, lam: float = 5) -> np.array:
    """ returns 1/x think of lam as a squishification constant """
    return 1/np.exp(x*lam)


def PDF_E(x: np.array, lam: float = 5) -> np.array:
    """ returns e^(lam*x) think of lam as a squishification constant """
    return np.exp(x*lam)


def PDF_90E(x: np.array, lam: float = 5) -> np.array:
    """ returns an nparray think of lam as a squishification constant """
    return 1-(x**3*lam)
