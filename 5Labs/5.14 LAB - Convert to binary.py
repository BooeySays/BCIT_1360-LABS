###
# [PROG] :  Smallest and largest number in a list
# [LANG] :  Python
# [AUTH] :  BooeySays
# [DESC] :  Enter a bunch of numbers and the script will start
#           when a negative number is entered. After, it will
#           spit out the smallest and the largest number from
#           the list.
# [EDTR] :  PyCharm 2020.2.1
# [LAB#] :  5.21 LAB: Smallest and largest numbers in a list
###

numList = []                # Create empty list
while True:
    num = int(input())
    if num > 0:
        numList.append(num)
    else:
        break

sml = numList[0]
lrg = numList[0]
for num in numList:
    if num < sml:
        sml = num
    if num > lrg:
        lrg = num
print(sml, lrg)