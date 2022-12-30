print("PART A")
message = "The secret of this message is that it is secret"

print("Value of message is: " + message, end="\n\n")

print("PART B")
length = len(message)

print("The length of variable message is: " + str(length), end="\n\n")

print("PART C")
count = message.count("secret")

print("The occurences of substring 'secret' is: " + str(count), end="\n\n")

print("PART D")
censored = message.replace("secret", "xxxxxx")

print("The message after substring 'secret' is replaced by 'xxxxxx' is: " + censored)