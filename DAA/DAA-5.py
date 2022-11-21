import random


def quicksort(arr, start, stop):
    if start < stop:
        pivotindex = partitionrand(arr, start, stop)
        quicksort(arr, start, pivotindex)
        quicksort(arr, pivotindex + 1, stop)


def partitionrand(arr, start, stop):
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)


def partition(arr, start, stop):
    pivot = start
    i = start - 1
    j = stop + 1
    while True:
        while True:
            i = i + 1
            if arr[i] >= arr[pivot]:
                break
        while True:
            j = j - 1
            if arr[j] <= arr[pivot]:
                break
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


#array = [10, 7, 8, 9, 1, 5]
n = int(input("Enter length of array: "))
array = []
for i in range(n):
    a = int(input("Enter element: "))
    array.append(a)
quicksort(array, 0, n - 1)
print(array)

