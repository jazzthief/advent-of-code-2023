import re
from pathlib import Path

from ..utils import read_lines


def solve_sets() -> int:
    path = Path(__file__).resolve().parent / "input.txt"

    result = 0
    for line in read_lines(path):
        nums = re.findall(r'\d+', line[9:])
        matches_n = len(nums) - len(set(nums))

        if not matches_n:
            continue

        win = 2 ** (matches_n-1)
        result += win

    return result


if __name__ == "__main__":
    print(solve_sets())
