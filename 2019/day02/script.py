def run_program(program):
    # print(program[0:4])
    for i in range(0, len(program), 4):
        if program[i] == 1:
            program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
        elif program[i] == 2:
            program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]
        elif program[i] == 99:
            return program
        else:
            raise Exception(f"Position {i} contains {program[i]}")

    raise Exception("Program finished without hitting a 99")


assert run_program([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert run_program([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
assert run_program([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
assert run_program([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def pass_noun_and_verb(program, noun, verb):
    _program = program.copy()
    _program[1] = noun
    _program[2] = verb
    return run_program(_program)[0]

with open('input.txt') as f:
    program_imut = [l for l in f][0]
    program_imut = program_imut.strip().split(',')
    program_imut = [int(i) for i in program_imut]

# Task 1
# program[1] = 12
# program[2] = 2

# print(run_program(program)[0])

# Task 2

nouns = range(100)
verbs = range(100)

from sys import exit
for noun  in nouns:
    for verb in verbs: 
        output = pass_noun_and_verb(program_imut.copy(), noun, verb)
        if output == 19690720:
            print(noun, verb, noun * 100 + verb)
            exit(0)

