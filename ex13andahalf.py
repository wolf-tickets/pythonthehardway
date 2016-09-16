from sys import argv

script, first, second = argv

a = raw_input ("How many %s are there?  " % first)
b = raw_input ("How many %s are there?  " % second)
print "Alright. You have a total of ", int(a) + int(b), " animals!"

