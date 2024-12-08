import os

import pandas as pd
PATH = os.path.dirname(os.path.abspath(__file__))


def read_input() -> tuple[list, list]:
    list_a, list_b = [], []
    with open (PATH + "/input.txt", "r") as file:
        for line in file.readlines():
            
            list_a.append(int(line.replace('\n','').split('   ')[0]))
            list_b.append(int(line.replace('\n','').split('   ')[1]))

    return (list_a, list_b)


def part_1() -> int:
    list_a, list_b = read_input()
    
    list_a.sort()
    list_b.sort()

    df = pd.DataFrame({'a': list_a, 'b': list_b})
    df['diff'] = abs(df['a'] - df['b'])
    result = sum(df["diff"])
    return result

def part_2() -> int:
    list_a, list_b = read_input()

    similarity = sum([list_b.count(i) * i for i in list_a])
    return similarity


if __name__ == "__main__":
    print(part_1())
    print(part_2())
