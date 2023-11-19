

lineOfText = input("Please enter the sequences delimited by space:").split()
print("The type of the input variable is:", type(lineOfText))
print("The input variable has ", len(lineOfText), " elements.")

print("Here are the sequences: ")
for i in range(len(lineOfText)):
	print(lineOfText[i])
