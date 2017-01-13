# I made my own variation of the guessing game made in Codecademy's course

from random import randint

random_number = randint(1, 100)
#print random_number
guess = False
print("Guess a number between 1 and 100")

while guess != random_number:
    guess = int(raw_input("Your guess:"))
    if guess == random_number:
        print("\nYou win!")
    elif guess > random_number:
        print("\nYou guessed too high!")
    elif guess < random_number:
        print("\nYou guessed too low!")
    else:
        print("\nWell, something didn't work!")
