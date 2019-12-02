with open("input.txt") as f:
    polymer = [line.strip() for line in f][0]

polymer = list(polymer)


def collapse_polymer(polymer):
    indices = 999

    while indices:
        i = 0
        indices = set()
        indices_list = []

        while i < len(polymer) - 1:

            if polymer[i].capitalize() == polymer[i + 1].capitalize():
                if polymer[i].isupper() ^ polymer[i + 1].isupper():
                    indices_list.append((polymer[i], polymer[i + 1]))
                    indices.add(i)
                    indices.add(i + 1)
                    i += 2
                else:
                    i += 1
            else:
                i += 1

        polymer = [element for i, element in enumerate(polymer) if i not in indices]
    return len(polymer)


d = {
    i: collapse_polymer([element for element in polymer if element.casefold() != i])
    for i in set(element.casefold() for element in polymer)
}
