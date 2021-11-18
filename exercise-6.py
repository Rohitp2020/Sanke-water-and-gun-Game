## Sanke, water and gun Game

import random
print("Hello there, Welcome to our 'Snake, Water and Gun' game:")
print("For (Snake) type 's'\nFor (Water) type 'w'\nFor (Gun) type 'g'\n")
count = 10
i = ['s','w','g']
ComputerWinCount = 0
YourWinCount = 0

while (count != 0):
    ent = input("You can enter anyone from [s, w, g] here: ")
    if ent.lower() in i:
        ComputerChoice = random.choice(i)
        count -= 1
        if ent == ComputerChoice:
            print("Sorry! its a tie between you and computer, try again.")
        elif ComputerChoice == 's' and ent.lower() == 'w':
            print(f"Sorry! Computer won by choosing {ComputerChoice}")
            ComputerWinCount += 1
        elif ComputerChoice == 'w' and ent.lower() == 'g':
            print(f"Sorry! Computer won by choosing {ComputerChoice}")
            ComputerWinCount += 1
        elif ComputerChoice == 'g' and ent.lower() == 's':
            print(f"Sorry! Computer won by choosing {ComputerChoice}")
            ComputerWinCount += 1
        else:
            print(f"Hey! You won as computer choose {ComputerChoice}")
            YourWinCount += 1
    else:
        print("Sorry! You have entered wrong word: ",ent)

if ComputerWinCount > YourWinCount:
    print(f"Sorry! You lose by {ComputerWinCount-YourWinCount} points.")
elif ComputerWinCount == YourWinCount:
    print("Hey! Its a tie between You and Computer.")
else:
    print(f"Congratulations! You won this Game by {YourWinCount-ComputerWinCount} points.")




