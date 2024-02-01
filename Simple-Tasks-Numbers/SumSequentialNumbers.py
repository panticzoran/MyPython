# Finding a sum of all sequential numbers up to chosen number (including that number)
# Write a function sum_to(n) that returns the sum of all integer numbers up to and including n. So sum_to(10) would be 1+2+3…+10 which would return the value 55.


def sum_to(number):
  theSum = 0
  for i in range(number + 1):
    theSum += i
  return theSum


theNumber = int(input("Please enter an integer number: "))
print("The sum of all numbers up to the number ", theNumber, " is: ",
      sum_to(theNumber))
