matrices = [[], []]

LOWERCASE_A_ASCII = 97
UPPERCASE_A_ASCI = 65

# Taking input from user for each matrix (2 overall)
for i in range(2):
    print("\n== Creating Matrix "+ chr(UPPERCASE_A_ASCI + i) +" ==")

    for j in range(0, 3, 2):
        row = []

        for k in range(2):
            matrix_cell_value = int(input("Enter value for cell " + chr(LOWERCASE_A_ASCII + j + k) + ": "))  # type: ignore
            row.append(matrix_cell_value)
        
        matrices[i].append(row)

# Calculating matrix multiplication
result_matrix = []

for i in range(len(matrices[0])):
    row = []
    for j in range(len(matrices[0])):
        column = 0

        for k in range(len(matrices[0][i])):
            column += matrices[0][i][k] * matrices[1][k][j]

        row.append(column)
    result_matrix.append(row)

print()
print("Result:")
for row in result_matrix:
    print(row)
