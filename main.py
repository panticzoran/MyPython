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


# Listing students for the specific condition v1
counter = 0
studentsTakingSubject = ""
for (studentName, subjectTaken) in students:
  if "CompSci" in subjectTaken:
    counter += 1
    studentsTakingSubject += studentName + " "

print("The total number of students is", len(students))
print("The number of students taking CompSci is", counter, "and those are:", studentsTakingSubject)

print("\n")


# Listing students for the specific condition v2
counter = 0
studentsTakingSubject = []
for (studentName, subjectTaken) in students:
  if "CompSci" in subjectTaken:
    counter += 1
    studentsTakingSubject.append(studentName)

print("The total number of students is", len(students))
print("The number of students taking CompSci is", counter, "and those are:", studentsTakingSubject)

print("\n")


# Enumerating

for (i, value) in enumerate(students):
  print(i, value)

print("\n")


# Enumerating structure

for (i, sName) in enumerate(students):
  print(i, "---", sName)
  for valueSub in sName:
    print("--", valueSub)
    for (z, sCourses) in enumerate(valueSub):
      print(z, "-", sCourses)
  print("\n")

print("\n")


# Passing a list as an argument actually passes a reference to the list, not a copy or 
# clone of the list.

def double_stuff(a_list):
  """ Overwrite each element in a_list with double its value. """
  for (idx, val) in enumerate(a_list):
    a_list[idx] = 2 * val

things = [2, 5, 9]
print("Original list", things)
double_stuff(things)
print("List after calling the function", things)

print("\n")