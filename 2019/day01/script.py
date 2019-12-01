def get_fuel(module: int) -> int:
    return (module // 3) - 2

def get_recursive_fuel(module: int) -> int:
    l = []
    while get_fuel(module) > 0:
        module = get_fuel(module)
        l.append(module)

    return sum(l)

assert get_recursive_fuel(1969) == 966


with open("./input1.txt") as f:
    modules = [int(l.strip()) for l in f]

res = sum(get_recursive_fuel(module) for module in modules)
print(res)

