# Intro to Search
# Author: Angel Li
# 25 November 2025

import csv

# Introduction to Search Algorithms
# Search for all songs by "Kendrick"
# Display all YouTube and TikTok views
# Sort by either YouTube or TikTok views


def main():
    artist = "Kendrick Lamar"  # artist to find
    track_col = 0
    artist_col = 2
    yt_views_col = 11
    tiktok_views_col = 15

    # open the file
    with open("data/spotify2024.csv") as f:
        # get rid of the header
        _ = f.readline()

        # create a csv reader
        r = csv.reader(f)

        kendrick_songs = []

        # read each line of data
        for info in r:
            if artist == info[artist_col]:
                kendrick_songs.append(info)

        # print how many songs are in the list
        print(f"Number of Kendrick Songs: {len(kendrick_songs)}")

        # print our findings in a pretty way
        print("Track Name\t\tYouTube Views\t\tTikTok Views")  # header
        for song in kendrick_songs:
            current_track = song[track_col]
            current_ytviews = song[yt_views_col]
            current_tiktokviews = song[tiktok_views_col]

            print(f"{current_track}\t\t{current_ytviews}\t\t{current_tiktokviews}")
        # I Like Frogs      100,250,132         1,000,001
        # Eating Food       400,300             12,000,000

    # Find another artist's songs and add them to a list
    artist = "NewJeans"
    track_col = 0
    artist_col = 2

    with open("data/spotify2024.csv") as f:
        # get rid of the header
        _ = f.readline()

        # create a csv reader
        r = csv.reader(f)

        NJ_songs = []

        # read each line of data
        for info in r:
            if artist == info[artist_col]:
                NJ_songs.append(info)

        print(f"Number of Songs: {len(NJ_songs)}")

        # print our findings in a pretty way
        print("Track Names for NewJeans:")  # header
        for song in NJ_songs:
            current_track = song[track_col]
            print(f"{current_track}")

    # Display all the songs that are not explicit
    with open("data/spotify2024.csv") as f:
        # get rid of the header
        _ = f.readline()

        # create a csv reader
        r = csv.reader(f)

        Not_Ex_songs = []

        ex_col = -1

        # read each line of data
        for info in r:
            if info[ex_col] == "0":
                Not_Ex_songs.append(info)
            # elif info[-1] == "1":
            #     pass

        print(f"Number of Songs: {len(Not_Ex_songs)}")

        # print our findings in a pretty way
        print("Track Names for all the Explicit Songs:")
        for song in Not_Ex_songs:
            current_track = song[0]
            print(f"{current_track}")


if __name__ == "__main__":
    main()
