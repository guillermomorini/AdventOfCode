def run():
    file1 = open('year2023/day5/input.txt', 'r')
    lines = file1.read().strip().split('\n')
    
    result = processLines(lines)

    return result

def processLines(lines):
    seeds = getSeeds(lines[0])
    maps = getMaps(lines)

    locations = []

    for seed in seeds:
        location = getLocation(maps, seed)
        locations.append(location)
    
    return min(locations)

def getLocation(maps, seed):
    currentValue = seed

    for currentMap in maps:
        currentValue = getDestinationValue(currentMap["mapRange"], currentValue)

    return currentValue

def getDestinationValue(map, sourceValue):
    for mapRange in map:
        sourceRangeStart = mapRange["source range start"]
        rangeLength = mapRange["range length"]
        destinationRangeStart = mapRange["destination range start"] 

        if sourceValue >= sourceRangeStart and sourceValue < sourceRangeStart + rangeLength:
            return destinationRangeStart + sourceValue - sourceRangeStart
    
    return sourceValue

def getMaps(lines):
    maps = []
    currentMap = {
        "title": "",
        "mapRange": []
    }

    for index in range(2, len(lines)):
        currentLine = lines[index]

        if currentLine == '':
            maps.append(currentMap)
            currentMap = {
                "title": "",
                "mapRange": []
            }

        elif currentLine[0].isdigit():
            mapRange = getMapRange(currentLine)

            currentMap["mapRange"].append(mapRange)

        else:
            currentMap["title"] = currentLine[0: len(currentLine) - 1]
    
    maps.append(currentMap)

    return maps

def getMapRange(line):
    mapRangeData = line.split(" ")

    mapRange = {
        "source range start": int(mapRangeData[1]),
        "destination range start": int(mapRangeData[0]),
        "range length": int(mapRangeData[2])
    }

    return mapRange

def getSeeds(line):
    data = line.split(': ')[1]
    seeds = [int(datum) for datum in data.split(" ")]

    return seeds