# Programming Challenge: Find The Number of Characters in A String
# In a .py file, write a program which calculates the number of characters in a string.

# The string should be entered using input() and assigned to a variable. 

# Use print() twice at the end of your program.  The first print() will print the string that the user entered and the second print() will display the number of characters in the string.  For example, if the user entered the string "hello world", the number of characters would be 11.


ent = str(input("Pls enter a string: "))
count = 0
for char in ent:
    count += 1

print("user input string is: " + ent)
print("the num of characters are: " + str(count))