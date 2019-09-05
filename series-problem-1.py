# Write Python code to find if ALL the numbers in a given list of 
# integers are PART of the series defined by the following. 
# f(0) = 0, f(1) = 1, f(n) = 2*f(n-1) - 2*f(n-2) for all n > 1


m = {0: 0, 1: 1}


def is_part_of_series(lst):
    for i in lst:
        if i == 0 or i == 1:
            continue
        if not check_num(i):
            return False

    return True


def check_num(num):
    x_val = 2
    while True:
        val = 2 * (m[x_val - 1] - m[x_val - 2])
        if x_val not in m:
            m[x_val] = val
        x_val += 1

        if val == num:
            return True
        if abs(num) < abs(val):
            return False


print(is_part_of_series([0, 32, -64, -128, 512]))    #Test Case


# to check the series for input 0 to 100
def series():
    print("0: 0")
    print("1: 1")
    for i in range(2, 100):
        m[i] = 2 * (m[i-1] - m[i-2])
        print(f"{i}: {m[i]}")
