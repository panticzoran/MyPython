# Playing with Lists

someList = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
for i in someList:
  print(i)

print("\n")

someOtherList = ["one", "two", "three", "then", "backwards"]
for i in someOtherList:
  print(i)

print("\n")

for i in range(len(someOtherList)):
  print(someOtherList[i])

print("\n")

students = [("John", ["CompSci", "Physics"]),
  ("Vusi", ["Maths", "CompSci", "Stats"]),
  ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
  ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
  ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]


# Listing students for the specific condition
counter = 0
studentsTakingSubject = ""
for (studentName, subjectTaken) in students:
  if "CompSci" in subjectTaken:
    counter += 1
    studentsTakingSubject += studentName + " "

print("The total number of students is", len(students))
print("The number of students taking CompSci is", counter, "and those are:", studentsTakingSubject)

print("\n")


