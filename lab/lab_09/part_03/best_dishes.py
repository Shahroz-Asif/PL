best_dishes = set()

print("You will be asked to enter your best dishes")
while True:
    dish = input("\nEnter your best dish: ")
    best_dishes.add(dish)

    again = input("Do you want to provide more dishes? Enter y or n: ").casefold()
    if again != "y":
        break

print()
print("Here are your best dishes:")
while len(best_dishes) != 0:
    dish = best_dishes.pop()

    print(dish)