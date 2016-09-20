#!bin/usr/env python

import numpy as np
import matplotlib.pyplot as plt

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
        if(isNumber(words[0])):
            column1.append(words[0])
        if(isNumber(words[1])):
            column2.append(words[1])
    col1 = np.array(column1)
    col2 = np.array(column2)
#   print (col1, col2) Debugging assistance
    return col1, col2

#This function is borrowed from user Daniel Goldberg on Stack Overflow, post at http://stackoverflow.com/q/354038
def isNumber(s):
    """
    This function takes a string as an argument and tries to parse it to float. If it can, it returns true. Else, it returns false. This will filter elements in the .dat file so that only numbers are included in the returned arrays
    """
    try:
        float(s)
        return True 
    except ValueError:
        return False

def main():
    """
    Executes readDat on xy.dat
    """
    dat = readDat("xy.dat")
    plt.plot(dat[0], dat[1], '-r')
    plt.xlabel('x variable')
    plt.ylabel('y variable')
    plt.title('Graphing 2 Column Data')
    plt.show()
    print 'Mean y value is ', np.mean(dat[1])
    print 'Max y value is ', np.amax(dat[1])
    print 'Minimum y value is ', np.amin(dat[1])


def test_readDat():
    """
    Tests readDat for test.dat file
    """
    test = readDat("test.dat")
    case = ([1.0,1.0,1.0],[1.0,1.0,0.0])
    success = 0

    def a_eq(x,y,tol = 1E-5):
        x = float(x)
        y = float(y)
        return (abs(x - y) < tol)

    for (i,j) in zip(test[0], case[0]):
        if a_eq(i,j):
            success += 1
    for (i,j) in zip(test[1], case[1]):
        if a_eq(i,j):
            success += 1
    assert (success == 6)

if __name__ == "__main__":
    main();
