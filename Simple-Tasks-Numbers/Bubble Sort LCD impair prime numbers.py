# Bubble sort
# =====================================================


def bubbleSortArray(arrayToBeSorted, ascending=True):
  """ Sorting the array ascending or descending"""
  if ascending:
    for i in range(len(arrayToBeSorted)):
      for j in range((len(arrayToBeSorted) - i - 1)):
        if arrayToBeSorted[j] > arrayToBeSorted[j + 1]:
          t = arrayToBeSorted[j + 1]
          arrayToBeSorted[j + 1] = arrayToBeSorted[j]
          arrayToBeSorted[j] = t
  else:
    for i in range(len(arrayToBeSorted)):
      for j in range((len(arrayToBeSorted) - i - 1)):
        if arrayToBeSorted[j] < arrayToBeSorted[j + 1]:
          t = arrayToBeSorted[j + 1]
          arrayToBeSorted[j + 1] = arrayToBeSorted[j]
          arrayToBeSorted[j] = t
  return arrayToBeSorted


print("Sorting an array")
print("-------------------------------------------")

# Input the array to be sorted
import random

howMany = int(input("How many elements the array to be sorted should have: "))

# Populate the array with random numbers
arrayToSort = []
for ix in range(howMany):
  element = random.randint(0, 100)
  arrayToSort.append(element)

# Printing the arrays
print("The array to be sorted is: ", arrayToSort)
print("The ascending-sorted array is: ", bubbleSortArray(arrayToSort, True))
print("The descending-sorted array is: ", bubbleSortArray(arrayToSort, False))
print("\n")

# Lowest common denominator
# =====================================================


def lowestCommonDenominator(a, b):
  """ Function to find the lowest common denominator of two numbers"""
  while True:
    if a == b:
      return a
    elif a > b:
      a = a - b
    else:
      b = b - a
  return a


print("Finding the Lowest Common Denominator for 2 numbers")
print("---------------------------------------------------")

# Input the numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Print the result
print("The lowest common denominator of", a, "and", b, "is",
      lowestCommonDenominator(a, b))
print("\n")

# Find the average of all impair numbers until the number n
# ==========================================================


def isNrImpair(number):
  """ Function to check if a number is odd or not"""
  if number % 2 == 0:
    return False
  else:
    return True


def averageOfAllImpairNumbers(n):
  """ Function to find the average of all impair numbers until the number n"""
  sum = 0
  counter = 0
  for i in range(1, n + 1):
    if isNrImpair(i):
      sum += i
      counter += 1
  return sum / counter


print("Finding the average of all impair numbers until the number n")
print("------------------------------------------------------------")

number = int(input("Enter the number: "))
print("The average of all impair numbers from 1 to", number, "is",
      averageOfAllImpairNumbers(number))
print("\n")

# Find the sum of all prime numbers until the number n
# ==========================================================


def isPrime(number):
  """ Function to check if a number is prime or not"""
  if number == 1:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True


def sumOfAllPrimeNumbers(n):
  """ Function to find the sum of all prime numbers until the number n"""
  sum = 0
  for i in range(1, n + 1):
    if isPrime(i):
      sum += i
  return sum


print("Finding the sum of all prime numbers until the number n")
print("------------------------------------------------------------")

number = int(input("Enter the number: "))
print("The sum of all prime numbers from 1 to", number, "is",
      sumOfAllPrimeNumbers(number))
print("\n")
