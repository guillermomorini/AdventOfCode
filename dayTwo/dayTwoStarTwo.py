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
    gameData = getGameData(line)

    maxCountRed = 0
    maxCountBlue = 0
    maxCountGreen = 0

    for setOfCubeCounts in gameData:
        for cubeCount in setOfCubeCounts:
            if cubeCount[1] == 'red' and maxCountRed < cubeCount[0]:
                maxCountRed = cubeCount[0]
            elif cubeCount[1] == 'green' and maxCountGreen < cubeCount[0]:
                maxCountGreen = cubeCount[0]
            elif cubeCount[1] == 'blue' and maxCountBlue < cubeCount[0]:
                maxCountBlue = cubeCount[0]

    return maxCountRed * maxCountGreen * maxCountBlue

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

def getLineWithoutGameNumber(line):
    indexOfColon = line.index(':')
    return line[indexOfColon + 1 : len(line)]
