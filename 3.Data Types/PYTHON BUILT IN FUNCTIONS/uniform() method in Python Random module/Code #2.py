# Python3 code to demonstrate
# the application of uniform()

# for using uniform()
import random, math

# initializing player numbers
player1 = 4.50
player2 = 3.78
player3 = 6.54

# generating winner random number
winner = random.uniform(2, 9)

# finding closest
diffa = math.fabs(winner - player1)
diffb = math.fabs(winner - player2)
diffc = math.fabs(winner - player3)

# printing winner
if (diffa < diffb and diffa < diffc):
    print("The winner of game is : ", end="")
    print("Player1")

if (diffb < diffc and diffb < diffa):
    print("The winner of game is : ", end="")
    print("Player2")

if (diffc < diffb and diffc < diffa):
    print("The winner of game is : ", end="")
    print("Player3")
