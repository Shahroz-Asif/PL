def calculate_area(breadth, height):
    return breadth * height

given_breadth = int(input("Enter your rectangle's breadth: "))
given_height = int(input("Enter your rectangle's height: "))
area_of_rectangle = calculate_area(given_breadth, given_height)

print("Your rectangle's area is " + str(area_of_rectangle))
