LOWERCASE_A_ASCII = 97
mat_a = []
mat_b = []

# Taking input from user for each matrix (2 overall)
print("== Creating Matrix A ==")

for row_no in range(0, 3, 2):
    row = []
    for column_no in range(2):
        matrix_cell_value = int(input("Enter value for cell " + chr(LOWERCASE_A_ASCII + row_no + column_no) + ": "))
        row.append(matrix_cell_value)
    mat_a.append(row)

print("== Creating Matrix B ==")

for row_no in range(0, 3, 2):
    row = []
    for column_no in range(2):
        matrix_cell_value = int(input("Enter value for cell " + chr(LOWERCASE_A_ASCII + row_no + column_no) + ": "))
        row.append(matrix_cell_value)
    mat_b.append(row)

# Calculating matrix multiplication by individually multiplying and adding the cells
mat_c = [
   [ (mat_a[0][0] * mat_b[0][0]) + (mat_a[0][1] * mat_b[1][0]), (mat_a[0][0] * mat_b[0][1]) + (mat_a[0][1] * mat_b[1][1]) ],
   [ (mat_a[1][0] * mat_b[0][0]) + (mat_a[1][1] * mat_b[1][0]), (mat_a[1][0] * mat_b[0][1]) + (mat_a[1][1] * mat_b[1][1]) ]
]

print("The result of matrix multiplication of A and B is:", mat_c)

