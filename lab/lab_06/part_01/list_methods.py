sample_list = [ 2, 1, 3, 5, 4, 3, 8 ]

print("Our sample list: ", sample_list)

del sample_list[2]
print("After applying del on index 2: ", sample_list)

sample_list.remove(4)
print("After applying remove on element 4: ", sample_list)

sample_list.sort()
print("After applying sort: ", sample_list)

sample_list.insert(4, 100)
print("After inserting 100 at 4th index: ", sample_list)

sample_list.pop()
print("After applying pop: ", sample_list)

sample_list.extend([ "a", "b", "c" ]) # type: ignore
print("After applying extend: ", sample_list)