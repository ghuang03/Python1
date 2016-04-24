################## ######
import sys
import os
#import random

##########################################################
#def add(num1, num2):
#	return num1 + num2
	
#def main():
#	operation = input ("What do you want to do (+,-,*,/):")
#	if (operation != '+' and operation != '-' and operation != '*' and operation != '/'):
#		#invalid operation
#		print ("You must enter a valid operation")
#	else:
#		var1 = int(input("Enter num1:" ))
#		var2 = int(input("Enter num2:"))
#		if(operation == '+'):
#			print (add (var1, var2)			

			
#main()
########################################################		
def main():
	print('What is file name to be edited?')
	filename = sys.stdin.readline()
	print ("File name is: ", filename)

	test_file = open ("filename", "wb")
	print (test_file)
	print(test_file.mode)
	print(test_file.name)
	print(test_file.mode)
	print(test_file.name)
	test_file.write(bytes("Write me to the file, please please\n", 'UTF-8'))
	test_file.close()
	try:
		test_file = open ("filename" , "r" )

		print (test_file.read())
#   	t = test_file.read()
#		print (t)
		test_file.close()
	except IOError:
		HandleError()
		Print ('IO Error', filename)
		
main()
################################

#def Cat(filename):
#	try:
#		f = open(filemname)
#		text = f.read()
#		print ('---', filename)
#		print (text)
#	except IOError:
#		HandleError()
#		print 'IO Error', filename








#################
#print('What is your name' )
#name = sys.stdin.readline()

#print ('Hello', name)
	
############## #########
#	long_string = "I'll catch you if you fall -the Floor"
#	print (long_string[0:4])  #I'll
#	print (long_string[-5:])  #Floor
#	print (long_string[:-5])   #I'll catch if ...
#	print(long_string[:4] + "be there") # I'll be there
#	print ("%c is my %s letter and my number %d number is %.5f, 9'X', 'favorite', 1, .14))
	
	# X is my favorite letter and my number 1 number is 0.14000
	
####### #########
#long_string = "I'll catch you if you fall -The Floor"
#print (long_string.captalize())
#print (long_string.find("Floor"))
#print (long_string.isalpha())
#print(long_string.isalnum())
#print(len(long_string))
#print(long_string_replace("Floor", "Ground"))
#print (long_string.strip())
#quote_list = long_string.split("")

########
