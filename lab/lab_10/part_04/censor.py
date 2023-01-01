def abc(filename):
    read_word_lines = []
    lines_to_write = []

    with open(filename, "r") as reading_file:
        read_lines = reading_file.readlines()

        for line in read_lines:
            read_word_lines.append(line.split(" "))

    for word_line in read_word_lines:
        writing_line = []

        for word in word_line:
            if len(word.casefold()) == 4:
                writing_line.append("xxxx")
            else:
                writing_line.append(word)

        lines_to_write.append(" ".join(writing_line))


    with open("abc.txt", "x") as writing_file:
        writing_file.writelines(lines_to_write)

given_filename = input("Enter the name of the file: ")
abc(given_filename)