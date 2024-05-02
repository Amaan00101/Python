# Programming Challenge: Roman Numeral Equivalent
# For this exercise, start by creating a variable and assigning it a randomly generated integer between and inclusive of both 1 and 10.

# Then, using your knowledge of if, elif, and else statements, create a program which prints the roman numeral equivalent of the randomly generated number.

# For example, if the randomly generated integer was 9, then the program would say that the roman numeral equivalent of 9 is IX in the output.


from random import randint
num = (randint(1,10))

if num == 1:
    print("the roman numeral equivalent of " + str(num) + " is I")
elif num == 2:
    print("the roman numeral equivalent of " + str(num) + " is II")
elif num == 3:
    print("the roman numeral equivalent of " + str(num) + " is III")
elif num == 4:
    print("the roman numeral equivalent of " + str(num) + " is IV")
elif num == 5:
    print("the roman numeral equivalent of " + str(num) + " is V")
elif num == 6:
    print("the roman numeral equivalent of " + str(num) + " is VI")
elif num == 7:
    print("the roman numeral equivalent of " + str(num) + " is VII")
elif num == 8:
    print("the roman numeral equivalent of " + str(num) + " is VIII")
elif num == 9:
    print("the roman numeral equivalent of " + str(num) + " is IX")
else:
    print("the roman numeral equivalent of " + str(num) + " is X")
