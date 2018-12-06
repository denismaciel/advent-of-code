"""
No matter how you slice it
"""
import re
from collections import Counter

rgx = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"

with open("input.txt") as f:
    tips = [line.strip() for line in f]

claims = [re.match(rgx, tip).groups() for tip in tips]

# print(claims)

# ('1319', '627', '639', '23', '11')


# (627, 639) (627, 639) ...     (650, 639)

# ... (628, 639)


# left = 627
# top = 639
# width = 23
# height = 11

c = Counter()


def inches_covered(left, top, width, height):
    left = int(left)
    top = int(top)
    width = int(width)
    height = int(height)

    for x in range(left, left + width):
        for y in range(top, top + height):
            yield (x, y)

for claim in claims:
    _id, left, top, width, height = claim
    inches = inches_covered(left, top, width, height)
    c.update(inches)

count_frequencies = Counter(c.values())
print(count_frequencies)

repeated_inches = sum([count_frequencies[frequency] for frequency in count_frequencies if frequency > 1])
print(repeated_inches)


# Second part: find single claim that has not overlap
for claim in claims:
    overlaps = 0
    _id, left, top, width, height = claim
    inches = inches_covered(left, top, width, height)
    for inch in inches:
        if c[inch] > 1:
            overlaps += 1
        if overlaps > 0:
            break

    if overlaps == 0:
        print(_id)

