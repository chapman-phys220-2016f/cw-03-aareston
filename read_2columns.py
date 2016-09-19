#!bin/usr/env python

import numpy as np

"""
Reads 2 column data file with each column formated as "-----[dat1]-------[dat2]" where dashes are whitespace and [dat1] and [dat2] are the columns, each containing 
"""

def readDat(f):
    """
    Reads file and converts two column data into arrays of floats. Takes name of file as argument. Returns first column then second column as arrays
    """
    infile = open(f, 'r')
    column1 = []
    column2 = []
    for line in infile:
        words = line.split()
        column1.append(words[0])
        column2.append(words[1])
    col1 = np.array(column1)
    col2 = np.array(column2)
#   print (col1, col2) Debugging assistance
    return col1, col2

def main():
    """
    Executes readDat on xy.dat
    """
    readDat("xy.dat")

def test_readDat():
    """
    Tests readDat for test.dat file
    """
    test = readDat("test.dat")
    case = ([1.0,1.0,1.0],[1.0,1.0,0.0])
    success = 0

    def a_eq(x,y,tol = 1E-5):
        return (abs(x - y) < tol)

    for i, j in zip(test, case):
        if a_eq(i,j):
            success += 1
    assert (success == 3)

if __name__ == "__main__":
    main();
