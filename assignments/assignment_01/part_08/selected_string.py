number_of_strings = int(input("Enter the amount of strings you want to provide: "))
selected_strings = 0

for i in range(1, number_of_strings + 1):
    given_string = input("Enter string " + str(i) + ": ")

    if len(given_string) >= 2 and given_string[0] == given_string[-1]:
        selected_strings += 1

print("The number of selected strings are: " + str(selected_strings))
