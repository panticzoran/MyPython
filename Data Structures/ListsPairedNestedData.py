# Working with lists with paired and nested data

students = [("John", ["CompSci", "Physics"]),
            ("Vusi", ["Maths", "CompSci", "Stats"]),
            ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
            ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
            ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

for (name, courses) in students:
  print("The student", name, "takes", len(courses), "courses.")
print("\n")

for (name, courses) in students:
  for i in courses:
    if i == "CompSci":
      print("Student", name, "takes", i, "course.")
