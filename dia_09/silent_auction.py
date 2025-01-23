buyers = {}


print("Welcome to the secret auction program")
while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    buyers[name] = bid
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if continue_bid == "yes":
        pass
    elif continue_bid == "no":
        highest_bid = 0
        winner = ""
        for buyer in buyers:
            if buyers[buyer] > highest_bid:
                highest_bid = buyers[buyer]
                winner = buyer
        print(f"The winner is {winner} with a bid of ${highest_bid}")
        break
    
