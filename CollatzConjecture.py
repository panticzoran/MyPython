# the Collatz conjecture, also known as the 3n + 1 conjecture

def collatzConjecture(number):
	
	""" Start from some given n, and to generate the next term of the sequence from n, either by halving n, (whenever n is even), or else by multiplying it by three and adding 1. The sequence terminates when n reaches 1."""

	while number != 1:
		print(number, end=", ")
		if number % 2 == 0:
			number = number //2
		else:
			number = number * 3 + 1
	print(number, end=".\n")

# Testing a range of numbers
for i in range(20):
	print("For number", i+1, end=": ")
	collatzConjecture(i+1)