import numpy as np


def import_data(_path: str) -> np.array:
    with open(_path, 'r') as file:
        text = file.read()
        return np.array([[*line] for line in text.split('\n')])


def move_up(_rocks_column: np.array, _ind: int) -> np.array:
    _rocks_column[_ind], _rocks_column[_ind - 1] = _rocks_column[_ind - 1], _rocks_column[_ind]
    return _rocks_column


def movable(_rocks_column: np.array, _ind: int) -> bool:
    if _rocks_column[_ind - 1] == '#' or _rocks_column[_ind - 1] == 'O' or _ind == 0 or _rocks_column[_ind] == '#':
        return False
    if _rocks_column[_ind - 1] == '.':
        return True


def after_tilting(_rocks_column: np.array) -> np.array:
    for i, item in enumerate(_rocks_column):
        ind = i
        while movable(_rocks_column, ind):
            _rocks_column = move_up(_rocks_column, ind)
            ind -= 1

    return _rocks_column


def get_load(_rocks: np.array) -> int:
    ud_rocks = np.flipud(_rocks)

    return sum(np.where(ud_rocks == 'O')[0] + 1)


def first_answer(_path: str) -> int:
    rocks = import_data(_path)
    for column_id in range(np.size(rocks, 1)):
        rocks[:, column_id] = after_tilting(rocks[:, column_id])
    return get_load(rocks)


if __name__ == '__main__':
    path = 'rocks.txt'
    ans1 = first_answer(path)
    print(f'First ans: {ans1}')
