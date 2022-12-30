def to_fahrenheit(celsius):
    return (celsius * (9 / 5)) + 32

celsius_temp = int(input("Enter your temperature in Degree Celsius: "))
fahrenheit_temp = to_fahrenheit(celsius_temp)

print("Your temperature in Degree Fahrenheit is " + str(fahrenheit_temp))
