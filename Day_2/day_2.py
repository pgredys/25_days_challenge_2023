import re


def get_lines(file_path: str) -> list[str]:
    with open(file_path) as f:
        return f.readlines()


def parse_line(_line: str) -> dict:
    split_line = _line.split(':')
    Game = dict(id=int(re.findall(r'\d+', split_line[0])[0]))
    Game['red'] = 0
    Game['blue'] = 0
    Game['green'] = 0
    games = split_line[1].split(';')
    for game in games:
        cubes = game.split(',')
        for color in ['red', 'blue', 'green']:
            for cube in cubes:
                cubes_number = int(re.findall(r'\d+', cube)[0])
                if color in cube and cubes_number > Game[color]:
                    Game[color] = cubes_number
    return Game


def first_answer(file_path, constraints):
    lines = get_lines(file_path)
    result = 0
    for line in lines:
        game = parse_line(line)
        if game['red'] <= constraints['red'] and \
                game['blue'] <= constraints['blue'] and \
                game['green'] <= constraints['green']:
            result += game['id']
    return result


def calc_power(game):
    return game['red'] * game['green'] * game['blue']


def second_answer(file_path):
    lines = get_lines(file_path)
    result = 0
    for line in lines:
        game = parse_line(line)
        power = calc_power(game)
        result += power
    return result


if __name__ == '__main__':
    constraints = {'red': 12, 'blue': 14, 'green': 13}
    result = second_answer('games.txt', constraints)

    print(result)
