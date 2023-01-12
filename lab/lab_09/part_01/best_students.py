position_mappings = ( "first", "second", "third", "fourth", "fifth" )
best_students = set()

while len(best_students) < 5:
    student_number = len(best_students)
    student_name = input("\nEnter your " + position_mappings[student_number] + " best student's name: ")

    best_students.add(student_name)

    if len(best_students) == student_number:
        print("Oops! You have repeated a student's name. Please try again.")

print()
print("The final set of best students is: ", best_students)