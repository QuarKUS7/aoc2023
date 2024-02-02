import re
from math import lcm


with open('8.txt') as f:
    input = f.read().splitlines()

instr = input[0]

nodes = {}
for node in input[2:]:
    reg = re.findall('[A-Z0-9]+', node)
    nodes[reg[0]] = (reg[1], reg[2])

lens = len(instr)
i = 0
place = 'AAA'
steps = 0
while place != 'ZZZ':
    node = nodes[place]
    ins = instr[i]
    if ins == 'R':
        place = node[1]
    else:
        place = node[0]
    i += 1
    i = i % lens
    steps += 1

print(steps)

starts = []
for a in nodes.keys():
    if a[-1] == 'A':
        starts.append(a)

cycles = []
i = 0
for start in starts:
    steps = 0
    while start[-1] != 'Z':
        node = nodes[start]
        ins = instr[i]
        if ins == 'R':
            start = node[1]
        else:
            start = node[0]
        i += 1
        i = i % lens
        steps += 1
    cycles.append(steps)

print(lcm(*cycles))
