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

def y1(t):
    return (10*t)-(4.405*(t**2))

def plot_Gravity():
    t = np.linspace(0, 2, 10)
    y = y1(t)

    plt.plot(t, y)
    plt.xlabel('time (s)')
    plt.ylabel('height (m)')
    plt.title('Effect of Gravity on Thrown Ball')
    plt.show()

