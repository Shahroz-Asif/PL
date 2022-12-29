number_of_years = int(input("Enter the amonut of years you've worked for: "))
monthly_pay = int(input("Enter your monthly pay: "))

DECADE_BONUS = 2500
bonus = (number_of_years * (0.5 * monthly_pay)) + (max(0, number_of_years - 10) * DECADE_BONUS)

print("Your bonus is: " + str(bonus))
