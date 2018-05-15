#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def merge_sort(array):
    """ Entry point of merge sort function, which do the "divide" part of divide and conquerer. """

    # print("merge_sort array = {}".format(array))

    length = len(array)
    if length <= 1:
        return array

    array1 = merge_sort(array[:length // 2])
    array2 = merge_sort(array[length // 2:])
    return merge(array1, array2)


def merge(array1, array2):
    """ Inner function of merge sort. Do the "conquer" part of divide and conquer. """

    # print("merge array1 {}, array2 {}".format(array1, array2))

    length1 = len(array1)
    length2 = len(array2)
    length = length1 + length2
    new_array = [0 for i in range(length)]

    counter1 = 0
    counter2 = 0
    for i, v in enumerate(new_array):
        if (counter2 < length2) and (counter1 < length1) and (array1[counter1] <= array2[counter2]):
            new_array[i] = array1[counter1]
            counter1 = counter1 + 1
        elif counter2 < length2:
            new_array[i] = array2[counter2]
            counter2 = counter2 + 1
        elif counter1 < length1:
            new_array[i] = array1[counter1]
            counter1 = counter1 + 1

    return new_array


if __name__ == "__main__":
    assert(merge_sort([3, 1, 9, 7, 5]) == [1, 3, 5, 7, 9])
    assert(merge_sort([3, 1, 9, 7]) == [1, 3, 7, 9])
    assert(merge_sort([3, 1, 9]) == [1, 3, 9])
    assert(merge_sort([3, 9]) == [3, 9])
    assert(merge_sort([9]) == [9])
    assert(merge_sort([]) == [])

    assert(merge_sort([8, 3, 1, 9, 7, 5]) == [1, 3, 5, 7, 8, 9])
    assert(merge_sort([8, 3, 4, 1, 9, 7, 5]) == [1, 3, 4, 5, 7, 8, 9])
