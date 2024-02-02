with open('9.txt') as f:
    input = f.read().splitlines()


seqs = []
for line in input:
    l = line.split(' ')
    l = [int(v) for v in l]
    seqs.append(l)


def step(seq, hist):
    diff = []
    for v in range(1, len(seq)):
        diff.append(seq[v] - seq[v-1])
    hist.append(diff)
    if all(v == 0 for v in diff):
        return hist
    return step(diff, hist)

def predict1(hist):
    p = 0
    for h in hist[::-1]:
        p += h[-1]
    return p

def predict2(hist):
    p = 0
    for h in hist[::-1]:
        p = h[0] - p
    return p

s = 0
for seq in seqs:
    hist = [seq]
    hist = step(seq, hist)
    pred = predict1(hist)
    s += pred
print(s)

s = 0
for seq in seqs:
    hist = [seq]
    hist = step(seq, hist)
    pred = predict2(hist)
    s += pred
print(s)


with open("9.txt", "r") as file:
    input = file.read().splitlines()


def get_next_value(history):
    if all(n == 0 for n in history):
        return 0
    else:
        diff = [history[i + 1] - history[i] for i in range(len(history) - 1)]
        return history[-1] + get_next_value(diff)


def get_prev_value(history):
    if all(n == 0 for n in history):
        return 0
    else:
        diff = [history[i + 1] - history[i] for i in range(len(history) - 1)]
        return history[0] - get_prev_value(diff)


print('========')

result1 = 0
result2 = 0
for line in input:
    history = [int(num) for num in line.split()]
    re= get_next_value(history)
    result1 += re
    result2 += get_prev_value(history)

print("Solution 1: ", result1)
print("Solution 2: ", result2)
