def run():
    file1 = open('year2023/day9/input.txt', 'r')
    lines = file1.read().strip().split('\n')

    report = processLines(lines)

    result = getSumOfExtrapolations(report)
    return result

def processLines(lines):
    report = [[int(value) for value in line.split(" ")] for line in lines]

    return report

def getSumOfExtrapolations(report):
    extrapolations = getExtrapolations(report)
    sumOfExtrapolations = sum(extrapolations)

    return sumOfExtrapolations

def getExtrapolations(report):
    extrapolations = [getExtrapolation(valueHistory) for valueHistory in report]
    return extrapolations

def getExtrapolation(valueHistory):
    sequences_of_differences = get_sequences_of_differences(valueHistory)
    first_numbers_of_sequences_of_differences = [sequence_of_differences[0] for sequence_of_differences in sequences_of_differences]

    extrapolation = 0

    for first_number_of_sequences_of_differences in first_numbers_of_sequences_of_differences[::-1]:
        extrapolation = first_number_of_sequences_of_differences - extrapolation

    extrapolation = valueHistory[0] - extrapolation
    return extrapolation

def get_sequences_of_differences(valueHistory):
    sequences_of_differences = []

    current_sequence_of_differences = valueHistory
    done = is_all_zeroes(valueHistory)

    while not done:
        current_sequence_of_differences = get_sequence_of_differences(current_sequence_of_differences)
        sequences_of_differences.append(current_sequence_of_differences)
        
        done = is_all_zeroes(current_sequence_of_differences)

    return sequences_of_differences

def is_all_zeroes(values):
    return all([value == 0 for value in values])

def get_sequence_of_differences(values):
    sequence_of_differences = [values[i + 1] - values[i] for i in range(len(values) - 1)]

    return sequence_of_differences



