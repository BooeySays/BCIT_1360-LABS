###
# [PROG] :  Smallest and largest number in a list
# [LANG] :  Python
# [AUTH] :  BooeySays
# [DESC] :  Enter a bunch of numbers and the script will start
#           when a negative number is entered. After, it will
#           spit out the smallest and the largest number from
#           the list.
# [EDTR] :  PyCharm 2020.2.1
# [LAB#] :  5.19.1: LAB: Countdown until matching digits
###

###
# Saved under pycharm at : /labs/5.19.1/
###

###
# Notes: I don't really understand what is being asked of me.
# Update: I think I understand what the question is asking of me  now..,
###

''' Type your code here. '''
x = int(input())

if 20 <= x <= 98:
    while x % 11 != 0:
        print(x)
        x -= 1
    print(x)
else:
    print("Input must be 20-98")
    
    
    
# FIRST ATTEMPT:
#
#    print(x, end='\n')
#    if x % 11 == 0:
#        break
#    x -= 1
#else:
#    print("Input must be 20-98")