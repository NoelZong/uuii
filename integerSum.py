"""
integerSum.py

Functions for summing integers

"""

import numpy as np


def nsum(n):

    """
    Sum the integers from 1 to n
    
    ARGUMENTS:  n   a positive integer
    
    RESULT:     s   the sum of the first n integers
    """

    #Initialise the sum to zero.
    s = 0;

    #Accumulate the sum by adding each integer in turn.
    for k in range(n + 1):
        s += k

    return s

def nsum_matrix(n):
    """
    Sum the integers from 1 to n
    
    ARGUMENTS:  n   a scalar or array of positive integers

    RESULT:     s   the sum of the first n(i) integers for each value of n
    """

    #If scalar return nsum(n)
    if isinstance(n,int):
        return nsum(n)
    
    #Else initialise to zero
    dim = np.shape(n)
    s = np.zeros(dim)
    
    for idx in np.ndindex(dim):
        #Accumulate the sum by adding each integer in turn
        s[idx] = nsum(n[idx])

    return s
    
    
    
    
        
