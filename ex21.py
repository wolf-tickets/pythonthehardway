def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a + b
	
def subtract (a, b):
	print "Subtracting %d - %d" % (a, b)
	return a - b
	
def multiply (a, b):
	print "Multiplying %d * %d" % (a, b)
	return a * b
	
def divide (a, b):
	print "Dividing %d / %d" % (a, b)
	return a / b
	
def puzzle (a, b, c, d):
	print """
	The solution to the puzzle is %d divided by 2, multiplied by %d, subtracted from %d, 
	added to %d.
	""" % (d, c, b, a)
	raw_input()
	return add(a, subtract(b, multiply(c, divide(d, 2))))

	
	
print "Let's do some math with just functions!"
raw_input()
	
age = add(30, 4)
height = subtract(78, 6)
weight = multiply(64, 3)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
raw_input()

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

raw_input()

print "That becomes: %d. Can you do it by hand?" % what
raw_input()

solution = puzzle (age, weight, height, iq)
print solution


