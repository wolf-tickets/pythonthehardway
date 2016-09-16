#Defines variable x as a string with the embedded variable d defined as 10
x = "There are %d types of people." % 10
#defines variable 'binary' as the string "binary"
binary = "binary"
#defines variable 'do_not' as the string "don't"
do_not = "don't"
#defines the variable y as a string with the two above variables embedded
y = "Those who know %s and those who %s." % (binary, do_not)

#outputs the string defined as variable x above
print x
#outputs the string defined as variable y above
print y
#outputs string with embedded variable x, which is a string defined above
print "I said: %r." % x
#does the same with variable y, also a string defined above
print "I also said: '%s'." % y
#defines variable 'hilarious' as False
hilarious = False
#defines variable 'joke_evaluation' as a string with embedded variable r
joke_evaluation = "Isn't that joke funny? %r"
#returns the joke_evaluation string with variable 'hilarious' (defined as False) for r
print joke_evaluation % hilarious
#defines w as a string
w = "This is the left side of..."
#defines e as a string
e = "a string with a right side."
#returns w and e together one after the other
print w + e
