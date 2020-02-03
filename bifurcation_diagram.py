import numpy as np
import matplotlib.pyplot as plt


def logistic_map(r, x):
    """
    Logistic map function
    :param r: biotic potential
    :param x: Current population
    :return: Next population
    """
    if type(x) == float:
        if x > 1:
            raise Exception("x cannot be larger than 1")
    else:
        if x.any() > 1:
            raise Exception("x cannot be larger than 1")

    return r * x * (1 - x)


def plot_system(r, x0, n, ax=None):
    """
    Plotting the logistic map and the line of y = x, showing how the system stabilises
    :param r: biotic potential
    :param x0: Initial population
    :param n: number of iterations
    :param ax: plots
    :return: nothing, just display the plots
    """

    t = np.linspace(0, 1)

    # plot the logistic map
    ax.plot(t, logistic_map(r, t), "k", lw=2)
    # plot the line of y=x
    ax.plot([0, 1], [0, 1], "k", lw=2)

    # if y=f(x) [where f(x) is the logistic map], recursively plot the lines of (x, x) -> (x, y) and (x, y) -> (y, y)
    # to show the convergence

    x = x0
    for i in range(n):
        y = logistic_map(r, x)

        # plot the lines
        ax.plot([x, x], [x, y], "k", lw=1)
        ax.plot([x, y], [y, y], "k", lw=1)

        # plot the position with increasing opacity to show convergence
        ax.plot([x], [y], "ok", ms=10, alpha=(i + 1) / n)

        # set the new population to be the current population
        x = y

    # title axis and display the plot
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
plot_system(2.5, 0.1, 1000, ax=ax1)
plot_system(3.5, .1, 1000, ax=ax2)
plt.show()
