import random

names = [ "Joe", "Jack", "Jake", "Jim", "Jenny", "Jordan" ]

print("List of intial names: ", names)

names.pop()
remaining_names = names[:]

print("List of remaining names: ", remaining_names)

scholarship = random.sample(remaining_names, 2)

print("Students who are getting scholarship: " + " and ".join(scholarship))