# ArrayAJigsaw - Find out if the array is a "jigsaw" so the 1st element is smaller than
# 2nd, 3rd smaller than 2nd and 4th, etc 

nrElements = int(input("Input the number of elements: "))

el = int(input("Input element #1: "))
previousEl = el
isJigsaw = True


for i in range (1,nrElements):
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