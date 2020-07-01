f = lambda x: #insert relevant function here
f_prime = lambda x: #insert derivatice of f above

def ModifiedNewtonsMethod(p0, tol, n0):
    '''
    p0: Initial guess
    tol: error tolerance
    n0: number of iterations executed
    '''
    i = 1
    while i <= n0:
        p = p0 - (((f(p0))*(f_prime(p0)))/((f_prime(p0)**2)-((f(p0))*(f_dub_prime(p0)))))
        print(p)
        if abs(p - p0) < tol:
            return p
        i += 1
        p0 = p
    return ('Method failed after ', n0, ' iterations')
