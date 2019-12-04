def increasing(pw: int) -> bool:
    pw = str(pw)
    for i in range(len(pw) - 1):
        if pw[i] > pw[i + 1]:
            return False

    return True


assert increasing(111111) == True
assert increasing(223450) == False


def adjacent(pw: int) -> bool:
    pw = str(pw)
    for i in range(len(pw) - 1):
        if pw[i] == pw[i + 1]:
            return True

    return False


assert adjacent(111111) == True
assert adjacent(223450) == True
assert adjacent(123789) == False


# Task 1
res = [i for i in range(158126, 624574 + 1) if increasing(i) and adjacent(i)]
print(len(res))


# Task 2

from collections import Counter

def larger_group(pw: int) -> bool:
    c = Counter(str(pw))

    # for _, amount in c.items():
    #     if amount == 2:
    #         return True
    # return False
    return any(amount == 2 for amount in c.values())

assert larger_group(123444) == False
assert larger_group(111122) == True

res2 = [i for i in res if larger_group(i)]

print(len(res2))
