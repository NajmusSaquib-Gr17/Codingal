import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

choices = ['R', 'P', 'S']
win_conditions = {'R': 'S', 'S': 'P', 'P': 'R'}

while True:
    print("\nRock, Paper, Scissors - Shoot!")
    userChoice = input("Choose your weapon [R]ock, [P]aper, [S]cissors or [Q]uit: ").upper()

    if userChoice == 'Q':
        print("Thanks for playing!")
        break
    if userChoice not in choices:
        print("Invalid choice. Please enter R, P, S or Q.")
        continue

    print("You chose:", userChoice)
    opponentChoice = random.choice(choices)
    print("I chose:", opponentChoice)

    if opponentChoice == userChoice:
        print("It's a tie!")
    elif win_conditions[opponentChoice] == userChoice:
        print(f"{opponentChoice} beats {userChoice}, I win!")
    else:
        print(f"{userChoice} beats {opponentChoice}, you win!")
