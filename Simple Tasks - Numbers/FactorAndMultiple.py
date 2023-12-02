import sys

def unitTest(didItPass):
	"""  Print the result of a test.   """
	lineNum = sys._getframe(1).f_lineno    # Get the caller's line number
	if didItPass:
		msg = "Test at line {0} ok.".format(lineNum)
	else:
		msg = "Test at line {0} FAILED".format(lineNum)
	print(msg)

def testSuiteIsFactor():
	""" Run the suite of tests for code in this module / this file"""
	unitTest(isFactor(3, 12))
	unitTest(not isFactor(5, 12))
	unitTest(isFactor(7, 14))
	unitTest(not isFactor(7, 15))
	unitTest(isFactor(1, 15))
	unitTest(isFactor(15, 15))
	unitTest(not isFactor(25, 15))


def testSuiteIsMultiple():
	""" Run the suite of tests for code in this module / this file"""
	unitTest(isMultiple(12, 3))
	unitTest(isMultiple(12, 4))
	unitTest(not isMultiple(12, 5))
	unitTest(isMultiple(12, 6))
	unitTest(not isMultiple(12, 7))



def isFactor(f, n):
	if n%f == 0:
		return True
	else:
		return False

	
def isMultiple(n, m):
	return isFactor(m, n)


print("Testing the IsFactor")
testSuiteIsFactor()    # The call to run the tests

print("Testing the IsMultiple")
testSuiteIsMultiple()    # The call to run the tests
