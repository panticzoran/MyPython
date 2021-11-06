# Opens the designated file, reads it, and returns the content of the file
def readfile(fileToOpen):
	f = open(fileToOpen)
	contents = f.read()
	f.close()
	return contents