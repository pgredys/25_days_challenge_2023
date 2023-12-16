import re
from collections import defaultdict


def import_sequence(_path: str) -> list[str]:
    with open(_path, 'r') as file:
        return file.read().split(',')


def hash_value(_element: str) -> int:
    _value = 0
    for _character in _element:
        _value += ord(_character)
        _value *= 17
        _value = _value % 256

    return _value


def first_answer(_path: str) -> int:
    _sequences = import_sequence(_path)
    _hash_value = []
    for element in _sequences:
        _value = hash_value(element)
        _hash_value.append(_value)

    return sum(_hash_value)


def lens_index(_lenses: list[str], _label: str) -> int:
    for idn, s in enumerate(_lenses):
        if _label in s:
            return idn
    return -1


def get_focal_length(_lens: str) -> int:
    num = re.findall(r'\d+', _lens)
    return int(num[0])


def fill_boxes(_sequence: list[str]) -> defaultdict:
    _boxes = defaultdict(list)
    for element in _sequence:
        label, foc_lens = re.split(r'[=-]', element)
        box_num = hash_value(label)

        if foc_lens == '':
            index = lens_index(_boxes[box_num], label)
            if index >= 0:
                _boxes[box_num].pop(index)
        else:
            index = lens_index(_boxes[box_num], label)
            if index >= 0:
                _boxes[box_num][index] = label + ' ' + foc_lens
            else:
                _boxes[box_num].append(label + ' ' + foc_lens)
    return _boxes


def second_answer(path):
    sequence = import_sequence(path)
    boxes = fill_boxes(sequence)
    results = 0
    for k, lenses in boxes.items():
        if lenses:
            for i, lens in enumerate(lenses):
                value = (k + 1) * (i + 1) * get_focal_length(lens)
                results += value

    return results


if __name__ == '__main__':
    path = 'sequence.txt'
    ans1 = first_answer(path)
    assert ans1 == 1320 or ans1 == 503487

    ans2 = second_answer(path)
    assert ans2 == 145 or ans2 == 261505
