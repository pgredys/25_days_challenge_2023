
def import_data(file_name: str) -> list[list[int]]:
    with open(file_name) as f:
        lines = [[int(n) for n in line.strip().split(' ')] for line in f]
        return lines

def is_safe(line: list[int]) -> bool:
    if line == sorted(line) or line == sorted(line, reverse=True):
        for i in range(len(line) - 1):
            if not(1 <= abs(line[i] - line[i+1]) <= 3):
                return False

        return True
    else:
        return False

def task_0(file_name: str) -> int:
    data = import_data(file_name)
    safe_reports = 0

    for record in data:
        if is_safe(record):
            safe_reports += 1

    return safe_reports


def is_safe_tolerated(record: list[int]) -> bool:
    for i in range(len(record)):
        fix_record = [element for j, element in enumerate(record) if j != i]

        if is_safe(fix_record):
            return True

    return False


def task_1(file_name: str) -> int:
    data = import_data(file_name)
    safe_reports = 0

    for record in data:
        if is_safe(record):
            safe_reports += 1
        elif is_safe_tolerated(record):
            safe_reports += 1

    return safe_reports

if __name__ == '__main__':
    # task 0:
    print('First task')
    print(f'Test answer: {task_0("test.txt")}')    # expected: 2
    print(f'Final answer: {task_0("input.txt")} '  # expected: 314
          f'\n-------------------\n')

    # task 1:
    print('Second task')
    print(f'Test answer: {task_1("test.txt")}')   # expected: 4
    print(f'Final answer: {task_1("input.txt")}') # expected: 373
