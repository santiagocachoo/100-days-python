import random
from game_data import data
import art
import os

def compare(user_a, user_b):
    return user_a["follower_count"] > user_b["follower_count"]

def choose_random():
    return random.choice(data)

score = 0
a = choose_random()
print(art.logo)

while True:
    b = choose_random()

    while b == a or (a["follower_count"] == b["follower_count"] and a["name"] != b["name"]):
        b = choose_random()

    print(f"Compare A: {a['name']}, {a['description']} from {a['country']}")
    print(art.vs)
    print(f"Against B: {b['name']}, {b['description']} from {b['country']}")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_guess == 'a':
        user_guess = a
        other = b
    elif user_guess == 'b':
        user_guess = b
        other = a

    #print(user_guess)

    if compare(user_guess, other) == True:
        score += 1
        os.system('clear')   
        print(f"Correct! Current score: {score}")
        a = user_guess
    else:
        print(f"Incorrect... Game over. Final score: {score}")
        break

    


    

