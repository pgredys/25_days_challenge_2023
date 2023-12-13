import numpy as np


def import_data(_path: str):
    with open(_path, 'r') as file:
        records = [record.splitlines() for record in file.read().split('\n\n')]
        for ind in range(len(records)):
            records[ind] = np.array([[*line] for line in records[ind]])
        return records


def vertical_reflection(_mirror: np.array, mode: int = 1) -> int:
    for i, column in enumerate(range(1, len(_mirror[0]))):
        mirror_plane = [column, column + 1]
        left_side = _mirror[:, mirror_plane[0] - min(i, len(_mirror[0]) - 2 - i) - 1:mirror_plane[0]]
        right_side = _mirror[:, column:mirror_plane[1] + min(i, len(_mirror[0]) - 2 - i)]

        if mode == 2:
            diff_mirror = np.compare_chararrays(left_side, np.fliplr(right_side), "==", True)
            if (~diff_mirror).sum() == 1:
                return i + 1
        else:
            if np.array_equal(left_side, np.fliplr(right_side)):
                return i + 1

    return 1_000_000


def horizontal_reflection(_mirror: np.array, mode: int = 1) -> int:
    for i, row in enumerate(range(1, len(_mirror))):
        mirror_plane = [row, row + 1]
        top_side = _mirror[mirror_plane[0] - min(i, len(_mirror) - 2 - i) - 1:mirror_plane[0], :]
        bottom_side = _mirror[row:mirror_plane[1] + min(i, len(_mirror) - 2 - i), :]

        if mode == 2:
            diff_mirror = np.compare_chararrays(top_side, np.flipud(bottom_side), "==", True)
            if (~diff_mirror).sum() == 1:
                return i + 1
        else:
            if np.array_equal(top_side, np.flipud(bottom_side)):
                return i + 1

    return 1_000_000


def first_answer(_path: str):
    mirrors = import_data(_path)
    results = 0
    for mirror in mirrors:
        vert = vertical_reflection(mirror)
        hor = horizontal_reflection(mirror)

        if min(vert, hor) == hor:
            results += 100 * hor
        elif min(vert, hor) == vert:
            results += vert

    return results


def second_answer(_path: str):
    mirrors = import_data(_path)
    results = 0
    for mirror in mirrors:
        vert = vertical_reflection(mirror, mode=2)
        hor = horizontal_reflection(mirror, mode=2)

        if min(vert, hor) == hor:
            results += 100 * hor
        elif min(vert, hor) == vert:
            results += vert

    return results


if __name__ == '__main__':
    path = 'mirrors.txt'
    ans = first_answer(path)
    print(f'First answer: {ans}')
    ans = second_answer(path)
    print(f'Second answer: {ans}')
