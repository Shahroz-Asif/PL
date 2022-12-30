first_term = int(input("Enter the first term of your sequence: "))
common_difference = int(input("Enter the common difference of your sequence: "))

while True:
    decision = input("Do you want to continue calculating an nth term? If yes, please reply with 'yes': ").casefold()

    if not decision == "yes":
        break

    term = int(input("Enter the term number you want to calculate: "))
    nth_term = first_term + (common_difference * (term - 1))

    print("The nth term of the " + str(term) + "th term is " + str(nth_term))