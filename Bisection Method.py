
f=lambda x: #Insert relevant function here

def BisectionMethod(a, b, tol, n0):
    '''
    a: start point of domain
    b: endpoint of domain
    tol: error tolerance
    n0: Number of iterations executed
    '''
    i = 1
    FA = f(a)
    while i <= n0:
        p = a + (b - a)/2
        print(p)
        FP = f(p)
        if FP == 0 or (b - a)/2 < tol:
            return p
        i += 1
        if FA*FP > 0:
            a = p
            FA = FP
        else:
            b = p
    return ('Method failed after ', n0, ' iterations')
