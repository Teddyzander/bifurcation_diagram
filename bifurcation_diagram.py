import numpy as np
import matplotlib.pyplot as plt


def logistic_map(r, x):
    """
    Logistic map function
    :param r: biotic potential
    :param x: Current population
    :return: Next population
    """
    if x.any() > 1:
        raise Exception("x cannot be larger than 1")
    else:
        return r * x * (1 - x)


# Create a graph the represent the logistic map of current population against next population
x = np.linspace(0, 1)
fig, ax = plt.subplots(1, 1)
ax.plot(x, logistic_map(2, x), "k")

plt.show()
