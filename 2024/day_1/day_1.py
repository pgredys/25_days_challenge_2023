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

def task_1(file_name: str) -> Any:
    imported = import_data(file_name)
    col0, col1 = separate_columns(imported)

    similarity_score = 0
    for number in col0:
        similarity_score += number * col1.count(number)
    return similarity_score


if __name__ == '__main__':
    # task 0:
    print('First task')
    print(f'Test answer: {task_0("test.txt")}')   # expected: 11
    print(f'Final answer: {task_0("input.txt")} ' # expected: 1660292
          f'\n__________________________\n')

    # task 1:
    print('Second task')
    print(f'Test answer: {task_1("test.txt")}')  # expected: 31
    print(f'Final answer: {task_1("input.txt")}')  # expected: 22776016