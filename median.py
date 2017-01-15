# This script returns the median number in a list of numbers

def median(old_list):
    new_list = sorted(old_list)
    if len(new_list) % 2 == 0:
        index1 = len(new_list) / 2
        index2 = index1 - 1
        result = (new_list[index1] + new_list[index2]) / 2.0
        return result
    else:
        index = len(new_list) / 2
        result = new_list[index]
        return result

print median([5, 2, 3, 1, 4])
print median([5, 2, 3, 6, 1, 4])
print median([50, 20, 30, 10, 40])
print median([50, 20, 30, 60, 10, 40])
