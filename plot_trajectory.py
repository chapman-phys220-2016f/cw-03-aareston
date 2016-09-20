#!/usr/bin/env python

"""Module Description
The docstring at the top of the file appears in the "Description" field of 
the help command. That is, if you load a python interpreter the following 
makes the docstring visible:

  $ python
  >>> import your_module
  >>> help(your_module)

Note the name "your_module" is just the filename without the .py extension.
You can check this field for any other python module (numpy, sympy, etc.) 
to get an idea about how module documentation is usually handled.
"""

import numpy as np
import matplotlib.pyplot as plt

def y2(x):
    return ((x)*np.tan(theta))-((1/(2*(vo**2)))*((9.8*x)/(np.cos(theta)**2))+ yo)

def plot_Trajectory():
    t = np.linspace(0, 2, 10)
    y = y2(x)
    yo = 0
    vo = 3
    theta = 30

    plt.plot(x, y)
    plt.xlabel('time (s)')
    plt.ylabel('height (m)')
    plt.title('Trajectory of a Ball')
    plt.show()

