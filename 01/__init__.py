from itertools import combinations
from typing import List, Optional
import sys


def get_entry_count() -> int:
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg.isdigit():
            return int(arg)

    return 2


def product(numbers: List[int]) -> int:
    result = 1

    for num in numbers:
        result = result * num

    return result


def find_sum(entries: List[int], count: int) -> Optional[int]:
    for combination in combinations(entries, count):
        if sum(combination) == 2020:
            return combination


def main():
    count = get_entry_count()

    with open("input.txt", "r") as file:
        entries = [int(e.strip("\n")) for e in list(file) if e != "\n"]

    results = find_sum(entries, count)
    if results:
        print(f"result: {product(results)}")


if __name__ == '__main__':
    main()

