import random

#   Game set up
print ("welcome to guess game!")
num_of_guess = 3
user_won = False

user_answer = random.randint(1, 10)
while num_of_guess > 0:
    user_guess = input("Guess the number ")
    user_guess = int(user_guess)

    if user_guess == user_answer:
        print("You guessed it correctly!")
        user_won = True
        break
    elif user_guess > user_answer:
        print("sorry, too high !")
    elif user_guess < user_answer:
        print("sorry, too low !")

    num_of_guess -= 1

if user_won == True:
    print("you win !")
else:
    print("you lost !")
