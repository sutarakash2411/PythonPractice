# Generate random number
from random import randint
answer = randint(1, 100)

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Decide the game level - easy or hard
def set_difficulty():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level.lower() == 'easy':
            return EASY_LEVEL_ATTEMPTS
        elif level.lower() == 'hard':
            return HARD_LEVEL_ATTEMPTS
        else:   
            print("Invalid input. Please choose either 'easy' or 'hard'.")

# Function to check if random number and users' guess matches
def check_answer(guess, answer, attempts):
    """Checks the user's guess against the answer and returns the number of attempts remaining."""
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1   
    else:
        print(f"Congratulations! You guessed the number correctly. The number was {answer}.")

def game():
    attempts = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
    #let the user make a guess
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print(f"You've run out of guesses. You lose. The number was {answer}.")
            return
        elif guess != answer:
            print("Guess again.")
game()