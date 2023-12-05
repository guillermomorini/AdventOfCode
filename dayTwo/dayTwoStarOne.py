def run():
    file1 = open('dayTwo/input.txt', 'r')
    lines = file1.readlines()
    
    result = processLines(lines)
    return result

def processLines(lines):
    sum = 0

    for line in lines:
        sum += processLine(line)
    
    return sum

def processLine(line):
    gameNumber = getGameNumber(line)
    gameData = getGameData(line)

    for setOfCubeCounts in gameData:
        for cubeCount in setOfCubeCounts:
            if isOutOfBounds(cubeCount[0], cubeCount[1]):
                return 0

    return gameNumber

def isOutOfBounds(cubeCount, cubeColor):
    if cubeColor == 'red' and cubeCount > 12:
        return True
    if cubeColor == 'green' and cubeCount > 13:
        return True
    if cubeColor == 'blue' and cubeCount > 14:
        return True
    
    return False

def getGameData(line):
    gameData = []

    lineWithoutGameNumber = getLineWithoutGameNumber(line)
    setsOfCubesLine = lineWithoutGameNumber.split(";")

    for setOfCubesLine in setsOfCubesLine:
        cubeCountLine = setOfCubesLine.split(',')
        setOfCubesArray = []

        for cubeCount in cubeCountLine:
            data = cubeCount.split(' ')
            setOfCubesArray.append([int(data[1]), data[2].replace("\n", "")])

        gameData.append(setOfCubesArray)

    return gameData


def getGameNumber(line):
    gameHeader = line.split(':')[0]
    gameNumber = int(gameHeader.split(' ')[1])
    return gameNumber

def getLineWithoutGameNumber(line):
    indexOfColon = line.index(':')
    return line[indexOfColon + 1 : len(line)]
