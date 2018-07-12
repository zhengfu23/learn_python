def print_backward(s):
    index = len(s) - 1
    while index >= 0:
        print(s[index])
        index -= 1


def duckling_names():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            letter = letter + 'u'
        print(letter + suffix)
