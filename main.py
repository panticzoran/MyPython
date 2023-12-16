# Calculating addition "manually"


def addLeadingZeroes(numberStr, sizeNrStr):
  """Adds number of leading zeroes to a number represented as string"""
  lenNumberStr = len(numberStr)
  newNumberStr = ""
  for _i in range(sizeNrStr - lenNumberStr):
    newNumberStr += "0"
  newNumberStr += numberStr
  return newNumberStr


def sumTwoNumbers(number1Str, number2Str):
  """Returns sum of two numbers, all represented as strings"""

  lenNr1 = len(number1Str)
  lenNr2 = len(number2Str)

  if lenNr2 > lenNr1:
    number1Str = addLeadingZeroes(number1Str, lenNr2)
  elif lenNr2 < lenNr1:
    number2Str = addLeadingZeroes(number2Str, lenNr1)
    lenNr2 = lenNr1

  sumNumberStr = ""
  overflowNr = 0
  sumDigitStr = ""

  for i in reversed(range(lenNr2)):
    sumDigitStr = str(int(number1Str[i]) + int(number2Str[i]) + int(overflowNr))
    if len(sumDigitStr) == 1:
      sumNumberStr = sumDigitStr + sumNumberStr
      overflowNr = 0
    else:
      sumNumberStr = sumDigitStr[1] + sumNumberStr
      overflowNr = int(sumDigitStr[0])
  
  if overflowNr != 0:
    sumNumberStr = str(overflowNr) + sumNumberStr

  return sumNumberStr


# Inputs two number as strings, and calls the function for make the sum

number1AsStr = input("Enter the 1st number:  ")
number2AsStr = input("Enter the 2nd number:  ")

number1Prt = number1AsStr
number2Prt = number2AsStr

summa = sumTwoNumbers(number1AsStr, number2AsStr)
lenSumma = len(summa)

print("\n")
print("{0:>{width}}".format(number1Prt, width=lenSumma + 1))
print("+" + "{0:>{width}}".format(number2Prt, width=lenSumma))
print((lenSumma + 1) * "=")
print("{0:>{width}}".format(summa, width=lenSumma + 1))