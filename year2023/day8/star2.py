import math

def run():
    file1 = open('year2023/day8/input.txt', 'r')
    lines = file1.readlines()

    input = processLines(lines)

    result = getResults(input["instructions"], input["network"])
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

def getResults(instructions, network):
    startingNodeValues = [nodeValue for nodeValue in network.keys() if nodeValue[-1] == 'A']
    results = [getResult(startingNodeValue, instructions, network) for startingNodeValue in startingNodeValues]

    return math.lcm(*results)

def getResult(startingNodeValue, instructions, network):
    numberOfSteps = 0

    currentNodeValue = startingNodeValue
    done = currentNodeValue[-1] == 'Z'

    while not done:
        for instruction in instructions:
            nextNodeValue = network[currentNodeValue][instruction]
            currentNodeValue = nextNodeValue
            numberOfSteps += 1
            
        done = currentNodeValue[-1] == 'Z'
        
    return numberOfSteps
