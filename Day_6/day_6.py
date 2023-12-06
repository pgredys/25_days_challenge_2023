import functools
import re


def import_file(path: str) -> list[str]:
    with open(path, 'r') as file:
        return file.read().splitlines()


def decode_file(path: str) -> dict:
    lines = import_file(path)
    times = re.findall(r'\d+', lines[0])
    distances = re.findall(r'\d+', lines[1])
    return {'times': [eval(time) for time in times],
            'distances': [eval(distance) for distance in distances]}


def calc_distance(speed: int, time_left: int) -> float:
    return time_left * speed


def win_ways(time: int, distance: int) -> list[int]:
    button_times = []
    for hold_time in range(1, time):
        if calc_distance(hold_time, time - hold_time) > distance:
            button_times.append(hold_time)

    return button_times


def first_answer(path: str):
    races = decode_file(path)
    ways_numbers = []
    for race_number in range(len(races['times'])):
        ways_numbers.append(len(win_ways(races['times'][race_number], races['distances'][race_number])))

    return functools.reduce(lambda a, b: a * b, ways_numbers)


def second_answer(time, distance):
    return win_ways(time, distance)


if __name__ == '__main__':
    file_path = 'race.txt'
    print(f'First: {first_answer(file_path)}')
    # print(len(second_answer(71530, 940200))) # test
    print(f'Second: {len(second_answer(46828479, 347152214061471))}')
