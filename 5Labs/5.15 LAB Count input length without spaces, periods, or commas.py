###
# [PROG] :  Smallest and largest number in a list
# [LANG] :  Python
# [AUTH] :  BooeySays
# [DESC] :  Enter a bunch of numbers and the script will start
#           when a negative number is entered. After, it will
#           spit out the smallest and the largest number from
#           the list.
# [EDTR] :  PyCharm 2020.2.1
# [LAB#] :  5.15 LAB: Count input length without spaces, periods, or commas
###

user_text = input()
text_length = len(user_text)
total = 0
non_char = 0

''' Type your code here. '''
num_spaces = int(user_text.count(" "))
num_periods = int(user_text.count('.'))
num_commas = int(user_text.count(','))

total = text_length - num_spaces - num_periods - num_commas
print(total)