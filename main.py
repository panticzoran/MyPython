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





for i in range (1,nrElements):
  previousEl = el
  el = int(input("Input element #" + str(i+1) + ": "))
  if i % 2 == 0 and previousEl < el:
    isJigsaw = False
    break
  if i % 2 != 0 and previousEl > el:
    isJigsaw = False
    break

if isJigsaw:
  print("The array is a jigsaw.")
else:
  print("The array is not a jigsaw.")