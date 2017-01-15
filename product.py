# This script multiplies the input values and returns the total

def product(num):
    total = 1
    for i in num:
        total *= i
    return int(total)

print product([4, 5, 5])
