import time

part_a_time = time.strftime("%A, %B %d %Y", time.localtime())
print("Part A time is: " + part_a_time)

part_b_time = time.strftime("%I:%M %p %Z on %m/%d/%Y")
print("Part B time is: " + part_b_time)

part_b_time = time.strftime("I will meet you on %a %B %d at %I:%M %p")
print("Part C time is: " + part_b_time)
