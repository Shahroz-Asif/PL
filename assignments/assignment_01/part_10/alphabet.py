char = input("Enter an alphabet: ")

if (len(char) > 1):
    print("You have provided a word!")
else:
    char_unicode = ord(char)

    if (char_unicode >= 65 and char_unicode <= 95) or (char_unicode >= 97 and char_unicode <= 122):
        print("The next alphabet is: " + chr(char_unicode + 1))
    else:
        print("You have provided a special character!")