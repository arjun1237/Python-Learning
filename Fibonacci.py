m = {}

# recusrsive and memoization method
def fib(n):
    if n in m:
        return m[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        m[n] = fib(n-1) + fib(n-2)
    return m[n]

print(fib(8))

# bottoms up approach
def fib2(n):
    for i in range(1, n+1):
        if i <= 2:
            f = 1
        else:
            f = m[i-1] + m[i-2]
        m[i] = f
    return m[n]

print(fib2(8))
