def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

i = 0
while i <= 10:
    result = factorial(i)
    print("The factorial of " + str(i) + " is: ", str(result))

    i += 1