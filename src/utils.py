from pathlib import Path

default_path = Path.cwd() / "input.txt"


def read_lines(path: Path = default_path):
    """Read file from `cwd` line-by-line yielding lines"""

    with open(path) as f:
        yield from f
