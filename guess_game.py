# This is a simple guessing game

from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
print "You have 3 tries to guess the right number! (Hint: it's between 1 and 10)"
#print random_number

# Start your game!
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "\nYou win!"
        break
    guesses_left -= 1
    print "\nNope! " + str(guesses_left) + " more tries..."
else:
    print "You lose. The correct number was " + str(random_number)
    print "\n" * 8
