# Intro to Sort
# Author: Angel Li
# 4 December

import helper_spotify

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


# # class example (Ver 2)
# def selection_sort(l: list[int], ascending=True) -> list[int]:
#     """Sorts a given list using selection sort

#     Params:
#         l - list of nums to be sorted
#         ascending - True if order is ascending

#     Returns:
#         a sorted list"""

#     num_items = len(l)

#     # start at the beginnng of list
#     for i in range(num_items):
#         candidate_num = l[i]
#         candidate_index = i
#         # check the rest of the list
#         for j in range(i + 1, num_items):
#             if ascending:
#                 if l[j] < candidate_num:
#                     candidate_num = l[j]
#                     candidate_index = j
#             else:
#                 if l[j] > candidate_num:
#                     candidate_num = l[j]
#                     candidate_index = j
#         # swap the current index with the lowest
#         l[i], l[candidate_index] = l[candidate_index], l[i]
#     return l


def sort_songs(songs: list[list[str]], col: int, ascending=True) -> list[list[str]]:
    """Sort a list of spotify songs in place

    Params:
        songs - list of songs
        col - column to sort
        ascending - will sort ascending by default

    Returns: sorted list"""
    # Use Selection Sort to sort songs
    num_songs = len(songs)
    # Starting at the beginning of the list
    for i in range(num_songs):
        # Set this value to the candidate's value
        candidate_val = helper_spotify.string_to_num(songs[i][col])
        candidate_idx = i

        for j in range(i + 1, num_songs):
            this_songs_val = helper_spotify.string_to_num(songs[j][col])
            if ascending:
                if this_songs_val < candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j
            else:
                if this_songs_val > candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j

        # Swap!
        songs[i], songs[candidate_idx] = songs[candidate_idx], songs[i]

    return songs


if __name__ == "__main__":
    # Get all songs from Taylor Swift
    taylors_songs = helper_spotify.songs_by_artist(
        "data/spotify2024.csv", "Taylor Swift"
    )
    taylors_sorted_songs = sort_songs(taylors_songs, 11, ascending=False)

    # Header on the results
    print("Taylor Swift's Songs")
    print("______________________")
    print("Name\tYT Views")
    # For every song, print out the Track Name, YT Views
    for song in taylors_sorted_songs:
        print(song[0], "\t", song[11])
