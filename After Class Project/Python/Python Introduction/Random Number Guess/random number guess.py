import random

def guessTheNumber():
    number = random.randint(1, 10)
    attempts = 3

    while attempts > 0:
        try:
            guess = int(input("Guess a number between 1 and 10: "))

            if guess < 1 or guess > 10:
                print("Out of range! Please enter a number between 1 and 10.")
                continue

        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 10.")
            continue

        if guess == number:
            print("Congratulations! Your guess was correct!")
            return

        attempts -= 1  

        if guess < number:
            print(f"Wrong guess! The number is higher. Attempts left: {attempts}")
        else:
            print(f"Wrong guess! The number is lower. Attempts left: {attempts}")

    print(f"You failed! Correct Number = {number}")

guessTheNumber()
