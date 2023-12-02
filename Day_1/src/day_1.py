import re


def import_lines(file_path: str) -> list:
    with open(file_path) as f:
        return f.readlines()


def find_digits(line_with_digits: str) -> str:
    numbers_from_line = re.findall(r'\d+', line_with_digits)
    return ''.join(numbers_from_line)


def decode_number(str_digits: str) -> int:
    first_digit = str_digits[0]
    last_digit = str_digits[-1]
    return 10 * int(first_digit) + int(last_digit)


def decode_line(_line: str) -> str:
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    counter = {}
    for k, i in digits.items():
        if _line.find(k) >= 0:
            counter[k] = _line.find(k)

    counter = sorted(counter.items(), key=lambda x: x[1])
    counter = dict(counter)
    for k, _ in counter.items():
        try:
            _line = _line.replace(k, digits[k])
            # print(_line)
        except:
            continue

    # print(counter)
    return _line


if __name__ == '__main__':
    # lines = import_lines("Trebuchet.txt")
    #
    # results = 0
    # for index, line in enumerate(lines):
    #     digits = find_digits(line)
    #     number = decode_number(digits)
    #     results += number
    #
    # print(results)

    lines = import_lines("Trebuchet.txt")
    results = 0
    for index, line in enumerate(lines):
        new_line = decode_line(line)

        digits = find_digits(new_line)
        number = decode_number(digits)

        print(f'{line.strip()}::{new_line.strip()}::{number}')
        results += number
        # break

    print('\n', f'Results: {results}')
    # assert  results == 53221
