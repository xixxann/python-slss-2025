# AOC Day 1
# Author: Angel Li
# 1 December


def part_one():
    cur_location = 50
    zero_count = 0

    # read every line in the instructions
    with open("data/aoc-2025-day1.txt") as f:
        for line in f:
            direction = line[0]
            distance = int(line[1:])

            if direction == "R":
                cur_location += distance
            else:
                cur_location -= distance

            if cur_location % 100 == 0:
                zero_count += 1

    # if we've landed on 0, keep track of this
    print(f"The number of zeros is {zero_count}.")


# Count those with 100s
def part_two():
    cur_location = 50
    zero_count = 0

    with open("data/aoc-2025-test.txt") as f:
        for line in f:
            direction = line[0]
            distance = int(line[1:])

            if direction == "R":
                cur_location += distance
            else:
                cur_location -= distance

            if cur_location < 0:
                actual_location = cur_location + 100
            elif cur_location > 99:
                actual_location = cur_location - 100

            if actual_location % 100 == 0:
                zero_count += 1

    print(f"The number of zeros is {zero_count}.")


if __name__ == "__main__":
    part_two()
