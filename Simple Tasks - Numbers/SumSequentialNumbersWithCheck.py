# Finding a sum of all sequential numbers up to chosen number (including that number)
# Write a function sum_to(n) that returns the sum of all integer numbers up to and including n. So sum_to(10) would be 1+2+3…+10 which would return the value 55.
# Added input validation

def sum_to(number):
  theSum = 0
  for i in range(number + 1):
    theSum += i
  return theSum


def checkIfInteger(someInput):
  try:
    someInput = int(someInput)
    return "OK"
  except ValueError:
    print("The value entered is not an integer number.")
    return "NotOK"


aCheck = "NotOK"

while aCheck == "NotOK":
  theNumber = input("Please enter an integer number: ")
  aCheck = checkIfInteger(theNumber)

theNumber = int(theNumber)

print("The sum of all numbers up to the number", theNumber, "is:",
      sum_to(theNumber))
