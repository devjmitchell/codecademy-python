# This script takes a list of numbers and "purifies" it by removing odd numbers and returning a new list of even numbers only

def purify(num):
    new_list = []
    for i in num:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

print purify([1,2,3,4,5,6])
