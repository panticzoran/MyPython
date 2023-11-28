# Perfect number, a positive integer that is equal to the sum of its proper divisors
# The smallest perfect number is 6, which is the sum of 1, 2, and 3. 
# Other perfect numbers are 28, 496, and 8128.

def isProperDivisor(nr , divisor):
  ''' Returns True if proper divisor, otherwise False'''
  return nr % divisor == 0

def isPerfect(nr):
  '''Returns True if perfect number, otherwise False'''
  sumDivisors = 1
  for i in range (2, nr):
    if isProperDivisor(nr,i):
      sumDivisors += i
  return sumDivisors == nr    


checkUntil = 100000 # Check for perfect numbers from 1 to checkUntil

for i in range(2, checkUntil):
  if isPerfect(i):
    print("The number", i , " is perfect number")