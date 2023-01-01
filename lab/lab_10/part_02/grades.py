def distribution(filename):
    grades = {}

    with open(filename, "r") as grades_file:
        all_grades = grades_file.readline().split(" ")

        for grade in all_grades:
            if grade not in grades:
                grades[grade] = 1
            else:
                grades[grade] += 1

        for grade, occurences in grades.items():
            print("The amount of students who got " + grade + " are: " + str(occurences))

provided_filename = input("Enter the name of the file: ")
distribution(provided_filename)