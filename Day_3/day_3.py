import re


def read_input(path):
    with open(path, 'r') as file:
        line_array = file.read().splitlines()
        cell_array = []
        for line in line_array:
            cell_array.append(line.split()[0])
        return cell_array


def is_part_number(engine_schematic, number_row, number_columns):
    if number_row == 0:
        rows = [number_row, number_row + 1]
    elif number_row == len(engine_schematic)-1:
        rows = [number_row -1, number_row]
    else:
        rows = [number_row - 1, number_row, number_row + 1]

    if number_columns[0] == 0:
        [number_columns.append(number_columns[-1] + 1) if number_columns[-1] + 1 <= len(
            engine_schematic[number_row])-1 else None]
    elif number_columns[-1] == len(engine_schematic[number_row]):
        [number_columns.insert(0, number_columns[0] - 1) if number_columns[0] - 1 <= 0 else None]
    else:
        [number_columns.append(number_columns[-1] + 1) if number_columns[-1] + 1 <= len(
            engine_schematic[number_row])-1 else None]
        [number_columns.insert(0, number_columns[0] - 1) if number_columns[0] - 1 >= 0 else None]

    numbers = []
    for row in rows:
        numbers.append([engine_schematic[row][i] for i in number_columns])

    numbers = [inner for outer in numbers for inner in outer]
    numbers = ''.join(numbers)

    if re.findall(r'[^\d.]', numbers):
        print(numbers)
        return True

    return False


def first_answer(path):
    engine_schematic = read_input(path)
    results = 0
    for index, _ in enumerate(engine_schematic):
        numbers_in_row = re.findall(r'\d+', engine_schematic[index])

        for ind, number in enumerate(numbers_in_row):
            number_index = engine_schematic[index].find(number)
            number_len = len(number)
            ans = is_part_number(engine_schematic, index, list(range(number_index, number_index + number_len)))
            if ans:
                # print(f'{numbers_in_row[ind]}')
                results += int(numbers_in_row[ind])

    return results


if __name__ == '__main__':
    # path = 'engine_test.txt'
    # answer = first_answer(path)
    # assert answer == 4361

    path = 'engine.txt'
    answer = first_answer(path)
    print(f'Answer: {answer}')
    assert answer == 531932
