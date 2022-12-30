starting_number = int(input("Enter your starting number: "))
ending_number = int(input("Enter your ending number: "))

for i in range(starting_number, ending_number + 1):
    for j in range(starting_number, ending_number + 1):
        print(i * j, end=" ")

    print()