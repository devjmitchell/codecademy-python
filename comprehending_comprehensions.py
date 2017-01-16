# comprehending comprehensions
# creating a list from 1 to 15 of numbers divisible by 3 or 5

threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]

print threes_and_fives
