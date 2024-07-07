import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2 
    SCISSORS = 3 


print('')
playerchoice = input("Enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors: \n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("Input must be 1,2, or 3.")

computerchoice = random.choice("123")

computer = int(computerchoice)

print('')
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

if player == 1 and computer == 3:
    print("😄 You won! Good job!")
elif player == 2  and computer == 1:
    print("😄 You won! Good job!")
elif player == 3  and computer == 2:
    print("😄 You won! Good job!")
elif player == computer:
    print("🤝 It's a tie!")
else:
    print("🐍 Python won! Better luck next time!")
    