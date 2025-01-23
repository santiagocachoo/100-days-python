import random 
from word_list import words
from ascii_art import HANGMANPICS

# choose random word
chosen_word = random.choice(words)
print(chosen_word)

# create word display
display = []
for letter in chosen_word:
    display.append("_")

# print placeholder as string
print(f"YOUR WORD IS: {"".join(display)}\n")

# lives variable
lives = 6

# game loop
while "_" in display:
    # ask user guess
    guess = input("Guess a letter: ").lower()
    

    # for loop to check if guess is in chosen word, if so, add it to the placeholder in the right place
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess

    # if guess is in word, let user know
    if guess in chosen_word:
        print("CORRECT!")
    
    # if the guessed letter is not in the word, remove one life
    if guess not in chosen_word:
        lives -= 1
        print("LETTER NOT IN WORD, YOU LOSE A LIFE")
    

    # art
    if lives == 6:
        print(HANGMANPICS[0])
    elif lives == 5:
        print(HANGMANPICS[1])
    elif lives == 4:
        print(HANGMANPICS[2])
    elif lives == 3:
        print(HANGMANPICS[3])
    elif lives == 2:
        print(HANGMANPICS[4])
    elif lives == 1:
        print(HANGMANPICS[5])
    


    # game over condition
    if lives == 0:
        print(HANGMANPICS[6])
        print("Game Over")
        break

    print(f"REMAINING LIVES = {lives}\n")
    print("".join(display))









            
    





    



