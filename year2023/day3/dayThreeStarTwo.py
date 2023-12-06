def run():
    file1 = open('year2023/day3/input.txt', 'r')
    lines = file1.read().strip().split('\n')
    
    result = processLines(lines)

    return result

def processLines(lines):
    gearRatios = []

    for lineNumber, line in enumerate(lines):
        for index, character in enumerate(line):
            if line[index] == '*':
                gearRatio = getGearRatio(lines, lineNumber, index)
                gearRatios.append(gearRatio)
                
    return sum(gearRatios)

def getGearRatio(lines, lineNumber, index):
    surroundingNumbers = getSurroundingNumbers(lines, lineNumber, index)

    if len(surroundingNumbers) == 2:
        gearRatio = surroundingNumbers[0] * surroundingNumbers[1]
        return gearRatio
    else:
        return 0

def getSurroundingNumbers(lines, lineNumber, index):
    surroundingNumbers = []
    lineCount = len(lines)

    #upper line:
    if lineNumber > 0:
        upperLine = lines[lineNumber - 1]
        getSurroundingNumbersInLineResult = getSurroundingNumbersInLine(upperLine, index)
        surroundingNumbers.extend(getSurroundingNumbersInLineResult)
    
    #current line:
    line = lines[lineNumber]
    getSurroundingNumbersInLineResult = getSurroundingNumbersInLine(line, index)
    surroundingNumbers.extend(getSurroundingNumbersInLineResult)

    #lower line:
    if lineNumber < lineCount - 1:
        lowerLine = lines[lineNumber + 1]
        getSurroundingNumbersInLineResult = getSurroundingNumbersInLine(lowerLine, index)
        surroundingNumbers.extend(getSurroundingNumbersInLineResult)

    return surroundingNumbers

def getSurroundingNumbersInLine(line, index):
    surroundingNumbers = []
    indexCharacter = line[index]
    lineLength = len(line)

    if indexCharacter.isdigit():
        #we know then that there can be at most one number.
        getNumberResult = getNumber(line, index)
        surroundingNumbers.append(getNumberResult["value"])

    else:
        #could be two numbers. Check left, and check right.

        #left
        if index > 0:
            getLeftNumberResult = getNumber(line, index - 1)
            if getLeftNumberResult["found"]:
                surroundingNumbers.append(getLeftNumberResult["value"])
        
        #right
        if index < lineLength - 1:
            getRightNumberResult = getNumber(line, index + 1)
            if getRightNumberResult["found"]:
                surroundingNumbers.append(getRightNumberResult["value"])

    return surroundingNumbers

def getNumber(line, index):
    if not line[index].isdigit():
        return {
            "found": False,
            "value": 0
        }
    
    digit = line[index]
    leftDigits = getDigitsToTheLeft(line, index)
    rightDigits = getDigitsToTheRight(line, index)

    return {
        "found": True,
        "value": int(leftDigits + digit + rightDigits)
    }

def getDigitsToTheLeft(line, index):
    digits = ""
    tempIndex = index - 1

    while tempIndex >= 0 and line[tempIndex].isdigit():
        digits = line[tempIndex] + digits
        tempIndex -= 1

    return digits

def getDigitsToTheRight(line, index):
    digits = ""
    lineLength = len(line)
    tempIndex = index + 1

    while tempIndex < lineLength and line[tempIndex].isdigit():
        digits = digits + line[tempIndex]
        tempIndex += 1

    return digits