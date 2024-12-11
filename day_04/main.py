import os
import re

PATH = os.path.dirname(os.path.abspath(__file__))


def read_input() -> list[list[int]]:
    input = []
    with open(PATH + "/input.txt", "r") as file:
        for line in file.readlines():
            input.append(line.replace("\n", ""))

    return input

def XMAS_count(lines: list[str]) -> int:
    count = 0
    for line in lines:
        matches_xmas = len(re.findall(r"XMAS", line))
        matches_samx = len(re.findall(r"SAMX", line))
        count += matches_xmas + matches_samx
        print(f"Line: {line} | XMAS: {matches_xmas}, SAMX: {matches_samx}")
    return count

def vertical_transform(matrix: list[list[str]]) -> list[str]:
    vertical_lines = ["".join(row[i] for row in matrix) for i in range(len(matrix[0]))]
    print("Vertical Lines:")
    for line in vertical_lines:
        print(line)
    return vertical_lines

def get_diagonals(matrix: list[list[str]]) -> tuple[list[str], list[str]]:
    N = len(matrix)
    diagonals_left = []
    diagonals_right = []

    # Diagonales inferiores izquierdas
    for d in range(N):
        diagonal = []
        for i in range(d + 1):
            row = N - 1 - i
            col = i
            if 0 <= row < N and 0 <= col < N:
                diagonal.append(matrix[row][col])
        diagonals_left.append("".join(diagonal))

    for d in range(1, N):
        diagonal = []
        for i in range(N - d):
            row = i
            col = d + i
            if 0 <= row < N and 0 <= col < N:
                diagonal.append(matrix[row][col])
        diagonals_left.append("".join(diagonal))

    # Diagonales superiores derechas
    for d in range(N):
        diagonal = []
        for i in range(d + 1):
            row = N - 1 - i
            col = N - 1 - (d - i)
            if 0 <= row < N and 0 <= col < N:
                diagonal.append(matrix[row][col])
        diagonals_right.append("".join(diagonal))

    for d in range(1, N):
        diagonal = []
        for i in range(N - d):
            row = i
            col = N - 1 - (d - i)
            if 0 <= row < N and 0 <= col < N:
                diagonal.append(matrix[row][col])
        diagonals_right.append("".join(diagonal))

    print("Diagonal Left:")
    for line in diagonals_left:
        print(line)

    print("Diagonal Right:")
    for line in diagonals_right:
        print(line)

    return diagonals_left, diagonals_right

def part_1(matrix: list[list[str]]) -> int:
    # Generar transformaciones
    horizontal_lines = ["".join(row) for row in matrix]
    vertical_lines = vertical_transform(matrix)
    diagonal_a, diagonal_b = get_diagonals(matrix)

    # Conteo por orientación
    print("Horizontal Lines:")
    for line in horizontal_lines:
        print(line)

    horizontal_count = XMAS_count(horizontal_lines)
    vertical_count = XMAS_count(vertical_lines)
    diagonal_a_count = XMAS_count(diagonal_a)
    diagonal_b_count = XMAS_count(diagonal_b)

    # Debugging de resultados parciales
    print(f"Horizontal: {horizontal_count}")
    print(f"Vertical: {vertical_count}")
    print(f"Diagonal A (izquierda): {diagonal_a_count}")
    print(f"Diagonal B (derecha): {diagonal_b_count}")

    # Resultado total
    return horizontal_count + vertical_count + diagonal_a_count + diagonal_b_count

# Ejemplo de entrada
input_matrix = [
    list("MMMSXXMASM"),
    list("MSAMXMSMSA"),
    list("AMXSXMAAMM"),
    list("MSAMASMSMX"),
    list("XMASAMXAMM"),
    list("XXAMMXXAMA"),
    list("SMSMSASXSS"),
    list("SAXAMASAAA"),
    list("MAMMMXMMMM"),
    list("MXMXAXMASX"),
]

# Resultado
print("Total de XMAS encontrados:", part_1(read_input()))
