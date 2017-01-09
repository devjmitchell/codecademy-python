# Slow way
def reverse_slow(text):
    new_string = []
    index = len(text)
    while index:
        index -= 1
        new_string.append(text[index])
    return ''.join(new_string)


print reverse_slow("!dlrow olleH")

# Better way
def reverse(text):
    return text[::-1]

print reverse('!dlrow olleH')
