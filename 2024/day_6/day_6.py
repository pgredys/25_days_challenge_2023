
def import_data(filename: str):
    with open(filename) as f:
        lines =  f.read().splitlines()
        return [list(line) for line in lines]

def find_guard(string_arr, key_char):
    flattenedArr = [item for sublist in string_arr for item in sublist]
    try:
        index = flattenedArr.index(key_char)
        rows = len(string_arr[1])
        cols = len(string_arr[0])
        return index // cols, index % cols
    except ValueError:
        raise ValueError

def change_dir():
    num = 0
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    while True:
        yield dirs[num % 4]
        num += 1

def is_inside(pos, dir, size):
    if (0 <= pos[0] + dir[0] <= size[0] - 1) and (0 <= pos[1] + dir[1] <= size[1] - 1):
        return True
    return False

def is_valid_move(curr,curr_dir, laboratory_map):
    new_curr = [0,0]
    new_curr[0], new_curr[1] = curr[0] + curr_dir[0], curr[1] + curr_dir[1]

    if laboratory_map[new_curr[0]][new_curr[1]] != '#':
        return True
    return False

def move(curr,curr_dir):
    return curr[0] + curr_dir[0], curr[1] + curr_dir[1]


def task_0(file: str) -> int:
    lab_map = import_data(file)
    map_size = len(lab_map[0]), len(lab_map)

    guard_position = find_guard(lab_map, '^')  # {col, row}

    route = set()
    route.add(guard_position)

    direction = change_dir()
    current_dir = next(direction)

    while is_inside(guard_position, current_dir, map_size):

        if is_valid_move(guard_position, current_dir, lab_map):
            guard_position = move(guard_position, current_dir)
            route.add(guard_position)

        else:
            current_dir = next(direction)
            # print(current_dir)
        # break
    return len(route)



if  __name__ == '__main__':
    # task 0:
    print('First task')
    print(f'Test answer: {task_0("test.txt")}')  # expected: 41
    print(f'Final answer: {task_0("input.txt")} '  # expected: 4964
          f'\n-------------------\n')

