import math

def calculate_height(length, degree_angle):
    angle_in_radians = math.pi * (degree_angle / 180)
    height = length * math.sin(angle_in_radians)

    return height

lengths_and_angles = (
    (16, 75),
    (20, 0),
    (24, 45),
    (24, 80)
)

for ladder_length, angle_from_ground in lengths_and_angles:
    ladder_height = calculate_height(ladder_length, angle_from_ground)

    print("The height of ladder of length " + str(ladder_length) + " feet and at an angle of " + str(angle_from_ground) + "° from the ground is: " + str(ladder_height) + " feet")