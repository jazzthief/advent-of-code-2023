from __future__ import annotations

import re
from pathlib import Path
from typing import Generator

GAME_LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def read_games(path: Path) -> Generator[list[dict[str, int]], None, None]:
    """Read input file line-by-line and yield parsed games info

    Game info line format:
    "Game {game_id}: N {Color}, ...; ..."
    """

    # Could try parsing entire lines with regex
    # This matches num-color pairs
    pattern = re.compile(r'(?:(\d+) (\w+))')

    with open(path) as f:
        for line in f:
            balls = line.split(":")[-1]


            balls_groups = [g.strip() for g in balls.split(";")]
            # create a list of tuples of (N, color)
            parsed_groups = list(map(pattern.findall, balls_groups))

            # create a list of dicts {color: N} for every game round
            rounds: list[dict[str, int]] = []
            for group in parsed_groups:
                round_ = {t[1]: int(t[0]) for t in group}
                rounds.append(round_)

            yield rounds


def part_1_solve_naive() -> int:
    """Solve iteratively by checking every round of every game

    Uses `for ... else` constructs to stop checking a game early if a limit
    violation was found.
    """

    input_path = Path.cwd() / "input.txt"
    games_generator = read_games(input_path)

    result = 0
    game_n = 1
    for game in games_generator:
        print("--------------------------")
        print(f"Game {game_n}")
        print(f"{game}\n")

        for round_ in game:

            for color, limit in GAME_LIMITS.items():
                picked_n = round_.get(color, 0)
                if picked_n > limit:
                    # Break out of both loops
                    print(f"Limit violated at round: {round_}\n")
                    break
            else:
                continue
            break
        else:
            # Executed if inner loop did NOT break
            # i.e. no violations in current game
            print(f"Game {game_n} is possible\n")
            result += game_n
            game_n += 1
            continue

        # Executed if inner loop breaks
        print(f"Game {game_n} is NOT possible\n")
        game_n += 1
        continue

    return result


if __name__ == "__main__":
    print(part_1_solve_naive())
