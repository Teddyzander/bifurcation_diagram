# bifurcation diagram

This is part of some wider reading I have been doing in population dynamics, fractal geometry, and dynamical systems.
During some reading between some computer science texts and some of my old notes on population dynamics, I noticed 
John von Neumann suggesting to use the logistic map of x(n+1) = 4x(n)(1-x(n)) to generate random numbers (as
generating truly random numbers on a computer was not a simple feat). I recognised the equation from my old population
dynamics, and wanted to see how this would generate random numbers. Also, the diagram is such an elegant representation
of mathematics, and I thought it would fun to code.

### Logistic Map

The logistic map, as I know it, was a simple model to predict how a population of something would change over time.

In it's most basic form, it is

x(n+1) = rx(n)(1-x(n)) where

*   x(n+1) is the next population, as a percentage of a theoretical maximum (between 0 and 1)
*   r ia a positive constant (written in my notes as the biotic potential)
*   x(n) is the current population, again as a percentage of a theoretical maximum (between 0 and 1)

### System behaviour

The long term behaviour of this system, depending on the choice of r, is incredibly interesting.

For small values of r, the system is stable. If my notes from lectures are correct:

1.  For 0 <= r <= 1 the population will eventually become extinct, regardless of the initial population
2.  For 1 <= r <= 3 the population will tend towards (r-1)/r, regardless of the initial population (though it will 
converge much slower if 2 < r <= 3).
3.  For values larger than 3, but less than 4, we start to oscillate between values, rather than stablising on one
value. For 3 < r < 1 + sqrt(6), it will oscillate between two values. For 1 + sqrt(6) <= r < 3.54409, it will oscillate 
between 4 values. Then 8, then 16, etc. This behaviour is known as period-doubling.
4.  Beyond 3.56995, chaos begins and the oscillations end (mostly, though there are occasionally "islands of stability")
5.  Beyond 4, almost every initial population will eventually leave the [0,1] interval, and diverge.

### Link to fractal geometry

The bifurcation diagram is self similar, hence it's connection the fractals. In fact, if you plot the mandlebrot set
in such a way that the z axis is the value that the iteration stabilises on, it will plot a bifurcation diagram.

Interesting!