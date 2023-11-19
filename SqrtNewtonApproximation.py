# Approximating the square root

import math

def squareRoot(number):
	approximation = number / 2.0
	nrOfIterations = 1
	while True:
		betterApproximation = (approximation + number/approximation) / 2.0
		if abs(approximation - betterApproximation) < 0.0000001:
			print(nrOfIterations, end=": ")
			return betterApproximation
		nrOfIterations += 1
		approximation = betterApproximation


# Testing
print(math.sqrt(25.0), squareRoot(25.0))
print(math.sqrt(49.0), squareRoot(49.0))
print(math.sqrt(11.0), squareRoot(11.0))
print(math.sqrt(100.0), squareRoot(100.0))