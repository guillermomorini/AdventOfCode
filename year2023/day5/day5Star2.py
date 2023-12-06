def run():
    file1 = open('year2023/day5/input.txt', 'r')
    lines = file1.read().strip().split('\n')
    
    result = processLines(lines)

    return result

def processLines(lines):
    seedRanges = getSeedRanges(lines[0])
    # print(seedRanges)
    maps = getMaps(lines)

    minLocation = getLocation(maps, seedRanges[0]["initial value"])
    print(minLocation)

    for seedRange in seedRanges:
        for seed in range(seedRange["initial value"], seedRange["initial value"] + seedRange["range"]):
            pass
            # location = getLocation(maps, seed)
            # print("location: " + str(location))

            # if location < minLocation:
            #     minLocation = location
            #     print("lowest location: " + str(minLocation))

    return minLocation

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

def getSeedRanges(line):
    data = line.split(': ')[1]
    seedData = [int(datum) for datum in data.split(" ")]

    seedRanges = []

    for index in range(0,len(seedData),2):
        seedRanges.append({
            "initial value" : seedData[index],
            "range" : seedData[index + 1]
        })

    return seedRanges