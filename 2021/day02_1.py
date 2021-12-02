from typing import NamedTuple
RAW ="""forward 5
down 5
forward 8
up 3
down 8
forward 2"""


class Instruction(NamedTuple):
    direction: str
    size: int

    @classmethod
    def from_string(cls, string):
        direction, size = string.split()
        return cls(direction, int(size))


class Ride:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, instruction: Instruction) -> None:
        if instruction.direction == "down":
            self.y += instruction.size
        elif instruction.direction == "up":
            self.y -= instruction.size
        elif instruction.direction == "forward":
            self.x += instruction.size
        else:
            raise RuntimeError

instructions  = [Instruction.from_string(line) for line in RAW.split("\n")]
ride = Ride(0, 0)
for i in instructions:
    ride.move(i)

assert ride.x * ride.y == 150


if __name__ == "__main__":
    with open("input/day02.txt") as f:
        instructions  = [Instruction.from_string(line) for line in f]

    ride = Ride(0, 0)
    for i in instructions:
        ride.move(i)

    print(ride.x * ride.y)
