from __future__ import annotations

import math
import re


def solve_re() -> int:
    """Treat rows as strings and use regex to mask symbols

    Most of this solution is essentialy reverse-engineered solution
    of reddit's user '4HbQ', who made some brilliant assumptions about
    the dataset and came up with an extremely concise algorithm.
    """

    schematic: list[str] = list(open("input.txt"))
    schematic_len = len(schematic[0]) - 1

    # Find all symbols' coordinates
    symbols = {
        (row, col): []
        for row in range(schematic_len)
        for col in range(schematic_len)
        if schematic[row][col] not in '01234566789.'
    }

    for i, row in enumerate(schematic):
        print(f"Proccessing row {i}:\n")
        print(f"Row: '{row}'\n")

        # Match digits and get their spans within the row
        for num in re.finditer(r'\d+', row):
            # Construct set of edge coords for found numbers
            edge = {
                (r, c)
                for r in (i-1, i, i+1)
                for c in range(num.start()-1, num.end()+1)
            }

            # Check for overlap between symbols & edge coordinates;
            # as seen from resulting `symbols` dict, no number is adjacent
            # to more than one symbol
            for o in edge & symbols.keys():
                symbols[o].append(int(num.group()))
                print(f"Found part number: {num.group()}")

        print("------------------\n")

    p1_answer = sum(sum(x) for x in symbols.values())

    # Use `math.prod()` to multiply all pairs of part numbers
    # that are adjacent to same symbol; works because the only symbols
    # having exactly two adjacent part numbers are '*'
    p2_answer = sum(math.prod(x) for x in symbols.values() if len(x) == 2)

    return p1_answer, p2_answer


if __name__ == "__main__":
    a1, a2 = solve_re()
    print(f"Part 1 answer: {a1}", f"Part 2 answer: {a2}")
