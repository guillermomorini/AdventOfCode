def run():
    file1 = open('dayThree/input.txt', 'r')
    lines = file1.readlines()
    
    result = processLines(lines)
    return result

def processLines(lines):
    sum = 0

    lineLength = len(lines[0])
    print("line length" + str(lineLength))
    
    for index, currentLine in enumerate(lines):
        if index == 0:
            print('first line')
        elif (index == len(lines) - 1):
            print('last line')
        else:
            upperLine = lines[index - 1]
            lowerLine = lines[index + 1]

            for lineIndex, character in enumerate(currentLine):
                if lineIndex == 0:
                    pass
                elif lineIndex == lineLength - 1:
                    pass
                else:
                    try:
                        int(character)
                        print(character)
                    except:
                        pass

    
    return sum

