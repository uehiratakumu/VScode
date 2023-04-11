import sys

def f(x):
    return x**3 - 3*x**2 + 9*x - 8

def bisection(a, b, tol):
    while (b-a)/2 > tol:
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

a,b = map(float, input().split())
tol = 1e-7

root = bisection(a, b, tol)

print('{:.07f}'.format(root))
