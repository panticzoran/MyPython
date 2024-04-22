# Example of First-Class Functions, creating a function that accepts another function as
# an argument and a list, applying the function to each element in the list

def applyFunction(functionToApply, listToBeAppliedTo):
  return [functionToApply(item) for item in listToBeAppliedTo]

# Applying lambda function for square of a number
listOfNumbers = [1, 2, 3, 4]
result = applyFunction(lambda x: x*x, listOfNumbers)

print ("The list is: ", listOfNumbers , "\n")

print("The squared list is: ", result)