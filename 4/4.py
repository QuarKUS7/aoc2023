import re, math

with open('4.txt') as f:
    input = f.read().splitlines()

cards = {}
point = 0
for line in input:
    card, rest = line.split(':')
    have, win = rest.split('|')
    card = re.findall('[0-9]+', card)
    have = re.findall('[0-9]+', have)
    win = re.findall('[0-9]+', win)
    win = [int(h) for h in win]
    have = [int(h) for h in have]
    common = set(win) & set(have)
    if len(common) >= 1:
        point += math.pow(2, len(common)-1)
    cards[int(card[0])] = len(common)
print(int(point))

def compute(card, cards, score):
    score += 1
    wins = cards[card]
    if wins == 0:
        return score
    for i in range(wins):
        score = compute(i+card+1, cards, score)
    return score

out = 0

for card in cards:
    out += compute(card, cards, 0)
print(out)
