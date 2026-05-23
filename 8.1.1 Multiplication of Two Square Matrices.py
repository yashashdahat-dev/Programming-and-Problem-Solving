# Matrix Multiplication Program

# Read dimension
n = int(input("dimension: "))

# Read first matrix
print("first matrix:")
first_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    first_matrix.append(row)

# Read second matrix
print("second matrix:")
second_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    second_matrix.append(row)

# Initialize result matrix with zeros
result = [[0 for _ in range(n)] for _ in range(n)]

# Perform matrix multiplication
for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += first_matrix[i][k] * second_matrix[k][j]

# Print the resultant matrix
print("Resultant Matrix:")
for row in result:
    print(" ".join(map(str, row)))
