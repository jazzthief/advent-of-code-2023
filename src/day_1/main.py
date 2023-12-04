import re
from pathlib import Path


def parse_numbers(line: str, map_: dict = {}) -> str:
    """Parse str number names to ints"""

    # init the map only on the first call
    if not map_:
        map_ = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }

    replace_dict = {}

    for word in map_.keys():
        found_idx = [m.start() for m in re.finditer(word, line)]
        replace_dict[map_[word]] = found_idx
    print(replace_dict)
    for digit, idx in replace_dict.items():
        for i in idx:
            line = line[:i] + str(digit) + line[i+1:]

    return line


def part_2_solve_naive():
    result = 0

    with open(Path.cwd() / "input.txt") as f:
        for line in f:
            print(f"original line: {line}")
            parsed_line = parse_numbers(line)
            print(f"parsed line: {parsed_line}")
            found_first, found_last = "", ""

            for char in parsed_line:
                if char.isdigit():
                    if not found_first:
                        found_first = char
                    else:
                        found_last = char

            # if there's only one number in line, then it's the first and the last
            if not found_last:
                found_last = found_first

            print(f"first: {found_first}, last: {found_last}")
            print(f"sum: {int(found_first + found_last)}")
            result += int(found_first + found_last)

    return result


def part_1_solve_naive():
    result = 0

    with open(Path.cwd() / "input.txt") as f:
        for line in f:
            print(line)
            found_first, found_last = "", ""

            for char in line:
                if char.isdigit():
                    if not found_first:
                        found_first = char
                    else:
                        found_last = char

            # if there's only one number in line, then it's the first and the last
            if not found_last:
                found_last = found_first

            print(f"first: {found_first}, last: {found_last}")
            print(f"sum: {int(found_first + found_last)}")
            result += int(found_first + found_last)

    return result


# Unfinished 2 pointers solution
def part_1_solve_pointers():
    result = 0

    with open(Path.cwd() / "input.txt") as f:
        for line in f:
            print(line)
            i, j = 0, len(line) - 1
            found_left, found_right = "", ""

            while i < j and not (found_left and found_right):
                print(f"Current {i} {j}")
                if not found_left:
                    if line[i].isdigit():
                        found_left = line[i]
                        print(f"Found left {found_left}")
                    else:
                        i += 1
                if not found_right:
                    if line[j].isdigit():
                        found_right = line[j]
                        print(f"Found right {found_right}")
                    else:
                        j -= 1
            print(f"left: {found_left}, right: {found_right}")
            print(f"sum: {int(found_left + found_right)}")
            result += int(found_left + found_right)

    return result


if __name__ == "__main__":
    print(part_2_solve_naive())
