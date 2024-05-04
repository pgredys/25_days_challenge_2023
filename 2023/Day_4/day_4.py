import re


def read_input(path):
    with open(path, 'r') as file:
        return file.read().splitlines()


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def get_points(count_matches: int):
    return 2 ** (count_matches - 1) if 2 ** (count_matches - 1) >= 1 else 0


def first_answer(path: str) -> int:
    lines = read_input(path)
    results = 0
    for line in lines:
        id = re.findall(r'\d+:', line)[0][:-1]
        winning_numbers = line.split(':', 1)
        winning_numbers = winning_numbers[1].split('|')[0]
        winning_numbers = re.findall(r'\d+', winning_numbers)
        winning_numbers = list(map(int, winning_numbers))

        numbers_you_have = line.split(':', 1)
        numbers_you_have = numbers_you_have[1].split('|')[1]
        numbers_you_have = re.findall(r'\d+', numbers_you_have)
        numbers_you_have = list(map(int, numbers_you_have))

        points_numbers = intersection(winning_numbers, numbers_you_have)

        results += get_points(len(points_numbers))

    return results


if __name__ == '__main__':
    first = first_answer('scratchcards.txt')
    assert first == 21558
    print(f'First answer: {first}')
