from typing import NamedTuple
from typing import Callable
from typing import List


class Password(NamedTuple):
    lo: int
    hi: int
    chr: str
    pw: str


def parse_rule(txt: str) -> Password:
    elemets = txt.split()

    lo, hi = elemets[0].split("-")
    chr_ = elemets[1][0]
    pw = elemets[2]

    return Password(int(lo), int(hi), chr_, pw)


def is_valid(pw: Password) -> bool:
    count = pw.pw.count(pw.chr)
    return pw.lo <= count <= pw.hi


def is_valid2(pw: Password) -> bool:
    one = pw.pw[pw.lo - 1] == pw.chr
    two = pw.pw[pw.hi - 1] == pw.chr
    return (one + two) == 1


Validator = Callable[[Password], bool]


def count_valid_pw(pws: List[Password], validate: Validator) -> int:
    return sum(validate(pw) for pw in pws)


if __name__ == "__main__":
    INPUTS = [
        Password(1, 3, "a", "abcde"),
        Password(1, 3, "b", "cdefg"),
        Password(2, 9, "c", "ccccccccc"),
    ]

    assert [is_valid(pw) for pw in INPUTS] == [True, False, True]
    assert [is_valid2(pw) for pw in INPUTS] == [True, False, False]

    with open("input/day02.txt") as f:
        inputs = [parse_rule(l.strip()) for l in f]

    print(count_valid_pw(inputs, is_valid))
    print(count_valid_pw(inputs, is_valid2))
