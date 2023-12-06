def run():
    file1 = open('year2023/day4/input.txt', 'r')
    lines = file1.read().strip().split('\n')
    
    result = processLines(lines)

    return result

def processLines(lines):
    cardWorths = [1] * len(lines)
    
    for index, line in enumerate(lines):
        cardWorth = processLine(line)

        for indexToIncrement in range(index + 1, index + 1 + cardWorth):
            if indexToIncrement < len(cardWorths):
                cardWorths[indexToIncrement] += cardWorths[index]

    return sum(cardWorths)

def processLine(line):
    card = getCard(line)
    cardWorth = getCardWorth(card)
    return cardWorth

def getCard(line):
    data = line.split(":")[1]

    winningNumbersText = data.split("|")[0]
    yourNumbersText = data.split("|")[1]

    winningNumbers = processNumbersText(winningNumbersText)
    yourNumbers = processNumbersText(yourNumbersText)

    return {
        "winning numbers" : winningNumbers,
        "your numbers" : yourNumbers
    }

def processNumbersText(numbersText):
    numbers = []

    for numberText in numbersText.split(" "):
        if (numberText.strip() != ""):
            number = numberText.strip()
            numbers.append(int(number))
    
    return numbers
    

def getCardWorth(card):
    yourWinningNumbers = []

    for winningNumber in card["winning numbers"]:
        if winningNumber in card["your numbers"]:
            yourWinningNumbers.append(winningNumber)
    
    if len(yourWinningNumbers) == 0:
        return 0
    
    return len(yourWinningNumbers)