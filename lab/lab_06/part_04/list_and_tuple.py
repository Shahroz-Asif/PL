monthsL = [ "Jan", "Feb", "Mar", "May" ]
monthsT = ( "Jan", "Feb", "Mar", "May" )

print("PART A")
try:
    monthsL.insert(3, "Apr")
    print("List after inserting Apr: ", monthsL)

    print("Attempting to insert Apr in tuple:")
    monthsT.insert(3, "Apr")
except AttributeError as err:
    print(err)
    print("Tuple after applying operation: ", monthsT, end="\n\n")

print("PART B")
try:
    monthsL.append("Jun")
    print("List after appending Jun: ", monthsL)

    print("Attempting to append Jun in tuple:")
    monthsT.append("Jun")
except AttributeError as err:
    print(err)
    print("Tuple after applying operation: ", monthsT, end="\n\n")

print("PART C")
try:
    monthsL.pop()
    print("List after applying pop: ", monthsL)

    print("Attempting to apply pop on tuple:")
    monthsT.pop()
except AttributeError as err:
    print(err)
    print("Tuple after applying operation: ", monthsT, end="\n\n")

print("PART D")
try:
    del monthsL[1]
    print("List after removing second item: ", monthsL)

    print("Attempting to remove second item in tuple:")
    del monthsT[1]
except TypeError as err:
    print(err)
    print("Tuple after applying operation: ", monthsT, end="\n\n")

print("PART E")
try:
    monthsL.reverse()
    print("List after reversing order: ", monthsL)

    print("Attempting to reverse order in tuple:")
    monthsT.reverse()
except AttributeError as err:
    print(err)
    print("Tuple after applying operation: ", monthsT, end="\n\n")

print("PART F")
try:
    monthsL.sort()
    print("List after sorting: ", monthsL)

    print("Attempting to sort the tuple:")
    monthsT.reverse()
except AttributeError as err:
    print(err)
    print("Tuple after applying operation: ", monthsT, end="\n\n")
