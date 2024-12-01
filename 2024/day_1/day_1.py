from typing import Any


def import_data(file_name: str) -> list[list[int]]:
    with open(file_name) as f:
        lines = [[int(n) for n in line.strip().split('   ')] for line in f]
        return lines

def separate_columns(lines: list) -> tuple[list[Any], list[Any]]:
    col_0, col_1 = [], []
    for row in lines:
        col_0.append(row[0])
        col_1.append(row[1])
    return col_0, col_1

def task_0(file_name: str) -> int:
    imported = import_data(file_name)
    col0, col1 = separate_columns(imported)
    col0, col1 = sorted(col0), sorted(col1)

    distances = [abs(col0[n] - col1[n]) for n in range(len(col0))]
    total_distance = sum(distances)
    return total_distance

if __name__ == '__main__':
    # task 0:
    print('First task')
    print(f'Test answer: {task_0("test.txt")}')
    print(f'Final answer: {task_0("input.txt")} \n__________________________')
