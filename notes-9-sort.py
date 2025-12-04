# Intro to Sort
# Author: Angel Li
# 4 December

import csv

# Sorting Algorithms
# The code below uses linear search to find songs from a particular artist
# We're going to sort the results using Selection Sort
#     * implement basic version
#     * implement sort with songs based on YouTube views in descending order


# # what I did (Ver 1)
# def selection_sort(l: list[int], ascending=True) -> list[int]:
#     """Sorts a given list using selection sort

#     Params:
#         l - list of nums to be sorted
#         ascending - True if order is ascending

#     Returns:
#         a sorted list"""

#     num_items = len(l)
#     if ascending:
#         # start at the beginnng of list
#         for i in range(num_items):  # i represents the current item
#             # set the current num to the lowest num
#             lowest_num = l[i]
#             # set the current index to the lowest index
#             lowest_index = i
#             # check the rest of the list
#             for j in range(i + 1, num_items):  # j represents the rest of the list
#                 # if this item is lower than the lowest
#                 if l[j] < lowest_num:
#                     # set this num to the lowest num
#                     lowest_num = l[j]
#                     # set this index to the lowest index
#                     lowest_index = j
#                 # move to the next number
#             # swap the current index with the lowest
#             l[i], l[lowest_index] = l[lowest_index], l[i]
#     else:  # descending
#         for i in range(num_items):
#             highest_num = l[i]
#             highest_index = i
#             for j in range(i + 1, num_items):
#                 if l[j] > highest_num:
#                     highest_num = l[j]
#                     highest_index = j
#             l[i], l[highest_index] = l[highest_index], l[i]

#     return l


# class example (Ver 2)
def selection_sort(l: list[int], ascending=True) -> list[int]:
    """Sorts a given list using selection sort

    Params:
        l - list of nums to be sorted
        ascending - True if order is ascending

    Returns:
        a sorted list"""

    num_items = len(l)

    # start at the beginnng of list
    for i in range(num_items):
        candidate_num = l[i]
        candidate_index = i
        # check the rest of the list
        for j in range(i + 1, num_items):
            if ascending:
                if l[j] < candidate_num:
                    candidate_num = l[j]
                    candidate_index = j
            else:
                if l[j] > candidate_num:
                    candidate_num = l[j]
                    candidate_index = j
        # swap the current index with the lowest
        l[i], l[candidate_index] = l[candidate_index], l[i]
    return l


if __name__ == "__main__":
    sorted_list = selection_sort([1, 43, 55, -11, 100, 34], False)
    print(sorted_list)
    sorted_list = selection_sort([1, 43, 55, -11, 100, 34], True)
    print(sorted_list)
