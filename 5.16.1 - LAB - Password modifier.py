###
# [PROG] :  Smallest and largest number in a list
# [LANG] :  Python
# [AUTH] :  BooeySays
# [DESC] :  Enter a bunch of numbers and the script will start
#           when a negative number is entered. After, it will
#           spit out the smallest and the largest number from
#           the list.
# [EDTR] :  PyCharm 2020.2.1
# [LAB#] :  5.16 LAB: Password modifier
###

word = input()
password = ""

for x in word:
    if (x == 'i'):
        password += "!"
    elif (x == 'a'):
        password += '@'
    elif (x == 'm'):
        password += 'M'
    elif (x == 'B'):
        password += '8'
    elif (x == 'o'):
        password += '.'
    else:
        password += x
password += 'q*s'
        
print(password)
