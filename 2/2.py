import re

BLUE = '([0-9]+) blue'
RED = '([0-9]+) red'
GREEN = '([0-9]+) green'

with open("2.txt") as f:
    input = f.read().splitlines()

data = {}

for line in input:
    game, rest = line.split(':')
    game_num = re.findall('[0-9]+', game)[0]
    data[game_num] = []

    subsets = rest.split(';')
    for subset in subsets:
        blue = re.findall(BLUE, subset)
        red = re.findall(RED, subset)
        green = re.findall(GREEN, subset)
        _set = {'blue': blue, 'green': green, 'red': red}
        data[game_num].append(_set)

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

possibles = []

for game, sets in data.items():
    for _set in sets:
        if _set['red'] != [] and int(_set['red'][0]) > RED_LIMIT:
            break
        if _set['green'] != [] and int(_set['green'][0]) > GREEN_LIMIT:
            break
        if _set['blue'] != [] and int(_set['blue'][0]) > BLUE_LIMIT:
            break
    else:
        possibles.append(game)

print(sum([int(pos) for pos in possibles]))

sum = 0
for game, sets in data.items():
    green = 0
    red = 0
    blue = 0
    for _set in sets:
        if _set['red'] != [] and int(_set['red'][0]) > red:
            red = int(_set['red'][0])
        if _set['blue'] != [] and int(_set['blue'][0]) > blue:
            blue = int(_set['blue'][0])
        if _set['green'] != [] and int(_set['green'][0]) > green:
            green = int(_set['green'][0])
    sum += (red * green * blue) # not safe
print(sum)
