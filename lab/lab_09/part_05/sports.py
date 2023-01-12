students = set()
students.update(range(40))

hockey = set()
hockey.update(range(21))

both = set()
both.update(range(10))

cricket = set()
cricket.update(range(len(students) - len(hockey) - len(both)))

print("The amount of students that only play cricket is: " + str(len(cricket)))