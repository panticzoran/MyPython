from os import remove
import string

# Count letters in a string


def countLetters(aString, aLetter):
  nrOccurences = 0
  for i in range(len(aString)):
    if aString[i] == aLetter:
      nrOccurences += 1
  return nrOccurences


someString = input("Please enter the string to be searched:")
someLetter = input("Please enter the letter to be counted:")
print("The letter '", someLetter, "' appears",
      countLetters(someString, someLetter), "times in the string '",
      someString, "'")
print("\n")

# Count the number of words in a text containing a specific letter


def stringToWords(aString):
  return aString.split()


def removePunctuation(aString):
  for i in range(len(aString)):
    if aString[i] in string.punctuation:
      aString = aString.replace(aString[i], " ")
  return aString


def countWordsHavingLetter(aListOfWords, theLetter):
  count = 0
  for word in aListOfWords:
    if theLetter in word:
      count += 1
  return count


letterInWord = "e"
my_story = """
Pythons are constrictors, which means that they will 'squeeze' the life
out of their prey. They coil themselves around their prey and with
each breath the creature takes the snake will squeeze a little tighter
until they stop breathing completely. Once the heart stops the prey
is swallowed whole. The entire animal is digested in the snake's
stomach except for fur or feathers. What do you think happens to the fur,
feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
you guessed it --- snake POOP! """

my_story_2 = """
Python has very simple syntaxes. Python as a language is beginner friendly. A programmer who is new to this field may get afraid of programming due to all these complex syntaxes in languages like C and Java. But Python also brings some complexities with its short and simple syntaxes. One of these issues is printing brackets.

In this article, we’re going to check how we can print brackets in Python.

What do brackets signify in Python?
Brackets in almost all programming languages are metacharacters. That means they are used to specify something. In Python, we use indentation instead of curly braces, but curly braces are still used just not for indentation. They are used for denoting a set or a dictionary. Square brackets are used to denote a list or used for indexing in indexed iterables like lists and tuples. Parenthesis is used to specify the order of operations and in calling a function or creating an instance of a class, or it denotes a tuple.

Printing Parentheses
Parentheses are “()”. They are used to call a function or create a tuple. The print function itself uses parenthesis. Let’s see how you can print parentheses.
"""

# First removing the punctuation (puting spaces instead)
my_story = removePunctuation(my_story)

# Second, splitting the string without punctuation to words
wordsList = stringToWords(my_story)

# Third, counting the number of words in the string that contain the letter "e"
theNumber = countWordsHavingLetter(wordsList, letterInWord)

print(
    "Your text contains {0} words, of which {1} ({2:.2f}%) contain an '{3}'.".
    format(len(wordsList), theNumber, 100 * theNumber / len(wordsList),
           letterInWord))

# First removing the punctuation (puting spaces instead)
my_story_2 = removePunctuation(my_story_2)

# Second, splitting the string without punctuation to words
wordsList = stringToWords(my_story_2)

# Third, counting the number of words in the string that contain the letter "e"
theNumber = countWordsHavingLetter(wordsList, letterInWord)

print(
    "Your text contains {0} words, of which {1} ({2:.2f}%) contain an '{3}'.".
    format(len(wordsList), theNumber, 100 * theNumber / len(wordsList),
           letterInWord))
