import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    """
    Logistic map function
    :param r: biotic potential
    :param x: Current population
    :return: Next population
    """
    if x > 1:
        raise Exception("x cannot be larger than 1")
    else:
        return r * x * (1 - x)