# In array of N elements find the biggest subset of repeating numbers, and 
# print what numbert it is, what is it's position and how big is the subset


import random

nrElements = 40

print("The number of elements in the array: ", nrElements)
print("\n")

print("The elements of the array are: ")
print("\n")

element = random.randint(1, 5) # Generates random integer 1 - 5 (inclusive)
previousEl = element

print("1: " + str(element))

theElement = element
theFinalElement = element

index1stElement = 1
theIndex1stElement = 1

biggestSize = 1
theBiggestSize = 1


for i in range (2,nrElements):
  previousEl = element
  element = random.randint(1, 5)
  print(str(i) + ": " + str(element))
  
  if element == previousEl:
    theElement = element
    biggestSize = biggestSize + 1
    index1stElement = i - biggestSize + 1
  else:
    biggestSize = 1

  if biggestSize >= theBiggestSize:
    theFinalElement = previousEl
    theBiggestSize = biggestSize
    theIndex1stElement = index1stElement

print("The biggest subset is having", theBiggestSize ,  "elements '" + 
      str(theFinalElement) + "' starting at the position" , theIndex1stElement)