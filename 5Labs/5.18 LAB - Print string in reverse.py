###
# [PROG] :  Smallest and largest number in a list
# [LANG] :  Python
# [AUTH] :  BooeySays
# [DESC] :  Enter a bunch of numbers and the script will start
#           when a negative number is entered. After, it will
#           spit out the smallest and the largest number from
#           the list.
# [EDTR] :  PyCharm 2020.2.1
# [LAB#] :  5.18 LAB: Print string in reverse
###

x = input("")
y = x[::-1]
print(y)
a = input("")
while (a != "Quit") and (a != "quit") and (a != "q"):
    b = a[::-1]
    print(b)
    a = input("")



# FIRST ATTEMPT:    
#reversed_string = []
#string_input = input('')
#
#while (string_input != 'Quit') or (string_input != 'quit') or (string_input != 'q'):
#    reversed_string.append(string_input[::-1])
#    string_input = input('')
#
#for x in reversed_string:
#    print(x, end=' ')
