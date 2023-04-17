import math

# Define the two functions
def f(x):
    return 2 - x**2

def g(x):
    return math.exp(x)

# Define the derivative of f(x)
def df(x):
    return -2*x

# Define the derivative of g(x)
def dg(x):
    return math.exp(x)

# Define the Newton's method
def newton(f, df, x0, eps=1e-6):
    x = x0
    while True:
        fx = f(x)
        if abs(fx) < eps:
            return x
        dfx = df(x)
        if dfx == 0:
            return None
        x = x - fx/dfx

# Get the initial value from the user
x0 = float(input())

# Use Newton's method to find the intersection point
x = newton(lambda x: f(x) - g(x), lambda x: df(x) - dg(x), x0)

# Print the result
print('{:.06f}'.format(x))
