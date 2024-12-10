import os
import re

PATH = os.path.dirname(os.path.abspath(__file__))
    

def read_input() -> list[list[int]]:
    with open(PATH + "/input.txt", "r") as file:
        input =  file.read()

    return input


def part_1() -> int:
    input = read_input()

    coincidences = re.findall(r"mul[(]\d+,\d+[)]", input)

    result = 0
    for el in coincidences:
        el = el[:-1].replace("mul(","")
        numbers = el.split(',')
        result += int(numbers[0]) * int(numbers[1])

    return result


def part_2() -> int:
    input = read_input()

    coincidences = re.findall(r"(mul[(]\d+,\d+[)])|(do[(][])])|(don't[(][])])", input)

    result = 0
    do = True
    for el in coincidences:
        el = next(x for x in el if x != '')
        if el == "do()":
            do = True
        elif el == "don't()":
            do = False
        elif do == True:
            el = el[:-1].replace("mul(","")
            numbers = el.split(',')
            result += int(numbers[0]) * int(numbers[1])

    return result



if __name__ == "__main__":
    print(part_1())
    print(part_2())
