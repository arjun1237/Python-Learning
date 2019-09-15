# FYI - the selection of pivot is first element, so worst case scenario is O(n^2)

list1 = [108, 64, 34, 25, 12, 22, 11, -90, 0]  # test case

def partition(low, high):
    pivot = list1[low]

    i = low + 1
    j = high - 1

    while i < j:
        while list1[i] <= pivot and i < len(list1) - 1:
            i += 1

        while list1[j] > pivot and j > 0:
            j -= 1

        if i < j:
            list1[i], list1[j] = list1[j], list1[i]

    return j

def quick(l, h):
    if l < h:
        j = partition(l, h)
        list1[l], list1[j] = list1[j], list1[l]
        quick(l, j)
        quick(j+1, h)


quick(0, len(list1))

print(list1)
