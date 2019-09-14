def selection(list1):
    list_len = len(list1)
    for i in range(list_len - 1):
        small = i
        swap = False
        for j in range(i+1, list_len):
            if list1[small] > list1[j]:
                small = j
                swap = True
        if swap:
            list1[i], list1[small] = list1[small], list1[i]

    return list1


print(selection([64, 34, 25, -12, 22, 11, -90]))  # test case
