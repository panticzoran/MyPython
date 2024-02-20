# Calculating the product of all numbers in a list

def calculateProduct(number_list):

    multipliedNumber = 1
    for item in number_list:
        multipliedNumber *= item

    return multipliedNumber


print(calculateProduct([1,2,3,4]))

print("\n")

print(calculateProduct([2,4,6,23,34]))

print("\n")

