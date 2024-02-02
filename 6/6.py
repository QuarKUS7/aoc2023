import re


with open('6.txt') as f:
    input = f.read().splitlines()

print(input)

times = re.findall('[0-9]+', input[0])
dist = re.findall('[0-9]+', input[1])

times = [int(t) for t in times]
dist = [int(d) for d in dist]
print(times)
print(dist)


ways = 1
for time, d in zip(times, dist):
    print(time)
    print(d)
    w = 0
    for v in range(time+1):
        travel = (time - v) * v
        if travel > d:
            w += 1
        print(travel)
    ways = ways * w

print(ways)
print('----------')

times = re.findall('[0-9]+', input[0])
dist = re.findall('[0-9]+', input[1])
times = int(''.join(times))
dist = int(''.join(dist))


w = 0
for v in range(times+0):
    travel = (times - v) * v
    if travel > dist:
        w += 1
print(w)
