import random
import os

def deal_card():
    """deals a random card from card list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """calculates score based on cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    """compares user and computer score"""
    if c_score == u_score:
        print("Draw!")
    elif c_score == 0:
        print("Dealer has blackjack! You lose")
    elif u_score == 0:
        print("Blackjack! You win:")
    elif u_score > 21:
        print("Bust! You lose")
    elif c_score > 21:
        print("Dealer's bust! You win")
    else:
        if u_score > c_score:
            print("You win!")
        else:
            print("You lose!")

def main(): 
    # lists for user and computer cards
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    # deal a two cards for user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score = {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            hit_or_stand = input("Do you want another card? 'h' for hit or 's' for stand: ")
            if hit_or_stand == "h":
                user_cards.append(deal_card())
                calculate_score(user_cards)
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {computer_cards}, final score: {computer_score}")
    compare(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
   os.system('clear')    
   main()
 