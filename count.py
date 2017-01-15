# This script counts how often the "item" appears in the "sequence"

def count(sequence,item):
    found = 0
    for i in sequence:
        if i == item:
            found += 1
    return found

print count([1,2,2,1],1)
print count([4, 'foo', 5, 'foo'],5)
print count([4, 'foo', 5, 'foo'],'foo')
