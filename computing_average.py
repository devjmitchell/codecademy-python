# FYI sum(grades) is a quicker way to get the sum, but Codecademy want us to learn how to manually do it
# This script adds to the previous sum.py script, but now gets the average

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for i in scores:
        total += i
    return total

def grades_average(grades):
    the_sum = grades_sum(grades)
    average = the_sum / float(len(grades))
    return average

print grades_average(grades)
