def run():
    file1 = open('year2023/day14/input.txt', 'r')
    lines = file1.read().strip().split('\n')

    tilted_platform = get_tilted_platform(lines)
    pattern_notes_summary = get_total_load(tilted_platform)

    return pattern_notes_summary

def get_tilted_platform(platform):
    column_count = len(platform[0])

    tilted_platform = [''] * len(platform)

    for column_index in range(column_count):
        column = get_column(platform, column_index)

        tilted_column = get_tilted_column(column)
        add_column(tilted_platform, tilted_column)
    
    return tilted_platform

def print_platform(platform):
    for row in platform:
        print(row)

def get_tilted_column(column):
    for index, character in enumerate(column):
        if character == 'O':
            upperIndex = index - 1

            while upperIndex >= 0 and column[upperIndex] == '.':
                swap_characters_in_column(upperIndex, upperIndex + 1, column)
                upperIndex -= 1

    return column

def swap_characters_in_column(index1, index2, column):
    temp = column[index1]
    column[index1] = column[index2]
    column[index2] = temp

def add_column(platform, column):
    for index, character in enumerate(column):
        platform[index] = platform[index] + character
    
def get_column(platform, index):
    return [row[index] for row in platform]

def get_total_load(platform):
    total_load = sum([round_rocks_count.count('O')*(len(platform) - index)  for index, round_rocks_count in enumerate(platform)])
    return total_load