from art import logo, vs
from data import info
import random
#Print the logoo
print(logo)
account_b=random.choice(info)

def check_answer(guess, a_followers, b_followers):
    """ check the followers against user's guess and return True if they got it right. Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

score=0 
game_should_continue=True
print("=== GAME STARTED ===")
while game_should_continue:
    #get random account details
    account_a=account_b
    account_b=random.choice(info)
    if account_a==account_b:
        account_b=random.choice(info)

    def format_data(account):
        """Takes the account data and returns the printable format."""
        name=account['name']
        description=account['description']
        country=account['country']
        return f"{name}, a {description}, from {country}"

    #Display account details to user
    print(f"Compare A:{format_data(account_a)} ")
    print(vs)
    print(f"Against B: {format_data(account_b)} ")

    #Ask user for a guess
    guess=input("Who has more followers? Type 'A' or 'B': ").lower()   

    #clear the screen between rounds
    

    #Check if user is correct
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]

    is_correct=check_answer(guess, a_follower_count, b_follower_count) 
    #Score keeping
       
    #Give user feedback on their guess
    if is_correct:
        score+=1
        print(logo)
        print(f"You are right! Current score:{score}")
        # print("\n" * 100)
       
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        game_should_continue=False
        
      
   