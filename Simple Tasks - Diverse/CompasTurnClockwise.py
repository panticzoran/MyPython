import sys


def unitTest(didItPass):
  """  Print the result of a test.   """
  lineNum = sys._getframe(1).f_lineno  # Get the caller's line number
  if didItPass:
    msg = "Test at line {0} ok.".format(lineNum)
  else:
    msg = "Test at line {0} FAILED".format(lineNum)
  print(msg)


def testSuite():
  """ Run the suite of tests for code in this module / this file"""
  unitTest(turnClockwise("N") == "E")
  unitTest(turnClockwise("W") == "N")
  unitTest(turnClockwise(42) == None)
  unitTest(turnClockwise("rubbish") == None)


def turnClockwise(pointer):
  if pointer == "N":
    return "E"
  if pointer == "E":
    return "S"
  if pointer == "S":
    return "W"
  if pointer == "W":
    return "N"
  return None


testSuite()  # The call to run the tests
