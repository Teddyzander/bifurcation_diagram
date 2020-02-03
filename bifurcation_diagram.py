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


"""
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
plot_system(3.56994, .1, 1000, ax=ax2)
plt.show()
"""

# Now we can plot the bifurcation diagram

# number of r values we will simulate
n = 10000
# values for r
r = np.linspace(0, 4, n)
# number of iterations (we will plot the last 100 iterations, assuming we have reached a convergence/oscillation
iterations = 1000
last = 100
# initial condition for population of 0.00001
x = 1e-5 * np.ones(n)
# approximate lyapunov exponent for r (can be seen as the rate of seperation)
lyapunov = np.zeros(n)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 9), sharex=True)
for i in range(iterations):

    x = logistic_map(r, x)

    # calculate the partial sum of the lyapunoc exponent
    lyapunov += np.log(abs(r - 2 * r * x))

    # display the bifurcation diagram
    if i >= (iterations - last):
        ax1.plot(r, x, ",k", alpha=0.25)

ax1.set_xlim(0, 4)
ax1.set_title("Bifurcation diagram")

# We display the Lyapunov exponent.
# Horizontal line.
ax2.axhline(0, color='k', lw=.5, alpha=.5)
# Negative Lyapunov exponent in black
ax2.plot(r[lyapunov < 0],
         lyapunov[lyapunov < 0] / iterations,
         '.k', alpha=.5, ms=.5)
# Positive Lyapunov exponentin red
ax2.plot(r[lyapunov >= 0],
         lyapunov[lyapunov >= 0] / iterations,
         '.r', alpha=.5, ms=.5)
ax2.set_xlim(0, 4)
ax2.set_ylim(-2, 1)
ax2.set_title("Lyapunov exponent")
plt.tight_layout()

plt.show()