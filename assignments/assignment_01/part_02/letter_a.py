def print_a():
    for row in range(7):
        for column in range(4):
            if column in [1, 2]:
                if row in [0, 3]:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            else:
                if row == 0 and column == 0:
                    print(" ", end=" ")
                else:
                    print("*", end=" ")
            
        print()

print_a()
