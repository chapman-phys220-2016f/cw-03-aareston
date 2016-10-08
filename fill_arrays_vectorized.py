#!bin/usr/env python

import nose as n
import numpy as np

"""
Module creates an array containing the evaluation of some h(x), defined here as 1 / sqrt(2 * pi) * e ** (-1 / 2 * x ** 2), at a series of 41 points in the interval [-4,4]
"""

import numpy as np

def fill_array(a, b, n):
    """
    Fills array with equally spaced points, taking the beginning point, the end point, and the number of desired coordinates
    """
    return np.linspace(a, b, n, endpoint=True, dtype=float)

def h(x):
    """
    A definition for the function h(x), returning the value of h evaluated at the point x
    """
    return 1.0 / np.sqrt(2.0 * np.pi) * np.exp(-1.0 / 2.0 * x ** 2.0)

def main():
    for x in range(41):
        print '%-0.5f %-0.5f' % (fill_array(-4, 4, 41)[x], h(fill_array(-4, 4, 41)[x]))

def test_h():
    """
    Test for function default h(x) defined above, using the initial point x = 0.0
    """
    test = h(0.0)
    n.tools.assert_almost_equals(test, (1 / np.sqrt(2 * np.pi)), places = 5)

if __name__ == "__main__":
    main()
