# Since variables refer to objects, if we assign one variable to another, both variables
# refer to the same object:

a = "Lala"
b = a
print("a and b :", a, b)
print("a and b are same object:", a is b)
print("a and b have the same value:", a == b)
print("----")
# Asining a new value to a, b stays the same, only a changes
a = "nesto"
print("a and b :", a, b)
print("a and b are same object:", a is b)
print("a and b have the same value:", a == b)

print("\n")

# This is not the case with lists (a and b have the same value but do not refer to the 
# same object):
a = [1, 2, 3]
b = [1, 2, 3]
print("a and b :", a, b)
print("a and b are same object:", a is b)
print("a and b have the same value:", a == b)
print("----")
# Asining a new value to a, b stays the same, only a changes
a = [1, 3, 3]
print("a and b :", a, b)
print("a and b are same object:", a is b)
print("a and b have the same value:", a == b)


print("\n")

# Because the same list has two different names, a and b, we say that it is aliased. 
# Changes made with one alias affect the other:
a = [1, 2, 3]
b = a
print("a and b :", a, b)
print("a and b are same object:", a is b)
print("a and b have the same value:", a == b)
print("----")
# Asining a new value to a, b stays the same, only a changes
a = [1, 3, 3]
print("a and b :", a, b)
print("a and b are same object:", a is b)
print("a and b have the same value:", a == b)