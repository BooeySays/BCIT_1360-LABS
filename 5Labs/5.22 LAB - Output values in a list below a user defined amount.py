###
# [PROG] :  Smallest and largest number in a list
# [LANG] :  Python
# [AUTH] :  BooeySays
# [DESC] :  Enter a bunch of numbers and the script will start
#           when a negative number is entered. After, it will
#           spit out the smallest and the largest number from
#           the list.
# [EDTR] :  PyCharm 2020.2.1
# [LAB#] :  5.22 LAB: Output values in a list below a user defined amount
###

firstNum = int(input())             # enter the first number that will tell the script how many numbers it will be working with
myList = []                         # Empty list for now

for i in range(firstNum):           # counting down the first number entered
    myList.append(int(input()))     # appending each input into list
lastNum = int(input())              # After entering all the numbers from firstNum, enter the last number which will be used the max num
for x in myList:                    # compare each number in list
    if x < lastNum:                 # if the number is less than the last number,
        print(x)                    # print it