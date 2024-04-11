# TDD, Test-Driven Development, file where the development work is done

def calculateSum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print("Message from the development-file:")
print("The sum of 1, 2 and 3 is", calculateSum([1, 2, 3]))