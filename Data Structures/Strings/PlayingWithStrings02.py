# Playing with strings and formatting

import string

s = "Hello, how are you? I'm doing well, thank you."
print("The string is:")
print(s)
print("\n")

# Using the split method
print("The string splitted to words is:")
print(s.split())
print("\n")


# Using the string module "punctuation" (need to "import string" at the beginning)
# Removing the punctuation from a string
def removePunctuation(ss):
  newS = ""
  for eachChar in ss:
    if eachChar not in string.punctuation:
      newS += eachChar
  return newS


print("The string with the punctuation removed is:")
print(removePunctuation(s))
print("\n")

# Removing the punctuation and splitting into words
my_story = """
Pythons are constrictors, which means that they will 'squeeze' the life
out of their prey. They coil themselves around their prey and with
each breath the creature takes the snake will squeeze a little tighter
until they stop breathing completely. Once the heart stops the prey
is swallowed whole. The entire animal is digested in the snake's
stomach except for fur or feathers. What do you think happens to the fur,
feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
you guessed it --- snake POOP! """

print("The story is:")
print(my_story)
print("\n")

print("The story splitted to words and without the punctuation is:")
print(removePunctuation(my_story).split())
print("\n")

# Playing with formatting

name = "Alice"
age = 10
s2 = "I am {1} and I am {0} years old.".format(age, name)
print(s2)
print("\n")

n1 = 4
n2 = 5
s3 = "2**10 = {0} and {1} * {2} = {3:f}".format(2**10, n1, n2, n1 * n2)
print(s3)
print("\n")

n1 = "Paris"
n2 = "Whitney"
n3 = "Hilton"
print("Pi to three decimal places is {0:.3f}".format(3.1415926))
print("123456789 123456789 123456789 123456789 123456789 123456789")
print("|||{0:<15}|||{1:^15}|||{2:>15}|||Born in {3}|||".format(
    n1, n2, n3, 1981))
print("The decimal value {0} converts to hex value {0:x}".format(123456))
print("\n")
