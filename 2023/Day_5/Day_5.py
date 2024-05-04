import re
import pandas as pd


def read_input(file_path: str) -> list:
    with open(file_path, 'r') as file:
        return file.read().splitlines()


def read_map(map_name: str, read_file: list[str]) -> list:
    start_index = 0
    for index, line in enumerate(read_file):
        if line.find(map_name) >= 0:
            start_index = index
        stop_index = index if line == '' else None
        if stop_index is not None and start_index > 0:
            map_lines = read_file[start_index + 1:stop_index]
            return [[int(int(j)) for j in i] for i in [(re.findall(r'\d+', cel)) for cel in map_lines]]


if __name__ == '__main__':
    read_lines = read_input('almanac_test.txt')
    seed_soil_map = read_map('seed-to-soil map:', read_lines)
    print(seed_soil_map)
    # soil_fertilizer_map = read_map('soil-to-fertilizer map:', read_lines)
    # fertilizer_water_map = read_map('fertilizer-to-water map', read_lines)
    # water_light_map = read_map('water-to-light map:', read_lines)
    # light_temperature_map = read_map('light-to-temperature map:', read_lines)
    # temperature_humidity_map = read_map('temperature-to-humidity map:', read_lines)
    # humidity_location_map = read_map('humidity-to-location map:', read_lines)
