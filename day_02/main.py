import os

import pandas as pd

PATH = os.path.dirname(os.path.abspath(__file__))


def read_input() -> list[list[int]]:
    input = []
    with open(PATH + "/input.txt", "r") as file:
        for line in file.readlines():
            line = line.replace("\n", "").split(" ")
            input.append(list((map(int, line))))

    return input


def is_asceding(data: list[int]) -> bool:
    return data == sorted(data)


def is_descending(data: list[int]) -> bool:
    return data == sorted(data, reverse=True)

def is_distance_valid(min: int , max:int, data: list[int]) -> int:
    for i in range(len(data) - 1):
        distance = abs(data[i] - data[i + 1])
        if distance <= min or distance > max:
            return False
    return True


def part_1() -> int:
    input = read_input()
    valid = 0

    for line in input:
        if (is_asceding(line) or is_descending(line)) and is_distance_valid(0, 3, line):
            valid += 1

    return valid



if __name__ == "__main__":
    print(part_1())
