#imports argv feature from the sys package
from sys import argv
#gets two arguments: the script name and one command line argument which should be the 
#filename
script, filename = argv
#uses the open command to open the example text file from the command line argument and 
#assigns it to the variable txt
txt = open(filename)

#prints the name of the text file from the command line argument
print "Here's your file %r:" % filename
#prints the contents of the text file by using the read function
print txt.read()



#prompts the user to re-enter the text file name from the command line argument
print "Type the filename again:"
#assigns the user's input to the variable file_again
file_again = raw_input("> ")

#takes the filename from file_again and opens the file
txt_again = open (file_again)

#prints the contents of the file with the filename from file_again, 
#using the read function
print txt_again.read()

txt.close()
txt_again.close()

