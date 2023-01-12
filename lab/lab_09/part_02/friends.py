friends = set()

print("Please first provide the name of your friends")
print("You will be asked if you want to provide more")
while True:
    friend = input("\nEnter your friend's name: ").casefold().title()
    friends.add(friend)

    again = input("Do you want to provide more names? Enter y or n: ").casefold()
    if again != "y":
        break

print("Your friend names are: ", friends, end="\n\n")

print("Now provide the names of two of these friends who have left NED")
target_friends = len(friends) - 2
while len(friends) > target_friends:
    left_friend = input("\nEnter the name of a friend that has left NED: ").casefold().title()

    if not left_friend in friends:
        print("This friend is not in your friends list!")
    else:
        friends.remove(left_friend)
        print("Your friends are now: ", friends)