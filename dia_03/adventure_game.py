print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

# game?
left_right = input("You come across two paths, do you wish to go left or right? ").lower
if left_right == "left":
    swim_wait = input("You come across a river, do you wish to swim or wait? ").lower
    if swim_wait == "wait":
        door = input("You come across three doors: red, blue and yellow. Which one do you open? ").lower
        if door == "red":
            print("You were burned by fire\nGame Over")
        elif door == "blue":
            print("You were eaten by beasts\nGame Over")
        elif door == "yellow":
            print("You win!!!")
        else:
            print("WRONG. GAME OVER.")
    else:
        print("You've been attacked by a trout\nGame Over")
else:
    print("You fell into a hole...\nGame Over")

    



