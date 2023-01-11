phonebook = {
    "John": 958535444,
    "Joe": 564644354,
    "Jane": 354856434,
    "Jill": 534535433,
    "Jack": 534541343,
    "Joseph": 687654356,
    "Jennifer": 244435343,
    "Jacqueline": 242434345,
    "Jimmy": 976765746,
    "Jordan": 687453435,
    "Jake": 554443543,
    "Josh": 245343543
}

def remove_number(name):
    del phonebook[name]

print("The phonebook: ", phonebook, end="\n\n")

name_to_remove = input("Enter the name of the person whose number you want to remove: ")
remove_number(name_to_remove)

print("The phonebook after removal of " + name_to_remove + ": ", phonebook)