# Implementation of simple exception handling

try:
    with open("aFileThatDoesNotExist.txt", "r") as fileToRead:
        print(fileToRead.read())
except FileNotFoundError:
    print("The file you are trying to read does not exist.")
finally:
    print("This prints always")

