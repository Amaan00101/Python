# Programming Challenge: Factorial
# Create a function which takes one positive integer as its input and returns its factorial.

# To make sure that your function works correctly, you should call it with the inputs 3, 4, and 5 and print what is returned by those calls.  For those inputs, you should get 6, 24, and 120, respectively.

# num = int(input("Pls enter a number: "))
# fact = 1

# for number in range(num, 0, -1):
#     fact *= number
# print(fact)


def factorial(number):
    fact = 1
    for num in range(number, 1, -1):
        fact *= num
    return fact

print(factorial(3))
print(factorial(4))
print(factorial(5))