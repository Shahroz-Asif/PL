triangle_types = [ "scalene", "isoceles", "equilateral" ]
triangle_sides = []

for i in range(3):
    side_length = int(input("Enter the length for side " + chr(65 + i) + ": "))
    triangle_sides.append(side_length)

# Loop counts the amount of matching side pairs
# 0 for scalene, 1 for isoceles, and 2 for equilateral
equal_sides_count = 0
for i in range(len(triangle_sides) - 1):
    for j in range(i + 1, len(triangle_sides)):
        if triangle_sides[i] == triangle_sides[j]:
            equal_sides_count += 1

print("Your triangle is", triangle_types[min(2, equal_sides_count)])
