def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "That's enough for a party!"
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly."
cheese_and_crackers(20, 30)
raw_input()

print "Or we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
raw_input()

print "We can even do math inside."
cheese_and_crackers(30 - 15, 40 - 20)
raw_input()

print "And we can combine the two, variables and math."
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
raw_input()
