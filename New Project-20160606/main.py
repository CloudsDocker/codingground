# Hello World program in Python for Todd zhang
    
import time
import calendar

print "Hello World!\n"*5
localTime=time.asctime(time.localtime(time.time()))
print "local time" , localTime

cal=calendar.month(2016,6)
print "here is the calendar:"
print cal

print "time zone is ", time.timezone
print "time zone name is ", time.tzname

#function definition
def printme(str):
	"This print a passed string into this function"
	print str
	return;
	
#now call the function
printme("todd")


#function with defautl arguments
def printinfo(name, age=35):
	"this  print a passed info"
	print "name: ", name
	print "Age ",age
	return;
	
#now call the function
printinfo(age=50,name="miki")
printinfo(name="miki")

#variable lenth arguments

def printinfov(arg1, *vartuple):
	" this prints a valirable passed arguments"
	print "output is:"
	print arg1
	print "vartuple output is:"
	for var in vartuple:
		print var
	return;
	
# now call the printinfov
printinfov(10)
printinfov(70,60,50)


# lambda functions

# function defeint
sum = lambda arg1, arg2 : arg1+arg2;

# now call
print "value of total: ", sum(10,30)


# test dir function, list functions in the module
import math

thePath=dir(math)

print thePath

print "############  file opertaion #################"
fo=open("tod.tmp","w+")
fo.write("python is a good langulage\n")
fo.write("definitely\n")
fo.close
print "  write down   , file name is: ", fo.name
fo=open("tod.tmp","r+")
str=fo.read()
print " the content are \n"
print str
fo.close()
