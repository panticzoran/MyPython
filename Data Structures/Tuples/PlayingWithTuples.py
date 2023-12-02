# Playing with tuples


# We can pass tuples as arguments
def testTuple(aTuple):
	(aString, bString, cInteger) = aTuple
	print("Tuple: ", aTuple)
	print("Reorganised text: \n", aString, cInteger, bString)

exampleTuple = ("It is possile to pass tuples as arguments. Here is an integer:", " and the rest of the text.", 12)
testTuple(exampleTuple)

