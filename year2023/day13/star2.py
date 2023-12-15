def run():
    file1 = open('year2023/day13/input.txt', 'r')
    lines = file1.read().strip().split('\n')
    
    patterns = get_patterns(lines)
    pattern_notes_summary = get_pattern_notes_summaries_with_fixed_smudges(patterns)

    return pattern_notes_summary

def get_pattern_notes_summaries_with_fixed_smudges(patterns):
    row_counts = []
    column_counts = []
    
    for pattern in patterns:
        pattern_notes_summary = get_pattern_notes_summary_with_fixed_smudges(pattern)

        row_counts.append(pattern_notes_summary["horizontal line of reflection"])
        column_counts.append(pattern_notes_summary["vertical line of reflection"])

    pattern_notes_summary = sum(row_counts) * 100 + sum(column_counts) 

    return pattern_notes_summary

def fix_smudge(row_index, column_index, pattern):
    character = pattern[row_index][column_index]

    if character == '.':
        pattern[row_index] = pattern[row_index][:column_index] + '#' + pattern[row_index][column_index + 1:]
    else:
        pattern[row_index] = pattern[row_index][:column_index] + '.' + pattern[row_index][column_index + 1:]

def get_pattern_notes_summary_with_fixed_smudges(pattern):
    #first, get the original answer. Then we will fix smudges until we get a different answer.
    pattern_notes_summary_with_smudge = get_pattern_notes_summary(pattern)

    height = len(pattern)
    width = len(pattern[0])

    print("ORIGINAL PATTERN")
    for line in pattern:
        print(line)
    print()
    print("horizontal line of reflection: " + str(pattern_notes_summary_with_smudge["horizontal line of reflection"]))
    print("vertical line of reflection: " + str(pattern_notes_summary_with_smudge["vertical line of reflection"]))
    print()


    for row_index in range(height):
        for column_index in range(width):
            pattern_copy = pattern.copy()
            fix_smudge(row_index, column_index, pattern_copy)

            pattern_notes_summary_with_fixed_smudge = get_pattern_notes_summary(pattern_copy)
            
            if isValidAnswer(pattern_notes_summary_with_fixed_smudge) and isDifferentAnswer(pattern_notes_summary_with_smudge, pattern_notes_summary_with_fixed_smudge):
                for line in pattern_copy:
                    print(line)
                print()
                print("smudge at (" + str(column_index) + ", " + str(row_index) + ")")
                print("horizontal line of reflection: " + str(pattern_notes_summary_with_fixed_smudge["horizontal line of reflection"]))
                print("vertical line of reflection: " + str(pattern_notes_summary_with_fixed_smudge["vertical line of reflection"]))
                print()

                return pattern_notes_summary_with_fixed_smudge

    return {
        "horizontal line of reflection": 0,
        "vertical line of reflection": 0
    }

def isValidAnswer(pattern_notes_summary):
    return pattern_notes_summary["horizontal line of reflection"] != 0 or pattern_notes_summary["vertical line of reflection"] != 0

def isDifferentAnswer(pattern_notes_summary1, pattern_notes_summary2):
    return pattern_notes_summary1["horizontal line of reflection"] != pattern_notes_summary2["horizontal line of reflection"] or pattern_notes_summary1["vertical line of reflection"] != pattern_notes_summary2["vertical line of reflection"]


def get_pattern_notes_summary(pattern):
    horizontal_line_of_reflection_index = get_horizontal_line_of_reflection_index(pattern)

    #apparently we are supposed to only return one line of reflection, checking horizontal first.
    # if (horizontal_line_of_reflection_index != 0):
    #     return {
    #     "horizontal line of reflection": horizontal_line_of_reflection_index,
    #     "vertical line of reflection": 0
    # }

    vertical_line_of_reflection_index = get_vertical_line_of_reflection_index(pattern)

    # for line in pattern:
    #     print(line)
    
    # print()
    # print("horizontal line of reflection: " + str(horizontal_line_of_reflection_index))
    # print("vertical line of reflection: " + str(vertical_line_of_reflection_index))
    # print()
    # print()

    return {
        "horizontal line of reflection": horizontal_line_of_reflection_index,
        "vertical line of reflection": vertical_line_of_reflection_index
    }

def get_horizontal_line_of_reflection_index(pattern):
    height = len(pattern)
    possible_lines_of_reflection = range(1, height)

    for possible_line_of_reflection in possible_lines_of_reflection:
        if is_horizontal_line_of_reflection(possible_line_of_reflection, pattern):
            return possible_line_of_reflection
    
    return 0

def get_vertical_line_of_reflection_index(pattern):
    width = len(pattern[0])
    possible_lines_of_reflection = range(1, width)

    for possible_line_of_reflection in possible_lines_of_reflection:
        if (is_vertical_line_of_reflection(possible_line_of_reflection, pattern)):
            return possible_line_of_reflection

    return 0

def is_horizontal_line_of_reflection(index, pattern):
    lower_reflected_lines_count = index
    upper_reflected_lines_count = len(pattern) - index

    reflected_lines_count = min(lower_reflected_lines_count, upper_reflected_lines_count)

    for reflection_distance in range(1, reflected_lines_count + 1):
        upper_row = get_upper_row_by_reflection_distance(reflection_distance, index, pattern)
        lower_row = get_lower_row_by_reflection_distance(reflection_distance, index, pattern)

        if not lists_are_equal(lower_row, upper_row):
            return False

    return True

def is_vertical_line_of_reflection(index, pattern):
    left_reflected_lines_count = index
    right_reflected_lines_count = len(pattern[0]) - index

    reflected_lines_count = min(left_reflected_lines_count, right_reflected_lines_count)

    for reflection_distance in range(1, reflected_lines_count + 1):
        left_column = get_left_column_by_reflection_distance(reflection_distance, index, pattern)
        right_column = get_right_column_by_reflection_distance(reflection_distance, index, pattern)

        if not lists_are_equal(left_column, right_column):
            return False

    return True

def get_upper_row_by_reflection_distance(reflection_distance, line_of_reflection_index, pattern):
    upper_row_index = line_of_reflection_index - reflection_distance

    upper_row = pattern[upper_row_index]
    return upper_row

def get_lower_row_by_reflection_distance(reflection_distance, line_of_reflection_index, pattern):
    lower_row_index = line_of_reflection_index + reflection_distance - 1

    lower_row = pattern[lower_row_index]
    return lower_row

def get_left_column_by_reflection_distance(reflection_distance, line_of_reflection_index, pattern):
    left_column_index = line_of_reflection_index - reflection_distance

    left_column = get_column(left_column_index, pattern)
    return left_column

def get_right_column_by_reflection_distance(reflection_distance, line_of_reflection_index, pattern):
    right_column_index = line_of_reflection_index + reflection_distance - 1

    right_column = get_column(right_column_index, pattern)
    return right_column

def get_column(index, pattern):
    column = [row[index] for row in pattern]
    return column

def lists_are_equal(list1, list2):
    for index in range(len(list1)):
        value1 = list1[index]
        value2 = list2[index]

        if value1 != value2:
            return False

    return True

def get_patterns(lines):
    patterns = []

    current_pattern = []

    for line in lines:
        if line == '':
            patterns.append(current_pattern)
            current_pattern = []
        else:
            current_pattern.append(line)
    
    patterns.append(current_pattern)

    return patterns
