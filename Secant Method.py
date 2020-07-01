f = lambda x: #Insert relevant function here

def SecantMethod(p0, p1, tol, n0):
    '''
    p0: Initial guess
    p1: Second initial guess
    tol: error tolerance
    n0: number of iterations to execute
    '''
    
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    while i <= n0:
        p = p1 - (q1*(p1-p0))/(q1-q0)
        if abs(p-p1) < tol:
            return p
        i += 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
        print(p)
    
    return ('Method failed after ', n0, ' iterations')
