# solves quadratic equation

import math


# Inputs 3 coeficients and returns 2 values for x
def solve_quadratic(a, b, c):
  d = (b**2) - 4 * a * c
  s1 = (-b + math.sqrt(d)) / (2 * a)
  s2 = (-b - math.sqrt(d)) / (2 * a)
  return s1, s2
