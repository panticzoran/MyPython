# the Collatz conjecture, also known as the 3n + 1 conjecture


def collatzConjectureNrSteps(number):
  """ Counts the number of steps """
  nrSteps = 0
  while number != 1:
    if number % 2 == 0:
      number = number // 2
    else:
      number = number * 3 + 1
    nrSteps += 1
  return nrSteps


def collatzConjecture(number):
  """ Prints the steps """

  while number != 1:
    print(number, end=", ")
    if number % 2 == 0:
      number = number // 2
    else:
      number = number * 3 + 1
  print(number, end=".\n")


# Testing a range of numbers
currentMaxSteps = 0
for i in range(500000):
  currentNrSteps = collatzConjectureNrSteps(i + 1)
  if currentMaxSteps < currentNrSteps:
    currentMaxSteps = currentNrSteps
    currentNumber = i + 1
    print("Maximal number of steps is ", currentMaxSteps, " for the number ",
          currentNumber)

print("For the number", currentNumber, end=": ")
collatzConjecture(currentNumber)
