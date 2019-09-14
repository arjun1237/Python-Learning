def bubble(list1):
    list_len = len(list1 - 1)
    for i in range(list_len):
        for j in range(list_len - 1 - i):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]

    return list1


print(bubble([64, 34, 25, 12, 22, 11, 90]))  # test case
