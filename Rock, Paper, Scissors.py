
# Rock, Paper, Scissors game with basic functionality
# 1 - rock; 2 - paper; 3 - scissors;


import random

def user_input():
    print("Choose your fighter wisely. Type 1 to go with rock, 2 for paper and 3 for scissors")
    user_choice = input()
    user_choice = int(user_choice)
    return user_choice

def computer_choice():   
    comp_choice = random.randrange(1,4)
    comp_choice = int(comp_choice)
    return comp_choice

def game_logic(user, computer):
    if user == computer:
        print("Great minds think alike! It's a tie!")
    elif user == 1:
        if computer == 3:
            print("That's a win! Rock destroys scissors!")
        else:
            print("That's unfortunate but you've lost! Paper covers rock!")
    elif user == 2:
        if computer == 1:
            print("That's a win! Paper covers rock!")
        else:
            print("That's unfortunate but you've lost! Scissors cuts paper into tiny pieces!")
    elif user == 3:
        if computer == 2:
            print("That's a win! Scissors cuts paper into tiny pieces!")
        else:
            print("That's unfortunate but you've lost! Rock destroys scissors!")


game_logic(user_input(), computer_choice())
