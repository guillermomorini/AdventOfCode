textToInts = {
    "one": "1",
    "two": "2", 
    "three": "3", 
    "four": "4", 
    "five": "5", 
    "six": "6", 
    "seven": "7", 
    "eight": "8", 
    "nine": "9"
}

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
        return None
    
    if (len(line) == 0):
        return None
    
    ints = []
    result = 0

    for index, character in enumerate(line):
        try: 
            int(character)
            ints.append(character)
        except:
            foundNumber = getNumberFromWrittenVersion(index, line)

            if (foundNumber["found"]):
                ints.append(foundNumber["value"])
            pass

    if (len(ints) == 1):
        result = int(ints[0] + ints[0])
    else:
        result = int(ints[0] + ints[len(ints) - 1])
    
    return result

def getNumberFromWrittenVersion(index, line):
    for textLength in range(0, 3):
        subString = line[index:index+textLength]

        if subString in textToInts:
            return {
                "found": True,
                "value": textToInts[subString]
            }

    return {
        "found": False,
        "value": 0
    }