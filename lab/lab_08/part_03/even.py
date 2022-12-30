def even(n):
    if n < 2:
        return

    for i in range(2, n + 1):
        if i % 2 == 0 or i % 3 == 0:
            print(i, end=", ")

given_number = int(input("Enter your number: "))
even(given_number)