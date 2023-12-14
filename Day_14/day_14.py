import numpy as np


def import_data(_path: str) -> np.array:
    with open(_path, 'r') as file:
        text = file.read()
        return np.array([[*line] for line in text.split('\n')])


def move_up(_rocks_column: np.array, _ind: int) -> np.array:
    _rocks_column[_ind], _rocks_column[_ind - 1] = _rocks_column[_ind - 1], _rocks_column[_ind]
    return _rocks_column


def movable_up(_rocks_column: np.array, _ind: int) -> bool:
    if _rocks_column[_ind - 1] == '#' or _rocks_column[_ind - 1] == 'O' or _ind == 0 or _rocks_column[_ind] == '#':
        return False
    if _rocks_column[_ind - 1] == '.':
        return True


def after_tilting(_rocks_column: np.array) -> np.array:
    for i, item in enumerate(_rocks_column):
        ind = i
        while movable_up(_rocks_column, ind):
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


def move_cycle(_rocks: np.array) -> np.array:
    # move north
    for col_id in range(np.size(_rocks, 1)):
        _rocks[:, col_id] = after_tilting(_rocks[:, col_id])

    # move west
    for row_id in reversed(range(np.size(_rocks, 1))):
        _rocks[row_id, :] = after_tilting(_rocks[row_id, :])

    # move south
    for col_id in (range(np.size(_rocks, 1))):
        _rocks = np.flipud(_rocks)
        _rocks[:, col_id] = after_tilting(_rocks[:, col_id])
        _rocks = np.flipud(_rocks)

    # move east
    for row_id in range(np.size(_rocks, 1)):
        _rocks = np.fliplr(_rocks)
        _rocks[row_id, :] = after_tilting(_rocks[row_id, :])
        _rocks = np.fliplr(_rocks)

    return _rocks


def move_cycles(_rocks: np.array, cycle_num: int) -> np.array:
    for i in range(cycle_num):
        _rocks = move_cycle(_rocks)
    return _rocks


def second_better(_path: str) -> int:
    _rocks = import_data(path)
    # period = 1000000007
    for i in range(1_000_000_000):
        _rocks = move_cycle(_rocks)

        if i == 900:
            g0 = _rocks

        # if i > 700 and np.all(np.char.equal(g0, _rocks)):
        #     period = i - 500

        if i > 900 and np.any(np.char.equal(g0, _rocks)) and (1_000_000_000 - i) % (i - 900) == 0:
            print(f'performed {i} loops')
            return get_load(_rocks)

        if i == 1000:
            print('SMART WAY FAILED YOU')
            return get_load(_rocks)


#             (1B - curent)% period == 0


if __name__ == '__main__':
    assert first_answer('rocks.txt') == 108641
    path = 'rocks.txt'
    rocks = import_data(path)
    print('Input:\n', rocks, '\n___________________________________________')

    path = 'rocks.txt'
    # print('Ans:', get_load(move_cycles(rocks, 1000)))
    print('Ans:', second_better(path))
