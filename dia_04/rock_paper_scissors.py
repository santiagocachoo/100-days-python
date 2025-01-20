import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""



print("Welcome to THE GAME")
usr_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors "))
if usr_choice == 0:
    print(rock)
elif usr_choice == 1:
    print(paper)
elif usr_choice == 2:
    print(scissors)
else:
    print("Option not valid")


computer_options = [rock, paper, scissors]
computer_choice = random.choice(computer_options)

if computer_choice == rock:
    print("Computer chose:")
    print(rock)

if computer_choice == paper:
    print("Computer chose:")
    print(paper)

if computer_choice == scissors:
    print("Computer chose:")
    print(scissors)

if (computer_choice == rock and usr_choice == 1) or (computer_choice == scissors and usr_choice == 0) or (
    computer_choice == paper and usr_choice == 2
):
    print("You win")
elif (computer_choice == rock and usr_choice == 2) or (computer_choice == scissors and usr_choice == 1) or (
    computer_choice == paper and usr_choice == 0
):
    print("You lose")
else:
    print("Its a tie")


