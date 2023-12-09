def run():
    file1 = open('year2023/day6/input.txt', 'r')
    lines = file1.read().strip().split('\n')
    
    result = processLines(lines)

    return result

def processLines(lines):
    raceRecords = getRaceRecords(lines)
    recordBreakingOptionsCounts = []

    for raceRecord in raceRecords:
        recordBreakingOptionsCount = getRecordBreakingOptionsCount(raceRecord)
        recordBreakingOptionsCounts.append(recordBreakingOptionsCount)
    
    multiple = 1

    for recordBreakingOptionsCount in recordBreakingOptionsCounts:
        multiple = multiple*recordBreakingOptionsCount

    return multiple

def getRecordBreakingOptionsCount(raceRecord):
    recordBreakingOptions = getRecordBreakingOptions(raceRecord)
    return len(recordBreakingOptions)

def getRecordBreakingOptions(raceRecord):
    recordBreakingOptions = []
    time = raceRecord["time"]
    recordDistance = raceRecord["distance"]

    for speed in range(time):
        distance = speed * (time - speed)
        if (distance > recordDistance):
            recordBreakingOptions.append({
                "time": time,
                "distance": distance
            })
    
    return recordBreakingOptions

def getRaceRecords(lines):
    times = parseLine(lines[0])
    distances = parseLine(lines[1])

    print(times)
    print(distances)

    raceRecords = []

    for index, time in enumerate(times):
        raceRecords.append({
            "time": time,
            "distance": distances[index]
        })
    
    return raceRecords


def parseLine(line):
    textWithoutHeader = line.split(':')[1]

    data = ""

    for character in textWithoutHeader:
        if (character != ' '):
            data += (character)
    
    return [ int(data) ]

