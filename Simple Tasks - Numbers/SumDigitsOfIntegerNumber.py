# Finding a sum of digits for an integer

theNumber = int(input ("Please enter an integer: "))

stringOfTheNumber = str(theNumber)
digitsInTheNumber = len(stringOfTheNumber)
sumOfDigits = 0
numOfIterations = digitsInTheNumber
operatingOnTheNumber = theNumber

while numOfIterations > 0:
	sumOfDigits = sumOfDigits + operatingOnTheNumber%10
	operatingOnTheNumber = operatingOnTheNumber//10
	numOfIterations -= 1

print ("Sum of digits for the number: " , theNumber , " is: ", sumOfDigits)

