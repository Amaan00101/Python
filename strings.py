# Strings Exercises
# Do all of this in a .py file



# Create a variable and assign it the string "Just do it!"
var = "just do it!"

# Access the "!" from the variable by index and print() it
print(var[10])

# Print the slice "do" from the variable
print(var[5:7])

# Get and print the slice "it!" from the variable
print(var[8:])

# Print the slice "Just" from the variable
print(var[:4])

# Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.
slice = (var[5:])
concatenate = "Don't" + " " + (slice)
print(concatenate)