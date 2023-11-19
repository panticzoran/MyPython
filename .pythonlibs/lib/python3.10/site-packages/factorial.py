"""This is my first module to implement the factorial function"""
def factorial(n):
	if (n==1):
			return 1
	else:
			return n*factorial(n-1)