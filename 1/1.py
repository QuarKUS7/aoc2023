import re


with open("1.txt") as input:
    lines = input.read().splitlines()

sum = 0

for line in lines:
    digits = re.findall('[0-9]', line)
    cal_value = int(digits[0]+digits[-1])
    sum += cal_value

print(sum)


sum = 0

LETTERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in lines:
    num = ''

    digit = ''
    dig = ''
    s_left = 9999999
    s_right = 9999999
    for i, letter in enumerate(LETTERS):
        index = line.find(letter)
        if index != -1 and index <= s_left:
            s_left = index
            digit = i+1
        index = line.find(str(i+1))
        if index != -1 and index <= s_right:
            s_right = index
            dig = int(line[index])
    if s_left < s_right:
        num += str(digit)
    else:
        num += str(dig)

    digit = ''
    dig = ''
    e_left = 0
    e_right = 0

    for i, letter in enumerate(LETTERS):
        index = line.rfind(letter)
        if index != -1 and index >= e_left:
            e_left = index
            digit = i+1
        index = line.rfind(str(i+1))
        if index != -1 and index >= e_right:
            e_right = index
            dig = int(line[index])
    if e_left > e_right:
        num += str(digit)
    else:
        num += str(dig)
    sum += int(num)

print(sum)
