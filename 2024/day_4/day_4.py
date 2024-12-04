def import_data(filename: str) -> list[list[str]]:
    with open(filename) as file:
        lines = file.read().splitlines()
        return [[ch for ch in line]for line in lines]


def is_valid(x, y, size_x, size_y):
    return 0 <= x < size_x and 0 <= y < size_y


def find_in_direction(grid, n, m, word, index,
                      x, y, dir_x, dir_y):
    if index == len(word):
        return True

    if is_valid(x, y, n, m) and word[index] == grid[x][y]:
        return find_in_direction(grid, n, m, word, index + 1,
                                 x + dir_x, y + dir_y, dir_x, dir_y)

    return False


def search_word(grid, word):
    ans = []
    n = len(grid)
    m = len(grid[0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(n):
        for j in range(m):

            if grid[i][j] == word[0]:
                for dirX, dirY in directions:
                    if find_in_direction(grid, n, m, word, 0,
                                         i, j, dirX, dirY):
                        ans.append([i, j])

    return ans

def task_0(file: str) -> int:
    data = import_data(file)
    key_word = "XMAS"
    ans = search_word(data, key_word)
    return len(ans)

if __name__ == '__main__':
    # task 0:
    print('First task')
    print(f'Test answer: {task_0("test.txt")}')  # expected: 161
    print(f'Final answer: {task_0("input.txt")} '  # expected: 196826776
          f'\n-------------------\n')