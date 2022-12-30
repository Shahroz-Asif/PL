sample_list = [ 2, 1, 3, 5, 4, 3, 8 ]

print("Our sample list: ", sample_list)

# Part A - Index of middle element
middle_index = 0

if len(sample_list) % 2 == 0:
    middle_index = (len(sample_list) + 1) // 2
else:
    middle_index = len(sample_list) // 2

print("The index of the middle element of list of length " + str(len(sample_list)) + " is: " + str(middle_index))

# Part B - Middle Element
middle_element = sample_list[middle_index]

print("The middle element of this list is " + str(middle_element))

# Part C - Sort in descending order
sample_list.sort()
sample_list.reverse()

print("The list sorted in descending order is: ", sample_list)

# Part D - Remove first element and add it to last
first_element = sample_list[0]
sample_list = sample_list[1:]
sample_list.append(first_element)

print("The list after shifting the first element to the last position is: ", sample_list)