import string

# function that reverses its string argument, and satisfies these tests:


def reverseString(aString):
  return aString[::-1]


print(reverseString("Hello World!"))
print("\n")

# Mirroring the string

bString = "Hello World!"
print(bString + reverseString(bString))
print("\n")

# Check if a string is palindrome


def isPalindrome(aString):
  return aString == reverseString(aString)


def removeWhitespace(aString):
  return aString.replace(" ", "")


print(isPalindrome("Hello World!"))
print("\n")

print(isPalindrome(removeWhitespace("ana voli milovana")))
print("\n")
