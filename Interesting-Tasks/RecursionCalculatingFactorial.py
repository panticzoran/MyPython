# Recursive function that calculates the factorial of a number

# The key components of recursion are the base case and the recursive case. 
# The base case is the condition under which the recursion stops, while the
# recursive case is where the function calls itself with modified parameters,
# moving towards the base case.

def factorial(n):
    # Base case: if n is 0, the factorial is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

# Examples

print("5! = " + str(factorial(5)))  # Prints 120, because 5! = 5*4*3*2*1 = 120
print("\n")
print("6! = " + str(factorial(6)))  # Prints 720, because 6! = 6*5*4*3*2*1 = 120