###
# [PROG] :  Smallest and largest number in a list
# [LANG] :  Python
# [AUTH] :  BooeySays
# [DESC] :  Enter a bunch of numbers and the script will start
#           when a negative number is entered. After, it will
#           spit out the smallest and the largest number from
#           the list.
# [EDTR] :  PyCharm 2020.2.1
# [LAB#] :  5.24 LAB: Warm up: Drawing a right triangle
###

###
# Saved in pycharm under: /labs/5.24.1/
###

a = 0                                               # count
char = input('Enter a character:\n')                # get char
height = int(input('Enter triangle height:\n'))     # get height
for a in range(height + 1):                         # prints point
  print("%s " % char * a)