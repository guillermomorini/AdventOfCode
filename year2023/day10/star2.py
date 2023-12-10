import math

def run():
    file1 = open('year2023/day10/input.txt', 'r')
    lines = file1.read().strip().split('\n')

    farthestStepCount = getArea(lines)

    return farthestStepCount

def getArea(landscape):
    pipeMap = getPipeMap(landscape)
    for line in pipeMap:
        print("".join(line))    
    
    print()

    area = 0

    for line in pipeMap:
        print("".join(line))
        inside = False
        lineArea = 0

        for character in line:
            if character in ['|', 'F', '7', 'J', 'L', 'S']:
                inside = not inside
                print(character)
                print(inside)
            else:
                if inside and character == '0':
                    lineArea += 1
                    print(character)
                    print("new line area: " + str(lineArea))
        
        print(lineArea)
        area += lineArea

    return area

def getPipeMap(landscape):
    pipeMap = [['0'] * len(landscapeRow) for landscapeRow in landscape]

    startingPosition = getStartingPosition(landscape)
    pipeMap[startingPosition[0]][startingPosition[1]] = 'S'

    startingPositionNeighbors = get_starting_position_neighbors(landscape, startingPosition)

    pointerPosition = startingPositionNeighbors[0]
    pipeMap[pointerPosition[0]][pointerPosition[1]] = landscape[pointerPosition[0]][pointerPosition[1]]

    previousPointerPosition = startingPosition

    while landscape[pointerPosition[0]][pointerPosition[1]] != 'S':
        nextPointerPosition = getNextPosition(landscape, previousPointerPosition, pointerPosition)
        previousPointerPosition = pointerPosition
        pointerPosition = nextPointerPosition
        pipeMap[pointerPosition[0]][pointerPosition[1]] = landscape[pointerPosition[0]][pointerPosition[1]]

    return pipeMap

def getStartingPosition(landscape):
    for columnIndex, column in enumerate(landscape):
        for rowIndex, row in enumerate(column):
            if landscape[columnIndex][rowIndex] == "S":
                return [columnIndex, rowIndex]

def get_starting_position_neighbors(landscape, startingPosition):
    neighbors = []
    columnIndex = startingPosition[0]
    rowIndex = startingPosition[1]

    #north
    if columnIndex > 0:
        northIndex = columnIndex - 1
        northCharacter = landscape[northIndex][rowIndex]

        if northCharacter in ['F','|','7','S']:
            neighbors.append([northIndex, rowIndex])

    #south
    if columnIndex < len(landscape) - 1:
        southIndex = columnIndex + 1
        southCharacter = landscape[southIndex][rowIndex]

        if southCharacter in ['L','|', 'J','S']:
            neighbors.append([southIndex, rowIndex])

    #east
    if rowIndex < len(landscape[0]) - 1:
        eastIndex = rowIndex + 1
        eastCharacter = landscape[columnIndex][eastIndex]

        if eastCharacter in ['7','-', 'J','S']:
            neighbors.append([columnIndex, eastIndex])

    #west
    if rowIndex > 0:
        westIndex = rowIndex - 1
        westCharacter = landscape[columnIndex][westIndex]

        if westCharacter in ['F', '-', 'L','S']:
            neighbors.append([columnIndex, westIndex])
    
    return neighbors

def get_nonstarting_position_neighbors(landscape, position):
    neighbors = []
    columnIndex = position[0]
    rowIndex = position[1]
    currentCharacter = landscape[columnIndex][rowIndex]

    if currentCharacter == 'F':
        neighbors.append([columnIndex, rowIndex + 1])
        neighbors.append([columnIndex + 1, rowIndex])

    if currentCharacter == '-':
        neighbors.append([columnIndex, rowIndex + 1])
        neighbors.append([columnIndex, rowIndex - 1])

    if currentCharacter == '7':
        neighbors.append([columnIndex, rowIndex - 1])
        neighbors.append([columnIndex + 1, rowIndex])

    if currentCharacter == '|':
        neighbors.append([columnIndex - 1, rowIndex])
        neighbors.append([columnIndex + 1, rowIndex])
    
    if currentCharacter == 'J':
        neighbors.append([columnIndex, rowIndex - 1])
        neighbors.append([columnIndex - 1, rowIndex])

    if currentCharacter == 'L':
        neighbors.append([columnIndex, rowIndex + 1])
        neighbors.append([columnIndex - 1, rowIndex])
    
    return neighbors

def getNextPosition(landscape, previousPosition, currentPosition):
    neighbors = get_nonstarting_position_neighbors(landscape, currentPosition)

    if neighbors[0][0] == previousPosition[0] and neighbors[0][1] == previousPosition[1]:
        return neighbors[1]
    
    return neighbors[0]