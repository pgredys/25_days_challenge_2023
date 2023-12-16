import sys

sys.setrecursionlimit(10_000)

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
MOVES = ['R', 'L', 'D', 'U']
MIRRORS = {
    '.': {'R': ['R'], 'L': ['L'], 'D': ['D'], 'U': ['U']},
    '-': {'R': ['R'], 'L': ['L'], 'D': ['L', 'R'], 'U': ['L', 'R']},
    '|': {'R': ['D', 'U'], 'L': ['D', 'U'], 'D': ['D'], 'U': ['U']},
    '/': {'R': ['U'], 'L': ['D'], 'D': ['L'], 'U': ['R']},
    '\\': {'R': ['D'], 'L': ['U'], 'D': ['R'], 'U': ['L']},
}


def import_grid(_path):
    with open(_path) as file:
        return [list(x) for x in file.read().strip().split('\n')]


def start_possibilities(x_length, y_length):
    pos_positions = []
    for x in range(x_length):
        pos_positions.append((x, 0, 'R'))
        pos_positions.append((x, y_length - 1, 'L'))
    for y in range(y_length):
        pos_positions.append((0, y, 'D'))
        pos_positions.append((0, x_length - 1, 'U'))
    return pos_positions


def illuminated_from(start, grid):
    illuminated = set()

    def illuminate(x, y, dr):
        if (x, y, dr) in illuminated:
            return
        illuminated.add((x, y, dr))
        mr = grid[x][y]
        for nxt in MIRRORS[mr][dr]:
            nxt_dr = DIRECTIONS[MOVES.index(nxt)]
            nx = x + nxt_dr[0]
            ny = y + nxt_dr[1]
            if nx in range(len(grid)) and ny in range(len(grid[0])):
                illuminate(nx, ny, nxt)

    illuminate(start[0], start[1], start[2])
    return len(set([(x, y) for x, y, _ in illuminated]))


if __name__ == '__main__':
    path = 'layout.txt'
    grid = import_grid(path)

    print(illuminated_from((0, 0, 'R'), grid))

    possibilities = start_possibilities(len(grid), len(grid[0]))
    print(max(illuminated_from(test, grid) for test in possibilities))
