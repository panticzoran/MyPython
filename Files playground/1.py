
# Prints Hello World
print("Hello World")
print("2 + 3 = " + str(2+3))


# Calls the quadratic equation code
from quadratic_equation import solve_quadratic
answer = solve_quadratic(5, 6, 1)
print("x is " + str(answer))

# Calls the fractal code
from factorial import factorial
print("Factorial 5 = " + str(factorial(5)))


# Calls the file code and prints out a file
from working_with_files import readFile
contentsForPrinting = readFile("mydata.txt")
print (contentsForPrinting)

# Calls the file code and creates the file and puts content in it
from working_with_files import createFile
filename = "created_file.txt"
textForInput = "This is some data that our Python script created.\n"
createFile(filename, textForInput)
