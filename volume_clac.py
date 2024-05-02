# Programming Challenge: Volume of a Rectangular Prism

# For this programming challenge, you will be creating a function that calculates the volume of a rectangular prism in cubic feet.  The formula to find the volume of a rectangular prism is V = l * w * h where l, w, and h are length, width, and height, respectively.

# First, create three variables representing length, width, and height.   Assign each of them an integer as user input using the input() function and int().

# Next, create a function to calculate the volume of the rectangular prism.  It should have 3 parameters representing length, width, and height and return the volume of a rectangular prism calculated using those 3 parameters.

# Finally, use print() to display "The volume of the rectangular prism is [call function  here to calculate volume] cubic feet." in the output.  You will have to use str() on the function call to be able to concatenate it with strings since it returns an integer.


length = int(input("enter the length of prism: "))
width = int(input("enter the width of prism: "))
height = int(input("enter the height of prism: ")) 

def volume (l, w ,h):
    return(l * w * h)

print("the volume of the rectangular prism " + str(volume(length, width, height)) + " cubic feet.") 