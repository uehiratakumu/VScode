# Initialize the coefficient matrix and the right-hand side vector
a = [[0]*3 for i in range(3)]
b = [0]*3

# Read input values for the matrix and vector
for i in range(3):
    a[i][0], a[i][1], a[i][2], b[i] = map(float, input().split())

# Perform Gaussian elimination
for i in range(3):
    # Pivot selection
    max_row = i
    for j in range(i+1, 3):
        if abs(a[j][i]) > abs(a[max_row][i]):
            max_row = j
    a[i], a[max_row] = a[max_row], a[i]
    b[i], b[max_row] = b[max_row], b[i]
    
    # Elimination
    for j in range(i+1, 3):
        factor = a[j][i] / a[i][i]
        for k in range(i+1, 3):
            a[j][k] -= factor * a[i][k]
        b[j] -= factor * b[i]

# Back-substitution
z = b[2] / a[2][2]
y = (b[1] - a[1][2]*z) / a[1][1]
x = (b[0] - a[0][1]*y - a[0][2]*z) / a[0][0]

# Output the solution
print("{:.10f}".format(x))
print("{:.10f}".format(y))
print("{:.10f}".format(z))
