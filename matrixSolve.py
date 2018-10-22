import numpy as np

def lower_triangular_solve(A,b0):
    """
    Solve the system  A x = b  where A is assumed to be lower triangular,
    i.e. A(i,j) = 0 for j > i, and the diagonal is assumed to be nonzero,
    i.e. A(i,i) \= 0.
    
    ARGUMENTS:  A   lower triangular n x n array
                b0   right hand side column n-vector
                
    RETURNS:    x   column n-vector solution    
    """

    #Check that A is lower triangular
    if not np.allclose(A,np.tril(A)):
        print "Error: The input array is not lower triangular!"
        return None

    #Get n-dimension
    n = len(b0)
    
    #Copy vector b0 and convert to float
    b = np.copy(b0).astype(float)

    #Initialise x
    x = np.zeros([n,1])
    
    #Loop through the remaining rows, calculating the solution components
    #in turn by backward substitution
    
    for i in xrange(n):
        for j in xrange(i):
            b[i] = b[i] - A[i,j]*x[j]
        x[i] = b[i] / A[i,i]

    return x


def upper_triangular_solve(A,b0):
    """
    Solve the system  A x = b  where A is assumed to be upper triangular,
    i.e. A(i,j) = 0 for j < i, and the diagonal is assumed to be nonzero,
    i.e. A(i,i) \= 0.
    
    ARGUMENTS:  A   upper triangular n x n array
                b0   right hand side column n-vector
                
    RETURNS:    x   column n-vector solution    
    """

    #Check that A is upper triangular
    if not np.allclose(A,np.triu(A)):
        print "Error: The input array is not upper triangular!"
        return None

    #Get n-dimension
    n = len(b0)
    
    #Copy vector b0 and covert to float
    b = np.copy(b0).astype(float)

    #Initialise x
    x = np.zeros([n,1])
    
    #Loop through the remaining rows, calculating the solution components
    #in turn by backward substitution
    
    for i in xrange(n-1,-1,-1):
        for j in xrange(i+1,n):
            b[i] = b[i] - A[i,j]*x[j]
        x[i] = b[i] / A[i,i]

    return x

def gauss_elimination(A,b,*args):
    """
    Reduce the system  A x = b  to upper triangular form, assuming that
    the diagonal is nonzero, i.e. A(i,i) \= 0.
    
    ARGUMENTS:  A   n x n matrix
                b   right hand side column n-vector
                
                print  (optional) prints elimination steps
    
    RETURNS:    A   upper triangular n x n matrix
                b   modified column n-vector    
    """
    #Get dimensions
    n = len(b)
    
    #Make sure entries are set to float
    A = A.astype(float)
    b = b.astype(float)
    
    #Loop through the rows (i) of the system
    for i in xrange(n-1):
        #Print solution information
        if 'print' in args:
            print 'Eliminate column %d\n' %i
            raw_input('Press key to continue')

        #Pick out the diagonal entry (and assume that it isn't zero
        r = 1. / A[i,i]
        
        #Loop through the rows (j) of the system below row i
        for j in xrange(i+1,n):
            #Calculate the multiplier for that row for elimination
            d = r * A[j,i]
 
            #Loop through the elements of row j which have yet to be set to zero
            for k in xrange(i,n):
                #For column k, subtract the scaled element in row i from row j.
                A[j,k] = A[j,k] - d*A[i,k]
            
            #Subtract scalded right hand side of row i from row j
            b[j] = b[j] - d*b[i]
        
        if 'print' in args:
            print A
            print b
        
    return A,b

