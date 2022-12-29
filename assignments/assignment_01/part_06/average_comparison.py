prompt_helpers = [ "first", "second", "third", "last" ]
given_numbers = []

for i in range(4):
    given_number = float(input("Enter your " + prompt_helpers[i] + " number: "))
    given_numbers.append(given_number)

total = sum(given_numbers[:3])
average = total / 3
if average == given_numbers[-1]:
    print("Equal")