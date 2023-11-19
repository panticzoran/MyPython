import sys

def unitTest(didItPass):
	"""  Print the result of a test.   """
	lineNum = sys._getframe(1).f_lineno    # Get the caller's line number
	if didItPass:
		msg = "Test at line {0} ok.".format(lineNum)
	else:
		msg = "Test at line {0} FAILED".format(lineNum)
	print(msg)

def testSuite():
	""" Run the suite of tests for code in this module / this file"""
	unitTest(absoluteValue(17) == 17)
	unitTest(absoluteValue(-17) == 17)
	unitTest(absoluteValue(0) == 0)
	unitTest(absoluteValue(3.14) == 3.14)
	unitTest(absoluteValue(-3.14) == 3.14)

def absoluteValue(x):   # Function to be tested
	if x < 0:
		return -x
	elif x >= 0:
		return x

testSuite()    # The call to run the tests
