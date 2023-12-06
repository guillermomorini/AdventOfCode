def run():
    file1 = open('year2023/day3/input.txt', 'r')
    lines = file1.read().strip().split('\n')
    
    result = processLines(lines)

    return result

def processLines(lines):
    lineLength = len(lines[0])
    partNumbers = []

    for lineNumber, line in enumerate(lines):
        i = 0
        while i < lineLength:
            try:
                int(line[i])
                numberLength = getNumberLength(line, i)
                number = int(line[i: i + numberLength])

                if isAPartNumber(lines, lineNumber, i, i + numberLength - 1):
                    partNumbers.append(number)

                i += numberLength

            except Exception as e:
                i += 1

    return sum(partNumbers)

def getNumberLength(line, index):
    tempIndex = index + 1
    length = 1

    while tempIndex < len(line):
        try:
            int(line[tempIndex])
            length += 1
            tempIndex += 1
        except:
            return length

    return length

def isAPartNumber(lines, lineNumber, firstIndex, lastIndex):
    surroundingCharacters =  getSurroundingCharacters(lines, lineNumber, firstIndex, lastIndex)
    result = containsSpecialCharacter(surroundingCharacters)
    return result

def getSurroundingCharacters(lines, lineNumber, firstIndex, lastIndex):
    surroundingCharacters = []
    
    lineLength = len(lines[0])
    lineCount = len(lines)

    #upper left character:
    if lineNumber > 0 and firstIndex > 0:
        upperLine = lines[lineNumber - 1]
        upperLeftCharacter = upperLine[firstIndex - 1]

        surroundingCharacters.append(upperLeftCharacter)

    #characters directly above
    if lineNumber > 0:
        upperLine = lines[lineNumber - 1]

        for index in range(firstIndex, lastIndex + 1):
            surroundingCharacters.append(upperLine[index])

    #upper right character:
    if lineNumber > 0 and lastIndex < lineLength - 1:
        upperLine = lines[lineNumber - 1]
        rightCharacter = upperLine[lastIndex + 1]

        surroundingCharacters.append(rightCharacter)
    
    #left character:
    if firstIndex > 0:
        line = lines[lineNumber]
        leftCharacter = line[firstIndex - 1]

        surroundingCharacters.append(leftCharacter)

    #right character:
    if lastIndex < lineLength - 1:
        line = lines[lineNumber]
        rightCharacter = line[lastIndex + 1]

        surroundingCharacters.append(rightCharacter)

    #lower left character:
    if lineNumber < lineCount - 1 and firstIndex > 0:
        lowerLine = lines[lineNumber + 1]
        lowerLeftCharacter = lowerLine[firstIndex - 1]

        surroundingCharacters.append(lowerLeftCharacter)

    #characters directly below
    if lineNumber < lineCount - 1:
        lowerLine = lines[lineNumber + 1]
        
        for index in range(firstIndex, lastIndex + 1):
            surroundingCharacters.append(lowerLine[index])

    #lower right character:
    if lineNumber < lineCount - 1 and lastIndex < lineLength - 1:
        lowerLine = lines[lineNumber + 1]
        lowerRightCharacter = lowerLine[lastIndex + 1]

        surroundingCharacters.append(lowerRightCharacter)
    
    return surroundingCharacters

def containsSpecialCharacter(characters):
    for character in characters:
        if isSpecialCharacter(character):
            return True
    
    return False

def isSpecialCharacter(character):
    try:
        int(character)
        return False
    except:
        return character != '.'
