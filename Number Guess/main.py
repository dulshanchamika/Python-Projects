from random import randint
from wsgiref.util import guess_scheme

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users guess against the actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess and returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The actual answer was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(0,100)
    print(answer)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess : "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of attempts. You lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()