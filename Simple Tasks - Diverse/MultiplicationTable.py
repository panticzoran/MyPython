# Printing multiplicaton tables, not formatted


def printRow(number, howManyNumbers):
  for i in range(1, howManyNumbers + 1):
    print(i * number, end="  ")


def printTable(rows, columns, number):
  for i in range(1, columns + 1):
    printRow(number * i, rows)
    print(end="\n")


printRow(7, 10)

print(end="\n\n")

printTable(7, 7, 1)

print("\n")

# Multiplication table, formatted

x = 12
y = 12

for i in range(1, y + 1):
  for j in range(1, x + 1):
    result = i * j
    place = len(str(x))
    print("|{:^7}".format(result), end='')
  print(end='|')
  print("\n")

print("\n")
