# Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. It will return True if the triangle is right-angled, or False otherwise


def isRightAngled(x, y, z):
	sides = [x, y, z] #puts the triangle sides into a list
	sides.sort()      #sorts the list, so the largest value is at the end of the list (hypotenuse)
	if pow(sides[2],2) == (pow(sides[0],2) + pow(sides[1],2)): #checks if Pythagore's Theoreme condition is satisfied c**2 = a **2 + b**2
		return True
	else:
		return False


a = float(input("Please enter the first side of the triangle: "))
b = float(input("Please enter the second side of the triangle: "))
c = float(input("Please enter the third side of the triangle: "))
	
if isRightAngled(a, b, c):
	print ("The triangle is right-angled.")
else:
	print ("The triangle is not right-angled.")
	

