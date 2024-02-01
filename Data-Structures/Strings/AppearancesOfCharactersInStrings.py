# Count the number of appearances of a character in a string


def countAppearances(text, character):
  """Counts the number of appearances of a character in a string"""
  countAppearances = 0
  for i in range(len(text)):
    if text[i] == character:
      countAppearances += 1
  return countAppearances


# Testing the above function

textInput = input("Please enter the string to be searched ")
charInput = input("Please enter the character to be searched for ")
print("The number of appearances of the character '", charInput,
      "' in the string ", textInput, "' is ",
      countAppearances(textInput, charInput))


def indexOfAppearance(text, character, fromIndex=0):
  """Returns the index of the first appearance of a character in a string""" ""
  ix = fromIndex
  while ix < len(text):
    if text[ix] == character:
      return ix
    ix += 1
  return -1


# Testing the above function
textInput = input("Please enter the string to be searched ")
charInput = input("Please enter the character to be searched for ")
fromIndex = 0
print("The character '",
      charInput,
      "' appears in the string'",
      textInput,
      "' on the folowing places",
      end=": ")
isDone = indexOfAppearance(textInput, charInput, fromIndex)
while isDone != -1:
  print(isDone, end=", ")
  fromIndex = isDone + 1
  isDone = indexOfAppearance(textInput, charInput, fromIndex)
