
s = [
    ['{', '}'],
    ['[', ']'],
    ['(', ')']
]


def matchParen(x):
    b = []
    for i in x:
        if open_brack(i):
            b.append(i)
        else:
            if len(s) == 0:
                return False
            elif not match(b.pop(), i):
                return False
    return len(b) == 0


def open_brack(brack):
    for i in s:
        if i[0] == brack:
            return True
    return False


def match(brack1, brack2):
    for i in s:
        if i[1] == brack2 and i[0] == brack1:
            return True
    return False

print(matchParen("[(])")) # test case
