g = lambda x: #insert relevant function here

def FixedPoint(p0, tol, n0):
    '''
    p0: Initial guess at zero
    tol: error tolerance
    n0: number of iterations executed
    '''

    
    i = 1
    while i <= n0:
        p = g(p0)
        print(p)
        if abs(p - p0) < tol:
            return p
        i += 1
        p0 = p
    return ('Method failed after',  n0, ' iterations')
