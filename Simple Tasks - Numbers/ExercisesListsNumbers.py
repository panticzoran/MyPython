# Different exercises with lists, triangular and prime numbers, etc

# List used for exercises
listOfNumbers = [3, 7, 9, 11, 10, 17, 2, 4, 2, -3, 8, -2, 9, -11, ]
listOfWords = ["I", "You", "We", "They", "Monday", "Wow", "san", "Terry", "extraterrestial", "Carne", "Equal", "Lala1", "sam", "Whatsoever", "Dish", "Roses"]


# Write a function to count how many odd numbers are in a list.
def countOdd(nrList):
	counter = 0
	for n in nrList:
		if n%2 != 0:
			counter += 1
	return counter

print("There are", countOdd(listOfNumbers), "odd numbers in this list of numbers: ", listOfNumbers, "\n")


# Sum up all the even numbers in a list.

def sumEven(nrList):
	sum = 0
	for n in nrList:
		if n%2 == 0:
			sum += n
	return sum

print("The sum of all even numbers", listOfNumbers, "is", sumEven(listOfNumbers), "\n")


# Sum up all the negative numbers in a list.

def sumNeg(nrList):
	sum = 0
	for n in nrList:
		if n < 0:
			sum += n
	return sum

print("The sum of negative numbers", listOfNumbers, "is", sumNeg(listOfNumbers), "\n")


# Count how many words in a list have length 5.

def countWords(wordList):
	counter = 0
	for i in wordList:
		if len(i) == 5:
			counter += 1
	return counter

print("There are", countWords(listOfWords), "words in the word list: ", listOfWords, "that have 5 letters \n")


# Sum all the elements in a list up to but not including the first even number.

def sumUpTo1stEven(nrList):
	sum = 0
	for n in nrList:
		if n%2 == 0:
			break
		sum += n
	return sum

print("The sum of all numbers up to (and excluding) the first even number", listOfNumbers, "is", sumUpTo1stEven(listOfNumbers), "\n")


# Count how many words occur in a list up to and including the first occurrence of the word “sam”.

def countWordsUpToWord(wordList):
	counter = 0
	exists = False
	for i in wordList:
		if i != "sam":
			counter += 1
		elif i == "sam":
			counter += 1
			exists = True
			break
	if exists:
		return counter
	else:
		return -1

result = countWordsUpToWord(listOfWords)
if result == -1:
	print("There is no word 'sam' in the word list: ", listOfWords)
else:
	print("There are", result, "words in the word list: ", listOfWords, "up to (and including) the word ""'sam'"" \n")


# Write a function print_triangular_numbers(n) that prints out the first n triangular numbers.

def printTriangular(number):
	for i in range(1, number+1):
		print(i, int((i*i + i)/2))

printTriangular(10)
print("\n")

# Test if a number is prime


def isPrime(number):
	isItPrime = True
	for i in range(2, number):
		if number%i == 0:
			isItPrime = False
			break
	return isItPrime

print("The number 11 is prime:", isPrime(11))
print("The number 12 is prime:", isPrime(12))
print("The number 23 is prime:", isPrime(23))
print("The number 29 is prime:", isPrime(29))
print("The number 104 is prime:", isPrime(104))
print("\n")

# Write a function num_even_digits(n) that counts the number of even digits in n.

def nrIsEven(number):
	if number%2 == 0:
		return True
	return False

def countEvenDigits(number):
	counter = 0
	for i in range(len(str(number))):
		digit = number%10
		if nrIsEven(digit):
			counter += 1
		number = number // 10
	return counter

testCases1 = [434523, 46756, 923534, 1002, 1234, 7456456, 1111, 222, 4444, 666666, 787878]
for i in testCases1:
	print("Number", i, "has", countEvenDigits(i), " even digits.")
print("\n")

import random
generator = random.Random()
nrOfRndNrs = generator.randrange(1, 31) # generate random number between 1 and 30
testcases2 = []
print("I will generate", nrOfRndNrs, "random numbers, and count even digits in each of them:")
for i in range(nrOfRndNrs):
	testcases2.append(generator.randrange(2, 9999999999))
for i in testcases2:
	print("Number", i, "has", countEvenDigits(i), " even digits.")
print("\n")