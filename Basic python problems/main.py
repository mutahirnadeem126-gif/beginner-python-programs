# game : rock paper scissors

import random
list = ["1:rock","2:papers","scissors"]
computer = random.choice(list)
you = input(f"Enter your choice,{list}")

if you == computer:
    print("It,s a Draw")
elif you == "rock" and computer == "scissors":
    print("You Wins!")
elif you == "scissors" and computer == "paper":
    print("You Wins!")
elif you == "paper" and computer == "rock":
    print("You Wins!") 

elif computer == "rock" and you == "scissors":
    print("You Lose!")
elif computer == "scissors" and you == "paper":
    print("You Lose!")
elif computer == "paper" and you == "rock":
    print("You Lose!") 

else:
    print("invalid choice!")


