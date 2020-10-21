###
# [PROG] :  Smallest and largest number in a list
# [LANG] :  Python
# [AUTH] :  BooeySays
# [DESC] :  Enter a bunch of numbers and the script will start
#           when a negative number is entered. After, it will
#           spit out the smallest and the largest number from
#           the list.
# [EDTR] :  PyCharm 2020.2.1
# [LAB#] :  5.17 LAB: Output range with increment of 10
###



###
# Saved under pycharm at : /labs/5.17.1/
###

''' Type your code here. '''
first = int(input())
second = int(input())
if first > second:
    print("Second integer can't be less than the first.", end='')
while first <= second:
    print(first, end=' ')
    first = first + 10
print('')