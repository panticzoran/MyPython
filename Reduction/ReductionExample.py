# Reduction example

def addition(x, y): # Function for addition
    return x + y

def subtraction(x, y): # Function for subtraction
    return x - y

def reduction(aFunction, aList, theNumber = 0): # performs a function on a list
    result = theNumber
    for num in aList:
        result = aFunction(result, num)
    return result

print("Sum of [1,2,3,4] =", reduction(addition, [1,2,3,4]))

totalSumOfList = reduction(addition,[12,11,10])
print("Sum of [12,11,10] =", totalSumOfList)

print("Difference 100 - [50,25,15] =", reduction(subtraction, [50,25,15], 100))