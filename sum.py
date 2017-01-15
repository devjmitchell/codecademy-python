# FYI sum(grades) is a quicker way, but Codecademy want us to learn how to manually do it
# This script returns the sum of the list of grades

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for i in scores:
        total += i
    return total

print grades_sum(grades)
