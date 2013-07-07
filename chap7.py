# Enter your answers for chapter 7 here
# Name: Stephanie Frias


# Ex. 7.5

import math
	
def factorial(n):
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result		

def estimate_pi():
	s = 0
	summation = 0
	while True:
		multiplier = ((2*math.sqrt(2))/9801)
		numerator = ((factorial(4*s))*(1103+26390*s))
		denominator =((factorial(s))**4)*(396**(4*s))
		calculation = multiplier*(numerator/denominator)
		summation += calculation

		if abs(calculation) <1e-15: break
		s += 1

	return 1/summation

print estimate_pi()

# How many iterations does it take to converge?