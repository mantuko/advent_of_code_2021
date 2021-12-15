"""
Advent of Code 2021
Day 1 - Sonar Sweep
Part 2
"""
from math import floor


def main():
    input = "input_02.txt"
    count = 0

    with open(input) as f:
        lines = f.read().splitlines()
        # Convert strings to intergers
        lines = [int(x) for x in lines]
        prev_window = None

        for i in range(0, len(lines)):
            window_start = i
            window_stop = i + 3
            window = tuple(lines[window_start:window_stop])

            if len(window) < 3:
                break

            if prev_window and sum(window) > sum(prev_window):
                count += 1

            prev_window = window

    print(f"increased_count: {count}")


if __name__ == "__main__":
    main()
