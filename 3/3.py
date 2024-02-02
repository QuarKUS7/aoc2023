with open('3.txt') as f:
    input = f.read().splitlines()

grid = input

def check(x, y, grid):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            try:
                p = grid[x+i][y+j]
                if p == '.' or p.isdigit():
                    continue
                else:
                    return false
            except:
                continue
    return True

num = False
numbers = []
alls = []
nu = []
for x in range(len(grid)):
    print(x)
    num = False
    incl = True
    nu = []
    for y in range(len(grid[0])):
        print(y)
        print(grid[x][y])
        if grid[x][y].isdigit():
            num = True
            if check(x, y, grid) != True:
                incl = False
            nu.append(grid[x][y])
        elif num == True:
            print(nu)
            if incl == True:
                numbers.append(int(''.join(nu)))
            alls.append(int(''.join(nu)))
            num = False
            nu = []
            incl = True
        else:
            continue
    if nu != []:
        if incl == True:
            numbers.append(int(''.join(nu)))
        alls.append(int(''.join(nu)))

print(sum(alls))
print(sum(numbers))
print(sum(alls) - sum(numbers))

#import re
#a = 0
#ak = []
#for line in grid:
#    print(line    f = re.findall('[0-9]+', line)
#    print(f)
#    for i in f:
#        a += int(i)
#        ak.append(int(i))
#print(ak)
#print(alls)
#for i,j in zip(ak, alls):
#    print(i,j)

num = False
numbers = []
alls = []
nu = []
for x in range(len(grid)):
    print(x)
    num = False
    incl = True
    nu = []
    for y in range(len(grid[0])):
        print(y)
        print(grid[x][y])
        if grid[x][y].isdigit():
            num = True
            if check(x, y, grid) != True:
                incl = False
            nu.append(grid[x][y])
        elif num == True:
            print(nu)
            if incl == True:
                numbers.append(int(''.join(nu)))
            alls.append(int(''.join(nu)))
            num = False
            nu = []
            incl = True
        else:
            continue
    if nu != []:
        if incl == True:
            numbers.append(int(''.join(nu)))
        alls.append(int(''.join(nu)))

print(sum(alls))
print(sum(numbers))
print(sum(alls) - sum(numbers))

def check_star(x, y, grid):
    aj = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            try:
                p = grid[x+i][y+j]
                if p == '.':
                    continue
                elif p.isdigit():
                    aj += 1
                else:
                    return False
            except:
                continue
    return True

gears = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == '*':
            check_star(x, y, grid)

#import re
#a = 0
#ak = []
#for line in grid:
#    print(line    f = re.findall('[0-9]+', line)
#    print(f)
#    for i in f:
#        a += int(i)
#        ak.append(int(i))
#print(ak)
#print(alls)
#for i,j in zip(ak, alls):
#    print(i,j)

