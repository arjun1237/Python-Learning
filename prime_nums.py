# prints prime numbers between 1 and 150(included) in one line

print([x for x in range(1, 151) if not any([x % y == 0 for y in range(2, int(x/2)+1)]) and not x == 1])
