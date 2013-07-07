# Enter your answers for chapter 6 here
# Name: Stephanie Frias


# Ex. 6.6
def first(word):
	return word[0]
	
def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]
	
def is_palindrome(word):
		if len(word)<=1:
			return True
		if first(word) != last(word):
			return False
		return is_palindrome(middle(word))

print is_palindrome('Stephanie')
print is_palindrome('redivider')
print is_palindrome('racecar')
print is_palindrome('poop')

# Ex 6.8

def gcd(a,b):
	c = abs (a-b)
	if a == b: 
		return b
	if a > b:
		return gcd(c,b)
	if a < b:
		return gcd(c,a)

print gcd(11,7)
print gcd(120,36)
print gcd(300,456)


