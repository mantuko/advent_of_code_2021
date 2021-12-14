"""
Advent of Code 2021
Day 1 - Sonar Sweep
Part 1
"""


def main():
    input = "input.txt"
    count = 0

    with open(input) as f:
        lines = f.readlines()
        prev_line = None

        for line in lines:
            if prev_line and int(line) > int(prev_line):
                count += 1

            prev_line = line

    print(count)


if __name__ == "__main__":
    main()
