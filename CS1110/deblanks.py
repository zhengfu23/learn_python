def deblanks(s):
    if s == '':
        return s
    elif len(s) == 1:
        if s[0] == ' ':
            return ''
        else:
            return s
    left = deblanks(s[0])
    right = deblanks(s[1:])
    return left+right
