angular_speed = 523.3
radiuses = [ 0.05, 0.1 ]

for radius in radiuses:
    linear_velocity = radius * angular_speed

    print("The linear velocity of blades in blender at " + str(radius) + " meters from the center is " + str(linear_velocity) + " m/s")