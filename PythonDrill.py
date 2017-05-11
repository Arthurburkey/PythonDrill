#Author:  Arthur Burkey
#
#Purpose: The Tech Academy - Python Course Slide 36 drill: Write my own program
#using assignment: int to var, str to var, float to var, .format()notation,
#operators(+,-,*,/,+=,=,%), logical operators(and,or,not), conditional statements
#(if, elif, else), while loop, for loop, list with loop interation of each line,
#create tuple and iterate through it using a for loop to print each item, define
#function that returns string var, call functions and print result to shell

#Assign an integer to a variable
a = 1

#Assign a string to a variable
b = "string"

#Assign a float to variable
c = 10.5

#Use the print function and .format()notation to print out assigned variable
x = 1    #method 1
print(x)

x = 1    #method 2
print

#Using operators +,-,*,/,+=,=,%
a = 1 #using addition    
b = 2
c = a + b
print(c)

a = 1 #using subtraction
b = 2
c = b - a
print(c)

a = 1 #using multiplication
b = 2
c = b * a
print(c)

a = 2 #using division
b = 4
c = b / a
print(c)

a = 1 #using +=
a += 4
print a

x = 9 #using =
y = 9
z = 9 / 9
print z

#using %(
name = raw_input("What is your name?")
print "your name is %s" % (name,)

#Use of logical operators: and, or, not
x = 1 #using, "and" logical operator
y = 1
if (x == 1) and (y != 0) :
    print "assigned variables correlate with if/and \n statement"

#using, "or" logical operator
string = "Coding is fun" 
string = string.split()

if "fun" in string or "coding" in string:
    print "Coding is fun!"
else:
    print "find motivation"

#using, "not" logical operator
a = 2 
b = 3
if 4 not in (a, b):
    print "4 is not an assigned varible"
else:
    print "4 has been assinged to either a or b"

#use of conditional statements: if, elif, else
guess = int (raw_input("Guess a number from 1 to 3: "))
n=2
if  guess == n:
    print ("Good job! that's the correct number")
elif guess != n:
    print ("That is not the correct guess")
else:
     print ("Your guess is not correct")


#Use of while loop
count = 0
while (count < 12):
    print 'Counting in order: ', count
    count = count + 1
print "thank you for counting with us!"

#Use of a for loop
musicians = ['Stevie Ray Vaughn', 'Muddy Waters',  'B.B. King', 'Robert Johnson']
for legends in musicians:        
   print 'Blues Legend : ', legends
print "End of legendary Bluesmen list"


#Create list and iterate through listusing a for loop to print each item on new line
musicians = ['Stevie Ray Vaughn', 'Muddy Waters',  'B.B. King', 'Robert Johnson']
for legends in musicians:        
   print 'Blues Legend : ', legends
print "End of legendary Bluesmen list"

#Create a tuple and iterate through it using a for loop to print each item on new line
musician = ('1.Stevie Ray Vaughn', '2.Muddy Waters',  '3.B.B. King', '4.Robert Johnson')
guitartype = ('1.Fender','2.Gibson','3.Gibson','4.Accoustic')
print("Here are the musicians..\n")
for item in musician:
    print (item)

print("\nHere are the guitars they used..\n")
for item in guitartype:
    print (item)

#Define a function that returns a string variable
def printme( str ):
    "This function returns a string value"
    print str
    return;
printme("1st call on defined function")
printme("2nd call on defined function")

#Call the function you defined above and print the result to the shell
'''
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: E:\PythonDrill\TestingAndErase.py =================
1st call on defined function
2nd call on defined function
>>> 
