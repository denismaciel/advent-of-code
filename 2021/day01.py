
from typing import Iterable

def load_input():
    with open("input/day01.txt") as f:
        return [int(line) for line in f]

def count_increases(measurements: list[int]) -> int:
    acc = 0
    for x, y in zip(measurements, measurements[1:]):
        if x < y:
            acc += 1
    return acc


def create_measurement_windows(measurements: list[int]) -> Iterable[tuple[int, ...]]:
    size = len(measurements)
    indices = [(start, start + 3) for start in range(size) if start + 2 < size]

    for start, end in indices:
        yield tuple(measurements[start:end])


def part_one(input: list[int]) -> int:
    return count_increases(input)


def part_two(input: list[int]) -> int:
    sum_win = [sum(w) for w in create_measurement_windows(input)]
    return count_increases(sum_win)

def main():
    input = load_input()
    print(part_one(input))
    print(part_two(input))


if __name__ == "__main__":
    main()
