import random
from sys import exit

# Computer guesses a random number between 1 and 20
print("Welcome to the guessing game!")
print("You have three guesses before losing your turn")
count: int = 3
another_game: chr = 'n'

# User has 3 guesses before losing the game

while count != 0:
    correct_answer: int = random.randint(1, 10)
# User guess the numbers
    user_guess = input("Guess my number: ")
    user_guess = int(user_guess)
    count -= 1

    # Computer tells the user whether guess was too high or too low
    if user_guess == correct_answer:
        print("Good guess! Wow you are mind reader")
        another_game = input("Do you want to continue? y/n ")
        if another_game == 'y':
            user_guess = 11
            count = 3
        elif another_game == 'n':
            exit()

    elif user_guess > correct_answer:
        print("Sorry, your guess is too high!")
        print("The correct answer is " + str(correct_answer))
        print("No luck this time, you have " + str(count) + " more tries")
    elif user_guess < correct_answer:
        print("Sorry, your guess is too low!")
        print("The correct answer is " + str(correct_answer))
        print("No luck this time, you have " + str(count) + " more tries")

    if count == 0:
        print("Game over, you used all your three tries, that was fun!")
        another_game = input("Do you want to continue? y/n ")
        if another_game == 'y':
            count = 3
        elif another_game == 'n':
            continue






