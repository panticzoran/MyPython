# Implementation simple Binary Search

def binarySearch(sortedList, targetToFind):
    leftElementIndex = 0
    rightElementIndex = len(sortedList) - 1

    while leftElementIndex <= rightElementIndex:
        middleElementIndex = (leftElementIndex + rightElementIndex) // 2
        middleElement = sortedList[middleElementIndex]

        if middleElement == targetToFind:
            return middleElementIndex  # Target found, return its index
        elif middleElement < targetToFind:
            leftElementIndex = middleElementIndex + 1  # Search in the right half
        else:
            rightElementIndex = middleElementIndex - 1  # Search in the left half

    return -1  # Target not found

# Example usage:
sortedList = [2, 3, 5, 8, 10, 30, 35, 40]
targetToFind = 35

print("Index of element", targetToFind, " is ", binarySearch(sortedList, targetToFind))


