# 1. Basic
for x in range(151):
    print(x)

#2 Multiples of Five
for x in range(5, 1001, 5):
    print(x)

# 3 Counting, the Dojo Way
for x in range(1, 101):
    if x % 10 == 0:
        print('Coding Dojo')
    elif x % 5 == 0:
        print('Coding')
    else:
        print(x)

# 4 Whoa. That Sucker's Huge
sum = 0
for x in range(1, 500000, 2):
    sum += x
print(sum)

#5 Countdown by Fours
for x in range(2018, 0, -4):
    print(x)

# 6 Flexible counter
lowNum = 2
highNum = 74
mult = 4
for x in range(lowNum, highNum+1):
    if x % mult == 0:
        print(x)