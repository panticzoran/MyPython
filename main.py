

print("Hello World")
print("2 + 3 = " + str(2+3))

from quadratic_equation import solve_quadratic
answer = solve_quadratic(5, 6, 1)
print("x is " + str(answer))

from factorial import factorial
print("Factorial 5 = " + str(factorial(5)))

from working_with_files import readfile
contentsforprinting = readfile("mydata.txt")
print (contentsforprinting)

