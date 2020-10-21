###
# [PROG] :  Smallest and largest number in a list
# [LANG] :  Python
# [AUTH] :  BooeySays
# [DESC] :  Enter a bunch of numbers and the script will start
#           when a negative number is entered. After, it will
#           spit out the smallest and the largest number from
#           the list.
# [EDTR] :  PyCharm 2020.2.1
# [LAB#] :  5.20.1: LAB: Brute force equation solver
###

''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

''' Type your code here. '''

solution = False

for x in range(-10,11):
    for y in range(-10,11):
        if (a * x + b * y == c) and (d * x + e * y ==f):
            print(x, y)
            solution = True

if (solution == False):
    print("No solution")