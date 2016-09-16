def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r." % (arg1, arg2)
	
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r." % (arg1, arg2)
	
def print_one(arg1):
	print "arg1: %r." % arg1
	
def print_name():
	print "I got nothin."
	
print_two("Al", "Smith")
print_two_again("Al", "Smith")
print_one("First")
print_name()
