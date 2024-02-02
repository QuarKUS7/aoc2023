import re


with open('5.txt') as f:
    input = f.read().splitlines()

seeds = re.findall('[0-9]+', input[0])
seeds = [int(i) for i in seeds]
mapping = False
map = ''
maps = {}
for i in input[2:]:
    if 'map' in i:
        maps[i] = []
        mapping = True
        map = i
    elif mapping and i != '':
        numps = re.findall('[0-9]+', i)
        numps = [int(i) for i in numps]
        maps[map].append(numps)
    elif i == '':
        map = ''
        mapping = False

def mapping(seeds, map):
    for i in range(len(seeds)):
        for interval in map:
            if interval[1] <= seeds[i] <= interval[1] + interval[2]:
                diff = seeds[i] - interval[1]
                new = interval[0] + diff
                seeds[i] = new
                break
    return seeds

for name, map in maps.items():
    seeds = mapping(seeds, map)
print(min(seeds))

print('----------------')

seeds = re.findall('[0-9]+', input[0])
seeds = [int(i) for i in seeds]

seedy = []
for i in range(0, len(seeds), 2):
    seedy.append((seeds[i], seeds[i] + seeds[i+1] - 1))

for map in maps.values():
    new = []
    while len(seedy) > 0:
        s,e = seedy.pop()
        for r in map:
            a, b, c = r
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:
                new.append((os - b + a, oe - b + a))
                if os > s:
                    seedy.append((s, os))
                if e > oe:
                    seedy.append((oe, e))
                break
        else:
            new.append((s, e))
    seedy = new
print(sorted(seedy)[0][0])
