# string methods 2 exercises

# Create a variable called the_string and assign it the string "North Dakota".
the_stirng = "North Dakota"

# Call .rjust() on the_string with 17 as its argument and print() the result.
print(the_stirng.rjust(17))

# Call .ljust() on the_string with the arguments 17 and "*" then print() the result.
print(the_stirng.ljust(17, "*"))

# Create a variable called center_plus and assign it the result of .center() being called on the_string with 16 and "+" as arguments.
# Use print() to display the string assigned to center_plus.
center_plus = the_stirng.center(16, "+")
print(center_plus)

# Call .lstrip() on the_string to remove "North" then print() the result.
print(the_stirng.lstrip("North"))

# Call .rstrip() on center_plus with "+" as its argument and print() the result.
print(center_plus.rstrip("+"))

# Call .strip() on center_plus with "+" as its argument and print() the result.
print(center_plus.strip("+"))

# Call .replace() on the_string and replace "North" with "South".  print() the result.
print(the_stirng.replace("North", "South"))