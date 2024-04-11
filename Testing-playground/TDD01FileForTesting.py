# TDD, Test-Driven Development, file for testing the file in which the development work is done

import unittest
from TDD01FileForDevelopment import calculateSum # Import the funtion to be tested from the file in which the development is done

class TestSum(unittest.TestCase):
    def testListSum(self):
        dataList = [1, 2, 3]
        result = calculateSum(dataList)
        self.assertEqual(result, 6)

print("\n")
print("Message from the testing-file:")
unittest.main() # This runs the testing

