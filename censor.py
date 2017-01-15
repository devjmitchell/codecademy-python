# This script censors the word you specify from your string and returns the string with asterisks (*) in its place

def censor(text,word):
    list1 = text.split()
    list2 = []
    for x in list1:
        if x == word:
            list2.append(len(x)*"*")
        else:
            list2.append(x)
    new_phrase = " ".join(list2)
    print new_phrase # to see what is being returned
    return new_phrase

censor("This hack is a hack test of hacks", "hack")

"""
# Someone gave me tip that the following is a quicker way to do this
def censor(text, word):
    return text.replace(word, "*" * len(word))
"""
