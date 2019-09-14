def bubble(list1):
    list_len = len(list1)
    for i in range(list_len):
        for j in range(list_len - 1 - i):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]

    return list1


print(bubble([5, 7, 3, 2, 8, 0]))  # test case
