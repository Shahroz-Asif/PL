months = "JanFebMarAprMayJunJulAugSepOctNovDec"
def month(month_number):
    start_index = (month_number - 1) * 3
    end_index = month_number * 3

    return months[start_index:end_index]

given_month_number = int(input("Enter your month number: "))
month_abberviation = month(given_month_number)

print("The abberviation of month " + str(given_month_number) + " is: " + month_abberviation)