def cheer(team):
    print("How do you spell a winner?")
    print("I know, I know!")

    for char in team.upper():
        print(char, end=" ")
    print("!")

    print("And that's how you spell winner!")
    print("Go " + team.title() + "!")

given_team = input("Enter your team name: ")
cheer(given_team)