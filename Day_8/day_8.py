import re


def import_map(path: str) -> [str, dict]:
    with open(path, 'r') as file:
        _directions, _, *_map = file.read().splitlines()
    nodes = {}
    [nodes.update(decode_map(line)) for line in _map]
    return _directions, nodes


def decode_map(node: str) -> dict:
    coords = list(re.findall(r'\w+', node))
    map_node = {coords[0]: [coords[1], coords[2]]}
    return map_node


def get_dir(turn_number: int, directions):
    dir_length = len(directions)
    return directions[turn_number % dir_length]


def get_last(_map: dict):
    return list(_map.keys())[-1]

def get_first(_map: dict):
    return list(_map.keys())[0]


def first_answer(maps, directions):
    current_node = 'AAA'
    last_node = 'ZZZ'

    counter = 0
    while current_node != last_node:
        inst = get_dir(counter, directions)
        if inst == 'R':
            current_node = maps[current_node][1]
            counter += 1
        elif inst == 'L':
            current_node = maps[current_node][0]
            counter += 1

    return counter


if __name__ == '__main__':
    file_path = "map.txt"
    directions, maps = import_map(file_path)
    # print(directions)
    # print(maps)
    print(first_answer(maps, directions))
    # print(get_dir(2))
