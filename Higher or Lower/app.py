import art
from game_data import data
import random

def format_data(account):
    """format the account data into printable format"""
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return  user_guess == "b"

print(art.logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{format_data(account_a)}\n")
    print(f"vs {art.vs}")
    print(f"Against B:{format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(art.logo)

    a_follower_account = account_a['follower_count']
    b_follower_account = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_account, b_follower_account)

    if is_correct:
        score += 1
        print(f"You're right! Current Score {score}")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        game_should_continue = False







