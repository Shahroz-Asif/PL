def to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

fahrenheit_temp = int(input("Enter your temperature in Degree Fahrenheit: "))
celsius_temp = to_celsius(fahrenheit_temp)

print("Your temperature in Degree Celsius is " + str(celsius_temp))
