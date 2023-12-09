def run():
    file1 = open('year2023/day8/input.txt', 'r')
    lines = file1.readlines()

    input = processLines(lines)

    result = getResult(input["instructions"], input["network"])
    return result

def processLines(lines):
    network = {}

    for index in range(2, len(lines)):
        node = processLine(lines[index])

        network[node["value"]] = {
            "L": node["L"],
            "R": node["R"]
        }

    return {
        "instructions": lines[0].replace("\n", ""),
        "network": network
    }

def processLine(line):
    data = line.split(" = ")
    directionsData = data[1].split(", ")
    left = directionsData[0].replace("(", "")
    right = directionsData[1].replace(")\n", "")
    
    return {
        "value": data[0],
        "L": left,
        "R": right
    }

def getResult(instructions, network):
    numberOfSteps = 0

    currentNodeValue = 'AAA'
    currentNode = network[currentNodeValue]

    while (currentNodeValue != 'ZZZ'):
        for instruction in instructions:
            currentNodeValue = currentNode[instruction]
            currentNode = network[currentNodeValue]
            numberOfSteps += 1

    return numberOfSteps

