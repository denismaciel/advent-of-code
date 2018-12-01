# with open('input.txt', 'r') as f:
#     l = f.readlines()

# freq = 0

# for i in l:
#     freq += int(i)

# print(freq)

with open('input.txt', 'r') as f:
    l = f.readlines()

freq = 0
seen = set()
i = 0

while True:

    if freq in seen:
        print(freq)
        break

    seen.add(freq)

    freq += int(l[i])

    if i == len(l) - 1:
        i = 0
    else:
        i += 1

