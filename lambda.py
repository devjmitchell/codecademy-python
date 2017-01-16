# lambda / anonymous functions
"""
lambda x: x % 3 == 0

is the same as

def by_three(x):
    return x % 3 == 0
"""

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

# this prints [0, 3, 6, 9, 12, 15] to the console
