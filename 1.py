

print("Hello World")
print("2 + 3 = " + str(2+3))

from quadratic_equation import solve_quadratic
answer = solve_quadratic(5, 6, 1)
print("x is " + str(answer))

from factorial import factorial
print("Factorial 5 = " + str(factorial(5)))

from working_with_files import readFile
contentsForPrinting = readFile("mydata.txt")
print (contentsForPrinting)

from working_with_files import createFile
filename = "created_file.txt"
textForInput = "This is some data that our Python script created.\n"
createFile(filename, textForInput)
