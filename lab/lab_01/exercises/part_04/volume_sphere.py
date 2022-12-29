import math

def calculate_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)

given_radius = int(input("Enter your sphere's radius: "))
sphere_volume = calculate_volume(given_radius)

print("Your sphere's volume is " + str(sphere_volume))
