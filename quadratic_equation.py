import math

def solve_quadratic(a, b, c):
	d = (b ** 2) - 4 * a * c
	s1 = (-b + math.sqrt(d)) / (2 * a)
	s2 = (-b - math.sqrt(d)) / (2 * a)
	return s1, s2

