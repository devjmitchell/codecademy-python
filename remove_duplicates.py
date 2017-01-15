# This script removes duplicates from the input values and return the new list

def remove_duplicates(old_list):
    new_list = []
    for i in old_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print remove_duplicates([1,1,2,3,2,4,3,5])
