# Casefold to remove uppercase and lowercase issues
given_string = input("Enter a string to check if it is a palindrome or not: ").casefold()

is_palindrome = True

for i in range(len(given_string) // 2):
    if not given_string[i] == given_string[len(given_string) - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")
