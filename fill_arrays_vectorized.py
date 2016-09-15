#!bin/usr/env python

"""

"""

import numpy as np

def fill_array():
    return np.linspace(-4, 4, 41, endpoint=True)


def h(x):
    return 1.0 / np.sqrt(2.0 * np.pi) * np.exp(-1.0 / 2.0 * x ** 2.0)

def main(argv):
    print [fill_array(), h(fill_array())]
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)
