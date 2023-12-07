from functools import cmp_to_key

cardValues = {
    'A':14, 
    'K':13, 
    'Q':12,  
    'T':10, 
    '9': 9,
    '8': 8, 
    '7': 7, 
    '6': 6, 
    '5': 5, 
    '4': 4, 
    '3': 3, 
    '2': 2,
    'J': 1
}

typeValues = {
    "Five of a kind": 7,
    "Four of a kind": 6,
    "Full house": 5,    
    "Three of a kind": 4,
    "Two pair": 3,
    "One pair": 2,
    "High card": 1
}

def run():
    file1 = open('year2023/day7/input.txt', 'r')
    lines = file1.read().strip().split('\n')
    
    result = processLines(lines)

    return result

def processLines(lines):
    handsWithBids = []

    for line in lines:
        cards = line.split(' ')[0]
        hand = getHand(cards)
        bid = int(line.split(' ')[1])

        handsWithBids.append({
            "hand": hand,
            "bid": bid
        })

    sortedHandsWithBids = sorted(handsWithBids, key=cmp_to_key(compareHandsWithBids))
    totalWinnings = getTotalWinnings(sortedHandsWithBids)

    return totalWinnings

def getTotalWinnings(sortedHandsWithBids):
    totalWinnings = 0

    for index, handWithBid in enumerate(sortedHandsWithBids):
        totalWinnings += handWithBid["bid"] * (index + 1)

    return totalWinnings

def compareHandsWithBids(handWithBid1, handWithBid2):
    return compareHands(handWithBid1["hand"], handWithBid2["hand"])

def compareHands(hand1, hand2):
    typeComparison = compareHandTypes(hand1, hand2)

    if typeComparison == 0:
        strengthComparison = compareHandStrengths(hand1, hand2)
        return strengthComparison
    
    return typeComparison

def compareHandStrengths(hand1, hand2):
    for index, hand1Card in enumerate(hand1["cards"]):
        hand2Card = hand2["cards"][index]

        cardComparison = compareCardStrengths(hand1Card, hand2Card)

        if cardComparison != 0:
            return cardComparison

    return 0

def compareCardStrengths(card1, card2):
    card1Strength = cardValues[card1]
    card2Strength = cardValues[card2]

    if card1Strength > card2Strength:
        return 1
    
    if card1Strength < card2Strength:
        return -1
    
    return 0

def compareHandTypes(hand1, hand2):
    if hand1["type value"] > hand2["type value"]:
        return 1
    
    if hand1["type value"] < hand2["type value"]:
        return -1
    
    return 0

def getHand(cards):
    type = getHandType(cards)
    typeValue = typeValues[type]

    return {
        "cards": cards,
        "type": type,
        "type value": typeValue
    }

def getHandType(hand):
    cardOccurrences = getCardOccurrences(hand)
    distinctCards = list(cardOccurrences.keys())
    distinctCardCount = len(distinctCards)
    
    if distinctCardCount == 5:
        return "High card"
    
    if distinctCardCount == 4:
        return "One pair"

    if distinctCardCount == 1:
        return  "Five of a kind"
    
    if distinctCardCount == 2:
        firstCard = distinctCards[0]

        if(cardOccurrences[firstCard] == 1 or cardOccurrences[firstCard] == 4):
            return "Four of a kind"
        
        return "Full house"
    
    if 3 in cardOccurrences.values():
        return "Three of a kind",

    return "Two pair"

def getCardOccurrences(cards):
    cardOccurrences = {}

    for card in cards:
        if card in cardOccurrences.keys():
            cardOccurrences[card] += 1
        else:
            cardOccurrences[card] = 1
    
    return cardOccurrences