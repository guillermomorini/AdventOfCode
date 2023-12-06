def run():
    file1 = open('year2023/day5/input.txt', 'r')
    lines = file1.read().strip().split('\n')
    
    result = processLines(lines)

    return result

def processLines(lines):
    cardWorths = []

    for line in lines:
        cardWorth = processLine(line)
        cardWorths.append(cardWorth)

    return sum(cardWorths)

def processLine(line):
    card = getCard(line)
    cardWorth = getCardWorth(card)
    return cardWorth
