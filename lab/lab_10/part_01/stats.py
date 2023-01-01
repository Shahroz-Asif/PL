def stats(filename):
    with open(filename, "r") as my_file:
        # Returns a list containing all the lines in the file
        file_lines = my_file.readlines()

        word_count = 0
        character_count = 0

        # The logic here is that for each line, the number of words is always one more than the number of spaces
        for line in file_lines:
            character_count += len(line)

            space_count = line.count(" ")
            word_count += space_count + 1

        print("The number of lines in the file is", len(file_lines))
        print("The total number of words in the file is", word_count)
        print("The total number of characters in the file is", character_count)

provided_filename = input("Enter the name of the file: ")
stats(provided_filename)
