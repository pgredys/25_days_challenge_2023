import re


def import_data(file_name: str) -> str:
    with open(file_name) as f:
        return f.read()

def mul(record: str) -> int:
    x, y = re.findall(r'\d+', record)
    if int(x) > 999 or int(y) > 999:
        print(record)
    return int(x) * int(y)

def task_0(file_name: str) -> int:
    data = import_data(file_name)
    clean_data = re.findall(r'mul[(]\d+,\d+[)]', data)
    answer = 0
    for i in clean_data:
        answer += mul(i)
    return answer

def task_1(file_name: str) -> int:
    data = import_data(file_name)
    clean_data = re.findall(r"mul[(]\d+,\d+[)]|don't|do", data)

    mul_flag = True
    answer = 0
    for i in clean_data:
        if i == 'do':
            mul_flag = True
        elif i == "don't":
            mul_flag = False
        elif mul_flag:
            answer += mul(i)
    return answer

if __name__ == '__main__':
    # task 0:
    print('First task')
    print(f'Test answer: {task_0("test.txt")}')  # expected: 161
    print(f'Final answer: {task_0("input.txt")} '  # expected: 196826776
          f'\n-------------------\n')

    # task 1:
    print('Second task')
    print(f'Test answer: {task_1("test2.txt")}')  # expected: 48
    print(f'Final answer: {task_1("input.txt")}')  # expected: 106780429

