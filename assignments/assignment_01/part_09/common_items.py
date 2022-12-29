def compare_lists(list_1, list_2):
    for element in list_1:
        if element in list_2:
            return True

    return False

prompt_helpers = [ "do not", "do" ]
lists = [[], []]
        
for i in range(2):
    label = chr(65 + i)
    elements = int(input("Enter the amount of elements you want in list " + label + ": "))

    for j in range(1, elements + 1):
        element = input("Enter element " + str(j) + " for list " + label + ": ")
        lists[i].append(element)

has_common_element = compare_lists(lists[0], lists[1])
print("The lists " + prompt_helpers[int(has_common_element)] + " have at least one common element")