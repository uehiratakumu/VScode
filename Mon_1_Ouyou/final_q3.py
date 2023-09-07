# Parameters
N_x = 32  # x-axis divisions
N_t = 10000  # t-axis divisions (set to make Δt = 1e-4)
x_range = [-1, 1]
t_range = [0, 1]

# Calculation of Δx, Δt
dx = (x_range[1] - x_range[0]) / (N_x - 1)
dt = (t_range[1] - t_range[0]) / (N_t - 1)

# Grid Initialization
u = [[0 for _ in range(N_x)] for _ in range(N_t)]

# Initial condition settings
for i in range(N_x):
    x = x_range[0] + i * dx
    u[0][i] = 1 - x**2

# Time integration by Crank-Nicolson method
for j in range(N_t - 1):
    # Create tridiagonal matrix
    A = [[(1 + dt / (2 * dx**2)) if i == j else (-dt / (4 * dx**2)) if abs(i - j) == 1 else 0 for i in range(N_x)] for j in range(N_x)]
    B = [[(1 - dt / (2 * dx**2)) if i == j else (dt / (4 * dx**2)) if abs(i - j) == 1 else 0 for i in range(N_x)] for j in range(N_x)]
    
    # Boundary condition settings
    A[0][0] = A[-1][-1] = 1
    B[0][0] = B[-1][-1] = 1
    A[0][1] = A[-1][-2] = 0
    B[0][1] = B[-1][-2] = 0
    
    # Right-hand side calculation
    b = [sum(B[i][k] * u[j][k] for k in range(N_x)) for i in range(N_x)]
    
    # Solve the tridiagonal matrix (Thomas Algorithm)
    c = [0 for _ in range(N_x)]
    d = [0 for _ in range(N_x)]
    for i in range(1, N_x - 1):
        c[i] = A[i][i+1] / (A[i][i] - A[i][i-1] * c[i-1])
        d[i] = (b[i] - A[i][i-1] * d[i-1]) / (A[i][i] - A[i][i-1] * c[i-1])
    
    # Update the solution by back substitution
    u[j+1][-1] = d[-1]
    for i in range(N_x - 2, -1, -1):
        u[j+1][i] = d[i] - c[i] * u[j+1][i+1]

# Output the value of u(x = 0, t = 1)
print(f"{u[-1][N_x // 2]:.8f}")
