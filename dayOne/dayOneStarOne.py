def run():
    file1 = open('dayOne/input.txt', 'r')
    lines = file1.readlines()
    
    result = processLines(lines)
    return result

def processLines(lines):
    sum = 0
    
    for line in lines:
        sum += processLine(line)
    
    return sum

def processLine(line):
    if (not line):
        return 0
    
    if (len(line) == 0):
        return 0
    
    ints = []
    result = 0

    for character in line:
        try: 
            int(character)
            ints.append(character)
        except:
            pass

    if len(ints) == 1:
        result = int(ints[0] + ints[0])
    elif len(ints) > 1:
        result = int(ints[0] + ints[len(ints) - 1])
    
    return result
