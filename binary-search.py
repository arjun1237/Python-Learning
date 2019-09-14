list1 = [2, 3, 4, 6, 7]  # test case
search = 7  # test case


def binary(nums, find):
    l = 0
    u = len(nums) - 1

    while l <= u:
        mid = (u+l) // 2
        temp = nums[mid]

        if temp == find:
            return mid

        if temp < find:
            l = mid + 1

        elif temp > find:
            u = mid - 1

    return -1


val = binary(list1, search)

if val == -1:
    print("Not Found")
else:
    print(f"Found at {val}")
