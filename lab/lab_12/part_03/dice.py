import random

dice1 = [ i for i in range(1, 7) ]
dice2 = [ i for i in range(1, 7) ]

print("The dice played for player 1 is: " + str(random.choice(dice1)))
print("The dice played for player 2 is: " + str(random.choice(dice2)))