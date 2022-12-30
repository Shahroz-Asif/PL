# Two rectangles
row_of_asterisk = "*" * 14
indentation = " " * 18

square_row = 0
while square_row < 8:
    if square_row < 4:
        print(row_of_asterisk)
    else:
        print(indentation + row_of_asterisk)
    
    square_row += 1

print()

# Triangle
triangle_row = 0
while triangle_row < 8:
    triangle_row += 1
    print("*" * triangle_row)

print()

# Inverse Triangle
inverse_triangle_row = 8
while inverse_triangle_row > 0:
    print("*" * inverse_triangle_row)
    inverse_triangle_row -= 1