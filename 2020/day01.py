import itertools
import functools
import operator

INPUTS = [1721, 979, 366, 299, 675, 1456]


def prod(x):
    """
    Equivalent of builtin sum
    """
    return functools.reduce(operator.mul, x)


# Very inefficient, but come on, it's day 01
def find_product(inputs, n):
    x = itertools.product(*itertools.repeat(inputs, n))
    result = [prod(tpl) for tpl in x if sum(tpl) == 2020]
    return result[0]


if __name__ == "__main__":
    with open("day01.txt") as f:
        inputs = [int(l) for l in f]

    assert find_product(INPUTS, 2) == 514579
    assert find_product(INPUTS, 3) == 241861950

    print(find_product(inputs, 2))
    print(find_product(inputs, 3))
