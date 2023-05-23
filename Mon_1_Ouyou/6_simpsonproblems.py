def f(x):
    return 1 / (1 + x**2)

def simpsons_rule():
    a = 0  # Lower limit
    b = 1  # Upper limit
    n = 1024  # Number of sub-intervals
    h = (b - a) / n  # Width of each sub-interval

    # Evaluate function values at the specified points within each sub-interval
    points = [f(a + i * h) for i in range(n + 1)]
    # Apply Simpson's rule formula
    integral = (h / 3) * (points[0] + 4 * sum(points[i] for i in range(1, n, 2)) + 2 * sum(points[i] for i in range(2, n, 2)) + points[n])

    return integral

# Calculate the definite integral
result = simpsons_rule()

# Print the result with up to 10 digits after the decimal point
print("{:.10f}".format(result))
