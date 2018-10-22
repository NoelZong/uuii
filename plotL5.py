"""
plotl5.py

This module contains plotting examples using matplotlib

To run via commanline use

python plotl5.py -m sine

OR

python plotl5.py -m nsum

"""

import sys
import os
import getopt
import numpy as np
import matplotlib.pyplot as plt

#Imports all functions from integer sum
from integerSum import *

def main(argv):
    try:
	# (short) options that require an argument are followed by a colon (':'; i.e., the same format that Unix getopt() uses)
	# Long options which require an argument should be followed by an equal sign ('=')
        opts, args = getopt.getopt(argv[1:], "m:", 
                                   ["mode="]) 
    except getopt.GetoptError:
	print "Warning: Unknown flag!"
	sys.exit(2)
	return 0     
    
    mode = None
    
    for opt,arg in opts:
        if opt in ("-m","--mode"): mode = arg
    
    if mode == 'sine':
        plot_sine()
    elif mode == 'nsum':
        plot_nsum()

def plot_sine():
    """
    Plots the graph sin(pi*x)
    """
    
    plt.figure()
    
    plt.subplot(311)
    y1 = plot_script()
    
    plt.subplot(312)
    y2 = plot_script_degrees()
    
    plt.subplot(313)
    erry = y2 - y1
    plt.plot(np.linspace(0,2,51),erry)
    # For label: Any text element can use math text. 
    # You should use raw strings (precede the quotes with an 'r'), and surround the math text with dollar signs ($), 
    plt.xlabel(r'$\theta$(radians)')
    plt.ylabel('Error')

    plt.show()

def plot_script():
    """
     Plots the graph of sine(pi*x) in radians
    """

    #Fix the number of points at which to plot the function
    n = 51

    #Set the vector x to contain n linearly spaced points between 0 and 2
    x = np.linspace(0,2,n)

    #Set y vector at specified values of x
    y = np.sin(np.pi*x)

    #Plot the graph
    plt.plot(x,y)
    plt.xlabel(r'$\theta$(radians)')
    plt.ylabel(r'sin($\theta$)')
    
    return y

def plot_script_degrees():
    """
    Plots the graph of sin(pi*x) in degrees
    """

    #Fix the number of points at which to plot the function
    n = 51
    
    #Set the vector x to contain n linearly spaced points between 0 and 360 degrees
    deg = np.linspace(0,360,n)

    #Set y vector at specified values of x
    y = np.sin(np.pi*deg/180)
    
    #Plot the graph
    plt.plot(deg,y)
    plt.xlim([0,360])
    plt.xlabel(r'$\theta$(degrees)')
    plt.ylabel(r'sin($\theta$)')
    
    return y

def plot_nsum():
    """
    Plots the sum of the first k integers against k
    """

    #Set the range of values to plot
    n = 11

    #Initialise x 
    x = range(1,n+1)

    #Map x to y vis nsum function
    y = map(nsum,x)
    
    #Plot the graph
    plt.figure()
    plt.plot(x,y)
    plt.xlim([1,n])
    plt.xlabel('k')
    plt.ylabel('nsum(k)')
    plt.show()

if __name__=='__main__':
    main(sys.argv)



