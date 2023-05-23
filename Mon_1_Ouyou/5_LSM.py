# Read the number of data points
num_points = int(input())

# Initialize variables for coefficient sums
sum_0 = sum_x = sum_y = sum_xy = sum_x2 = sum_y2 = sum_z = sum_xz = sum_yz = 0.0

# Read the data points and calculate the coefficient sums
for _ in range(num_points):
    x, y, z = map(float, input().split())
    sum_0 += 1
    sum_x += x
    sum_y += y
    sum_xy += x * y
    sum_x2 += x ** 2
    sum_y2 += y ** 2
    sum_z += z
    sum_xz += x * z
    sum_yz += y * z

# Calculate the coefficients
denominator = num_points * sum_x2 * sum_y2 + 2 * sum_x * sum_xy * sum_y - sum_x2 * sum_y ** 2 - num_points * sum_xy ** 2 - sum_x ** 2 * sum_y2
a0 = (sum_z * sum_x2 * sum_y2 + sum_x * sum_xy * sum_yz * sum_y - sum_x * sum_y2 * sum_xz - sum_z * sum_xy ** 2 - sum_xz * sum_x2 * sum_y) / denominator
a1 = (num_points * sum_xz - sum_z * sum_x) / denominator
a2 = (num_points * sum_yz - sum_z * sum_y) / denominator
a3 = (num_points * sum_x2 * sum_yz + sum_x * sum_xy * sum_z - sum_x * sum_y * sum_xz - num_points * sum_xy * sum_z - sum_x2 * sum_y * sum_yz) / denominator
a4 = (-num_points * sum_xy * sum_yz + sum_y * sum_xz * sum_x2 - sum_z * sum_x * sum_y2 + num_points * sum_z * sum_xy - sum_x2 * sum_yz * sum_x) / denominator
a5 = (-num_points * sum_xz * sum_y2 + sum_z * sum_yz * sum_x2 - sum_x * sum_y * sum_z + num_points * sum_xy * sum_z - sum_x2 * sum_y * sum_z) / denominator

# Print the coefficients
print("{:.6f}".format(a0))
print("{:.6f}".format(a1))
print("{:.6f}".format(a2))
print("{:.6f}".format(a3))
print("{:.6f}".format(a4))
print("{:.6f}".format(a5))
