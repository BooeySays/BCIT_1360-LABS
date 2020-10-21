###
# [PROG] :  Smallest and largest number in a list
# [LANG] :  Python
# [AUTH] :  BooeySays
# [DESC] :  Enter a bunch of numbers and the script will start
#           when a negative number is entered. After, it will
#           spit out the smallest and the largest number from
#           the list.
# [EDTR] :  PyCharm 2020.2.1
# [LAB#] :  5.25.1: LAB*: Program: Drawing a half arrow
###
###
# Saved in pycharm under Labs/5.23.1/
###
arrowBaseHeight = int(input('Enter arrow base height:\n'))
arrowBaseWidth = int(input('Enter arrow base width:\n'))
arrowHeadWidth = int(input('Enter arrow head width:\n'))

while arrowHeadWidth <= arrowBaseWidth:
    arrowHeadWidth = int(input('Enter arrow head width:\n'))
print("\n".rstrip("\n"))

for a in range(arrowBaseHeight):
    a = '*' * arrowBaseWidth
    print(a)
for b in range(arrowHeadWidth):
    b = '*' * arrowHeadWidth
    print(b)
    arrowHeadWidth -= 1
    
# Note: You have to choose a larger number for Arrow Head Width than Arrow Base Width.
#       It will just keep asking you over and over until you enter a larger number.
#       Why? Cause you can't draw it with those dimensions