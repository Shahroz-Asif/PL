def duplicates(filename):
    with open(filename, "r") as my_file:
        all_words = my_file.read().casefold().split(" ")
        set_of_words = set(all_words)
        has_duplicates = len(all_words) != len(set_of_words)

        print("Has Duplicates? " + str(has_duplicates))

provided_filename = input("Enter the name of the file: ")
duplicates(provided_filename)