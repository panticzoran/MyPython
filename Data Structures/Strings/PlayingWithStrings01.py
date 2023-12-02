# Playing with strings

aString = "Hello, dear World!"

print("The string is: ", aString)
print("Upper version of the string: ", aString.upper())
print("Lower version of the string: ", aString.lower())
print("SwapCase version of the string: ", aString.swapcase())
print("Capitalize version of the string: ", (aString.lower()).capitalize())

print("\n")

enumeratedString = list(enumerate(aString)) # Visualising the indices
print(enumeratedString)
print("\n")

print("Printing the string")
for i in range(len(enumeratedString)):
	print(str(i+1) + ". element is", enumeratedString[i])
print("\n")

print("Printing the reversed string")
for j in range(len(enumeratedString)-1, -1, -1):
	print(str(j) + ". element is", enumeratedString[j])
print("\n")

def findIndexOfCharInString(string, character):
	"""Finds the index of the character in the string"""
	for i in range(len(string)):
		if string[i] == character:
			return i
	return -1

print(findIndexOfCharInString("Compsci", "p"))
print(findIndexOfCharInString("Compsci", "C"))
print(findIndexOfCharInString("Compsci", "c"))
print(findIndexOfCharInString("Compsci", "x"))