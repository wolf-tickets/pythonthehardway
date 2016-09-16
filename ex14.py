from sys import argv

script, first_name, last_name = argv
prompt = '??? '
print "Hi %s, I'm the %s script." % (first_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s %s" % (first_name, last_name)
likes = raw_input(prompt)

print "Where do you live %s?" % first_name
lives = raw_input(prompt)

print "What kind of computer do you have, Mr. %s?" %last_name
comp = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, comp)

