SUBJECTS = 5

student_name = input("Enter your name: ")
father_name = input("Enter your Father's name: ")
# Roll numbers do not need to be integers
roll_no = input("Enter your roll number: ")

subject_names = []
subject_scores = []

for i in range(1, SUBJECTS + 1):
    subject_name = input("Enter your subject " + str(i) + ": ").casefold().capitalize()
    # Needs to be converted into integer as we need to calculate a total score later on
    subject_score_str = 0

    while True:
        subject_score_str = int(input("Enter your marks for subject " + str(i) + " (" + subject_name + ") (Out of 100): "))

        # We don't want a non-desired value, so we'll add some checks and ask again if it is not desired
        if subject_score_str > -1 and subject_score_str < 101:
            break
        else:
            print("You have a score that is out of bounds. Please enter the score again.")

    subject_names.append(subject_name)
    subject_scores.append(subject_score_str)


# We can get creative here
# I'm going to use some out of syllabus Python methods and concepts here

# To "vertically align" the columns, we need to add spaces according to the longest row

""" When the table rows are longer, then the name row is center aligned


                  Report Card

      Name: Joe        Father's Name: Jake

Subject             Score    Grade    Percentage
English             84       A        84%
Mathematics         78       B        78%
Computer Science    91       A+       91%
Physics             73       B        73%
Chemistry           69       C        69%

Overall             79       C        79%
"""

""" When the name row is longer, then the table is center aligned


                        Report Card

Name: Albert Einstein        Father's Name: Hermann Einstein

      Subject             Score    Grade    Percentage
      English             84       A        84%
      Mathematics         78       B        78%
      Computer Science    91       A+       91%
      Physics             73       B        73%
      Chemistry           69       C        69%

      Overall             79       C        79%
"""

subject_lengths = list(map(lambda subject: len(subject), subject_names))
subject_column_padding = " " * (max(max(subject_lengths), 7) - 3)

column_names_row = "Subject" + subject_column_padding + "Score    Grade    Percentage"
names_row = "Name: " + student_name + "        Father's Name: " + father_name

title_padding = " "
names_padding = " "
table_padding = " "

if len(names_row) > len(column_names_row):
    title_padding *= (len(names_row) - 11) // 2
    names_padding = ""
    table_padding *= (len(names_row) - len(column_names_row)) // 2
else:
    title_padding *= (len(column_names_row) - 11) // 2
    names_padding *= (len(column_names_row) - len(names_row)) // 2
    table_padding = ""

print()
print()
print(title_padding + "Report Card")
print()
print(names_padding + names_row)
print()
print(table_padding + column_names_row)

grade_mappings = [ "F", "F", "F", "F", "E", "D", "C", "B", "A", "A+"]

def generate_subject_row(subject_name, subject_score):
    subject_padding = " " * ((len(subject_column_padding) + 7) - len(subject_name))
    subject_name_padded = subject_name + subject_padding

    subject_score_str = str(subject_score)
    # If subject score is a single digit, then make it double digit by adding a 0
    if len(subject_score_str) == 1:
        subject_score_str = "0" + subject_score_str
    subject_score_padded = subject_score_str + (" " * 7)

    # Grades are converted from out of 100 to out of 10
    # Integer division rounds the number down
    # Scores from 90 to 100 correspond to 9, from 80 to 89 correspond to 8, etc
    # I have then created a list where the 9th index is A+, 8th index is A, etc
    subject_grade = grade_mappings[subject_score // 10]
    subject_grade_padding = " " * (9 - len(subject_grade))
    subject_grade_padded = subject_grade + subject_grade_padding

    subject_percentage = subject_score_str + "%"

    return table_padding + subject_name_padded + subject_score_padded + subject_grade_padded + subject_percentage

for i in range(SUBJECTS):
    print(generate_subject_row(subject_names[i], subject_scores[i]))

print()
print(generate_subject_row("Overall", sum(subject_scores) // len(subject_scores)))
