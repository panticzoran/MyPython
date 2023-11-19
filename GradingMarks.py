# Write a function which is given an exam mark, and it returns a string — the grade for that mark

def grade(markGotten):
	if markGotten >= 75:
		return "First"
	elif markGotten >= 70 and markGotten < 75:
		return "Upper Second"
	elif markGotten >= 60 and markGotten < 70:
		return "Second"
	elif markGotten >= 50 and markGotten < 60:
		return "Third"
	elif markGotten >= 45 and markGotten < 50:
		return "F1 Supp"
	elif markGotten >= 40 and markGotten < 45:
		return "F2"
	else :
		return "F3"


xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in xs:
	print("Grade for the mark ", i , " is: ", grade(i))

