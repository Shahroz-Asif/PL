matrices = [[], []]

LOWERCASE_A_ASCII = 97
UPPERCASE_A_ASCI = 65

# Taking input from user for each matrix (2 overall)
for i in range(2):
    print("\n== Creating Matrix " + chr(UPPERCASE_A_ASCI + i) + " ==")

    for j in range(0, 3, 2):
        row = []

        for k in range(2):
            matrix_cell_value = int(input("Enter value for cell " + chr(LOWERCASE_A_ASCII + j + k) + ": "))
            row.append(matrix_cell_value)
        
        matrices[i].append(row)

# Summing matrices
summed_matrix = [[0, 0], [0, 0]]
for matrix in matrices:
    for i in range(2):
        for j in range(2):
            summed_matrix[i][j] += matrix[i][j]

print()

# Printing Matrix
print("Result:")
for row in summed_matrix:
    print(row)