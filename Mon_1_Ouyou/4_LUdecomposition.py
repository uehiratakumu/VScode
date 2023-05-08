# Step 1: Input matrix A from the server
A = []
for i in range(3):
    row = list(map(float, input().split()))
    A.append(row)

# Step 2: Initialize L and U as identity and zero matrices, respectively
L = [[0.0 for j in range(3)] for i in range(3)]
U = [[0.0 for j in range(3)] for i in range(3)]

# Step 3: Perform LU decomposition
     
for i in range(3):
    
    for j in range(i, 3):
        L[j][i] = A[j][i]

    # Gauss elimination
    a = A[i][i] # diagonal component
    for n in range(3):
        A[i][n] /= a

    for j in range(i + 1, 3):
        ap = A[j][i] # the (i+1, i) component
        for n in range(i, 3):
            A[j][n] -= ap * A[i][n]

# Step 4: Output the components of L and U
for i in range(3):
    for j in range(3):
        print("{:.6f}".format(L[i][j]))
for i in range(3):
    for j in range(3):
        print("{:.6f}".format(A[i][j]))
