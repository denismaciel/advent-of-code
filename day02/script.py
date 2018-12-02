"""
Advent of code - Day 2
"""
from collections import Counter
from typing import Dict, List, Tuple

with open("input.txt", "r") as f:
    boxes = [line.strip() for line in f.readlines()]


def count_letters(word: str) -> Counter:
    """
    Count the counts of letters.
    """
    letter_count = Counter(word)

    return Counter(letter_count.values())


c = [count_letters(box) for box in boxes]


has_two = [box[2] != 0 for box in c]
has_three = [box[3] != 0 for box in c]

print(sum(has_two) * sum(has_three))


# Assert that lenghts of box ids are equal

for box in boxes:
    assert len(box) == len(boxes[0])


def compare_boxes(boxes: List[str]) -> Dict:
    """
    Returns a dict where keys are the numbers of equal letters between two boxes.
    """

    box_comparison = dict()

    for box1 in boxes:
        for box2 in boxes:
            if box1 != box2:
                n_equal_letters = sum([c1 == c2 for c1, c2 in zip(box1, box2)])
                box_comparison[n_equal_letters] = (box1, box2)

    return box_comparison


box_comparison = compare_boxes(boxes)

print(box_comparison)


def most_similar_boxes(box_comparison: Dict) -> Tuple[str, str]:

    max_equal_letters = max(box_comparison.keys())

    return box_comparison[max_equal_letters]


box1, box2 = most_similar_boxes(box_comparison)


def common_letters(string1: str, string2: str) -> str:
    """
    Given two strings, it returns a string with the common letters between them.
    """
    common_letters = "".join([letter for letter in string1 if letter in string2])
    return common_letters

common_letters = common_letters(box1, box2)

print(common_letters)
