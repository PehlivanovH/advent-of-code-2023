def converthands(hand):
    cards = hand.split()[0]
    bid = hand.split()[1]

    # Group cards with same symbols
    groups = {}
    jokers = 0
    for card in cards:
        symbol = card[0]
        if symbol == 'J':
            jokers += 1
        elif symbol in groups:
            groups[symbol].append(card)
        else:
            groups[symbol] = [card]

    rank = '0'
    if len(groups) == 1 or jokers == 5:
        rank = '7' # 5 of a kind
    elif any(len(group) + jokers == 4 for group in groups.values()):
        rank = '6' # 4 of a kind
    elif len(groups) == 2 and any(len(group) + jokers == 3 for group in groups.values()) and any(len(group) == 2 for group in groups.values()):
        rank = '5' # Full house
    elif any(len(group) + jokers == 3 for group in groups.values()):
        rank = '4' # 3 of a kind
    elif len(groups) == 3 and any(len(group) == 2 for group in groups.values()):
        rank = '3' # 2 pairs
    elif any(len(group) + jokers == 2 for group in groups.values()):
        rank = '2' # 1 pair
    else:
        rank = '1' # High card

    cards_to_digit = {
        'A': '14',
        'K': '13',
        'Q': '12',
        'J': '01',
        'T': '10',
        '2': '02',
        '3': '03',
        '4': '04',
        '5': '05',
        '6': '06',
        '7': '07',
        '8': '08',
        '9': '09'
    }


    return {'cards': int(rank + ''.join([cards_to_digit[card] for card in cards])), 'bid': int(bid)}

def test():
    assert converthands('AAAAJ 3') == {'cards': 71414141401, 'bid': 3}
    assert converthands('AAAJJ 3') == {'cards': 71414140101, 'bid': 3}
    assert converthands('AAJJJ 3') == {'cards': 71414010101, 'bid': 3}
    assert converthands('AJJJJ 3') == {'cards': 71401010101, 'bid': 3}
    assert converthands('JJJJJ 3') == {'cards': 70101010101, 'bid': 3}
    assert converthands('AAAAA 3') == {'cards': 71414141414, 'bid': 3}

    assert converthands('AAAJ3 3') == {'cards': 61414140103, 'bid': 3}
    assert converthands('AAAA3 3') == {'cards': 61414141403, 'bid': 3}

    assert converthands('AAA33 3') == {'cards': 51414140303, 'bid': 3}
    assert converthands('AA33J 3') == {'cards': 51414030301, 'bid': 3}

    assert converthands('AAA34 3') == {'cards': 41414140304, 'bid': 3}
    assert converthands('AAJ34 3') == {'cards': 41414010304, 'bid': 3}

    assert converthands('AA334 3') == {'cards': 31414030304, 'bid': 3}

    assert converthands('AA534 3') == {'cards': 21414050304, 'bid': 3}
    assert converthands('AJ534 3') == {'cards': 21401050304, 'bid': 3}

    assert converthands('A8534 3') == {'cards': 11408050304, 'bid': 3}

if __name__ == "__main__":
    test()
    with open('day7/input', 'r') as file:
        hands = list(map(converthands, file.readlines()))
        hands.sort(key=lambda hand: hand['cards'])
       
        print(sum(map(lambda hand: hand[0] * hand[1], [(index + 1, hand['bid']) for index, hand in enumerate(hands)])))

