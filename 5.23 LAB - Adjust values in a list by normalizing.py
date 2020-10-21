###
# [PROG] :  Smallest and largest number in a list
# [LANG] :  Python
# [AUTH] :  BooeySays
# [DESC] :  Enter a bunch of numbers and the script will start
#           when a negative number is entered. After, it will
#           spit out the smallest and the largest number from
#           the list.
# [EDTR] :  PyCharm 2020.2.1
# [LAB#] :  5.23.1: LAB: Adjust values in a list by normalizing
###

firstNum = int(input())     # Gets the first number which will be used to tell how many subsequent more numbers to enter
numList = []                # Create empty list now to store all the numbers that will be entered

for x in range(0,firstNum):   # Using the first number entered, get input until range reached
    number = int(input())       # Get the numbers via input
    numList.append(number)       # append each entered number to the empty list created at start
    
SmallestNum = min(numList)

for i in range(0,firstNum):
    numList[i] = numList[i] - SmallestNum
    print(numList[i])
    