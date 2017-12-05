#!/usr/bin/env python3


def merge_sorted_list(alist, blist):
    """ Use merge sort to sort sorted alist and blist, and return merged sorted list of alist. """

    if not isinstance(alist, list):
        raise TypeError("{} should be of type list".format(alist))

    if not isinstance(blist, list):
        raise TypeError("{} should be of type list".format(blist))

    sorted_list = []

    alist_length = len(alist)
    blist_length = len(blist)

    i = 0
    j = 0
    while (i < alist_length) or (j < blist_length):

        if i == alist_length:
            sorted_list.append(blist[j])
            j = j + 1
        elif j == blist_length:
            sorted_list.append(alist[i])
            i = i + 1
        elif alist[i] <= blist[j]:
            sorted_list.append(alist[i])
            i = i + 1
        else:
            sorted_list.append(blist[j])
            j = j + 1

    return sorted_list


def merge_sort_list(alist):
    """ Use merge sort to sort alist and return sorted list of alist. """

    if not isinstance(alist, list):
        raise TypeError("{} should be of type list".format(alist))

    length = len(alist)

    if length == 2:
        if alist[0] > alist[1]:
            alist[0], alist[1] = alist[1], alist[0]

        return alist

    elif length == 1:
        return alist

    half_length = length // 2
    first_half_list = alist[:half_length]
    second_half_list = alist[half_length:]

    sorted_list = merge_sorted_list(merge_sort_list(first_half_list), merge_sort_list(second_half_list))
    return sorted_list


def test_merge_sort():
    """ Test driver using merge sort to sort unsorted list into sorted one. """

    source_list = [3, 2, 1, 5, 6, 10, 9, 8, 4, 7, 0]
    print("source list before sort = {}".format(source_list))
    sorted_list = merge_sort_list(source_list)
    assert sorted_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("sorted_list = {}".format(sorted_list))


if __name__ == "__main__":
    test_merge_sort()
