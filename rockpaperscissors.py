import random

possible_choices = ['rock', 'paper' , 'scissors']

computer_choice = random.choice(possible_choices)

user_choice = input("rock, paper, or scissors?")

if user_choice == computer_choice:
    print("Tie")
elif user_choice == "rock" and computer_choice == "paper":
    print("computer wins")
elif user_choice == "paper" and computer_choice == "scissors":
    print("computer wins")
elif user_choice == "scissors" and computer_choice == "rock":
    print("computer wins")
else:
    print("you win :P")

#test