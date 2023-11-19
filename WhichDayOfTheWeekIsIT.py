# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write a function which is given the day number, and it returns the day name (a string).

def dayOfTheWeek(dayNr):
	dayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	return dayNames[dayNr]


day=int(input("Please enter the day's number:"))
print("The day number", day, " is named ", dayOfTheWeek(day))