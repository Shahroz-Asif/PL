angular_speed = 10
radiuses = [ 0.5, 1.0, 3.0 ]

for radius in radiuses:
    linear_velocity = radius * angular_speed

    print("The linear velocity of ball on string at " + str(radius) + " meters from the center is " + str(linear_velocity) + " m/s")