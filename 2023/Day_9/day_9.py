import functools
import re


def import_measurements(file_path: str) -> list[list[int]]:
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        return [[int(i) for i in list(re.findall(r'-*\d+', line))] for line in lines]


def difference_in_line(line: list[int]) -> list[int]:
    dif = []
    for i in range(len(line) - 1):
        dif.append((line[i + 1] - line[i]))
    return dif


def difference(line: list[int]):
    dif = [line]
    while any(dif[-1]) != 0:
        dif.append(difference_in_line(dif[-1]))
    return dif


def prediction(dif: list[list[int]]) -> int:
    lasts = [line[-1] for line in dif]
    lasts.reverse()
    return functools.reduce(lambda a, b: a + b, lasts)


def first_answer():
    paths = ['OASIS_test.txt', 'OASIS.txt']
    answer = []
    for path in paths:
        measurements = import_measurements(path)
        result = 0
        for measurement in measurements:
            differences = difference(measurement)
            result += prediction(differences)
        answer.append(result)
    if __name__ == '__main__':
        print(f'Test answer: {answer[0]} \nPart 1 answer: {answer[1]}\n')

    return answer


def difference_in_line_back(line: list[int]) -> list[int]:
    dif = []
    for i in reversed(range(len(line) - 1)):
        dif.append((line[i+1] - line[i]))
    dif.reverse()
    return dif


def difference_back(line: list[int]):
    dif = [line]
    while any(dif[-1]) != 0:
        dif.append(difference_in_line_back(dif[-1]))
    return dif


def prediction_back(dif: list[list[int]]) -> int:
    firsts = [line[0] for line in dif]
    firsts.reverse()
    return functools.reduce(lambda a, b: b - a, firsts)


def second_answer():
    paths = ['OASIS_test.txt', 'OASIS.txt']
    answer = []
    for path in paths:
        measurements = import_measurements(path)
        result = 0
        for measurement in measurements:
            diff = difference_back(measurement)
            # print(diff)
            result += prediction_back(diff)
        answer.append(result)
    if __name__ == '__main__':
        print(f'Test answer: {answer[0]} \nPart 2 answer: {answer[1]}\n')

    return answer


if __name__ == '__main__':
    first_answer()
    #     here part 2
    second_answer()
