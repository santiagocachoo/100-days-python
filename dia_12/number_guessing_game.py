from random import randint

def main():
    print("Welcome to the Number Guessing Game")
    number = randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    print(f"Hint, the number is {number}")
    lives = 0
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5

    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))
        if user_guess > number:
            lives -= 1
            print("Too high")
        elif user_guess < number:
            lives -= 1
            print("Too low")
        elif user_guess == number:
            print(f"You got it! The answer was {number}")
            break

    if lives == 0:
        print("You've run out of guesses, you lose")

main()


