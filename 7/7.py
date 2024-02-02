from collections import Counter

with open('7.txt') as f:
    input = f.read().splitlines()
print(input)

cards = {}


for line in input:
    card, bid = line.split(' ')
    print(card)
    cards[card] = int(bid)

print(cards)

types = [list() for _ in range(7)]
print(types)

for card in cards.keys():
    print(card)
    c = Counter(card)
    most = c.most_common(2)
    f = most[0][1]
    if f == 5:
        types[0].append(card)
    elif f == 4:
        types[1].append(card)
    elif f == 3:
        s = most[1][1]
        if s == 2:
            types[2].append(card)
        else:
            types[3].append(card)
    elif f == 2:
        s = most[1][1]
        if s == 2:
            types[4].append(card)
        else:
            types[5].append(card)
    else:
        types[6].append(card)

d = { "A": -1,
      "K": -2,
      "Q": -3,
      "J": -4,
      "T": -5,
      "9": -6,
      "8": -7,
      "7": -8,
      "6": -9,
      "5": -10,
      "4": -11,
      "3": -12,
      "2": -13,
     }
result = sorted(types[3], key=lambda x:(d[x[0]], d[x[1]], d[x[2]], d[x[3]], d[x[4]]))

print(types)
score = 0
rank = 0
for type in types[::-1]:
    result = sorted(type, key=lambda x:(d[x[0]], d[x[1]], d[x[2]], d[x[3]], d[x[4]]))
    for t in result:
        rank += 1
        score += rank * cards[t]

print(score)

types = [list() for _ in range(7)]
joker = False
for card in cards.keys():
    print(card)
    joker = card.count('J')
    print(joker)
    c = Counter(card)
    most = c.most_common(2)
    f = most[0][1]
    if f == 5:
        types[0].append(card)
    elif f == 4:
        if joker > 0:
            types[0].append(card)
        else:
            types[1].append(card)
    elif f == 3:
        s = most[1][1]
        if s == 2:
            if joker == 2:
                types[0].append(card)
            elif joker == 3:
                types[0].append(card)
            else:
                types[2].append(card)
        else:
            if joker == 3:
                types[1].append(card)
            elif joker == 1:
                types[1].append(card)
            else:
                types[3].append(card)
    elif f == 2:
        s = most[1][1]
        if s == 2:
            if joker == 2:
                types[1].append(card)
            elif joker == 1:
                types[2].append(card)
            else:
                types[4].append(card)
        else:
            if joker == 2:
                types[3].append(card)
            elif joker == 1:
                types[3].append(card)
            else:
                types[5].append(card)
    else:
        if joker == 1:
            types[5].append(card)
        else:
            types[6].append(card)
    joker = 0

d = { "A": -1,
      "K": -2,
      "Q": -3,
      "T": -5,
      "9": -6,
      "8": -7,
      "7": -8,
      "6": -9,
      "5": -10,
      "4": -11,
      "3": -12,
      "2": -13,
      "J": -14,
     }

score = 0
rank = 0
for type in types[::-1]:
    result = sorted(type, key=lambda x:(d[x[0]], d[x[1]], d[x[2]], d[x[3]], d[x[4]]))
    for t in result:
        rank += 1
        score += rank * cards[t]

print(types)
print(score)
