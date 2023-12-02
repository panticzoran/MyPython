# FindPositionOf1stLastMaxElements
# Find the biggest element in an array, and the positions of the first 
# and the last elements

nrElements = int(input("Input the number of elements: "))

el = int(input("Input element #1: "))
max = el
pos1st = 1
posLast = 1

for i in range (1,nrElements):
  el = int(input("Input element #" + str(i+1) + ": "))
  if el > max:
    max = el
    pos1st = i + 1
  if el == max:
    posLast = i + 1
    

print("The max number is ", max, " and it's first occurence is ", pos1st , " and it's last occurence is ", posLast , ".")