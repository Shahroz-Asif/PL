forecast = "It will be a sunny day today"

print("PART A")
count = forecast.count("day")

print("The occurences of substring 'day' is: " + str(count), end="\n\n")

print("PART B")
weather = forecast.index("sunny")

print("The index at which substring 'sunny' starts is: " + str(weather), end="\n\n")

print("PART C")
change = forecast.replace("sunny", "cloudy")

print("The result of replacing substring 'sunny' with 'cloudy' is: " + change, end="\n\n")
