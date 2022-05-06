import numpy as np

CONST_E = np.exp(1)


def PDF_COS(x: np.array, lam: float = 0.5) -> np.array:
    """ returns the cos of x*lam think of lam as a squishification constant """
    return (1+np.cos(x*lam))*0.5


def PDF_SIN(x: np.array, lam: float = 0.5) -> np.array:
    """ returns the sin of x*lam think of lam as a squishification constant """
    return (0.75+np.sin(x*lam))/(1.75)


def PDF_LINEAR(x: np.array, lam: float = 1) -> np.array:
    """ returns x*lam think of lam as a squishification constant """
    return x*lam


def PDF_SQUARE(x: np.array, lam: float = 5) -> np.array:
    """ returns x^2 think of lam as a squishification constant """
    return x**np.cos(x*lam)


def PDF_E(x: np.array, lam: float = 4) -> np.array:
    """ returns e^(-x*lam) think of lam as a bend factor """
    return np.exp(-x*lam)


def PDF_90E(x: np.array, lam: float = 4) -> np.array:
    """ returns 90 deg of e^-x graph think of lam as bend factor"""
    return 1 - np.exp(-x*lam)


def PDF_180E(x: np.array, lam: float = 4) -> np.array:
    """ returns 180 deg of e^-x graph think of lam as bend factor"""
    return -np.exp(x*lam)*(1/(CONST_E**lam)) + 1


def PDF_270E(x: np.array, lam: float = 4) -> np.array:
    """ returns 270 deg of e^-x graph think of lam as bend factor"""
    return 1/(CONST_E**lam)*np.exp(x*lam)
