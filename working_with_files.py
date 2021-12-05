# Opens the designated file, reads it, and returns the content of the file

# Reads the file and returns it's content
def readFile(fileToOpen):
	f = open(fileToOpen)
	contents = f.read()
	f.close()
	return contents

# Creates the file, and writes the text in it
def createFile(fileToCreate, textToWrite):
	f = open(fileToCreate, "w")
	f.write(textToWrite)
	f.close()
	return