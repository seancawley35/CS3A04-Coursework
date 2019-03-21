#----------------Lab 1 for CS3A04: Hello World-----------------------------------------------------------------------

# This is an easy assignment, and everyone needs to complete it.
'''Let's all just focus on making sure we have the Idle IDE working, the indentation perfect and any tab characters removed.
This will ensure you get the most points in your first assignment, which may come in handy down the road.


Make sure you have read and understood
both modules A and B this week, and
module 2R - Lab Homework Requirements
before submitting this assignment. Hand in only one program, please.

Please review your reading resources Reading (mm)


Write, run and debug a version of the "Hello World!" program from your first week's module.

Include your last (family) name.

Include an eight digit random number that you made up.


Note any two details  from page one of my Syllabus and three details
from the Lab Homework Requirements Page 2: Specific Requirements'''


#----------------------------------------------------------------------------------------------------------------------



'''Syllabus Notes 1: "Collaboration with others is a not allowed and copying code is banned (no stack overflow!!!!.


Syllabus Notes 2: 'To stay enrolled in class, complete all assignments and labs on time and complete all exams.


From Lab Notes 1: If you fail  to complete an assignment on time,you have one week to turn it in for 50%  of the grade 


From Lab Notes  2: Remove all the tabs in your settings and change it to four spaces each for spacing  

From Lab Notes 3: Always make sure your code is readable.  Do not bunch all of your code together'''

#--------------------------------------------------------------------------------------------------------------------


#Sean Cawley's code for Lab 1

#-------------------SOURCE--------------------------------------

#Imported the random function just to have more fun with the 8 random number generator
import random

#Assign a variable with my last name
last_name = 'Cawley'
my_name = ('My last name is ' + last_name)


#create a random 8 didgit number generator
Random_8 = random.randint(00000000,99999999)
#Assign a variable fot the statement containing my random number generator and display it as a string
my_number = ('My random 8 digit number is ' + str(Random_8))


#create 5 variables (2 for the syllabus notes and 3 for the labwork notes
Syllabus_Detail1 = 'Collaboration with others is a not allowed and copying code is banned (no stack overflow!!!! \n'
Syllabus_Detail2 = 'To stay enrolled in class, complete all assignments and labs on time and complete all exams. \n'
Labhomework_Note1 = 'If you fail  to complete an assignment on time,you have one week to turn it in for 50%  of the grade \n'
Labhomework_Note2 = 'Remove all the tabs in your settings and change it to four spaces each for spacing \n'
Labhomework_Note1 = 'Always make sure your code is readable.  Do not bunch all of your code together \n'


#create a variable that combines all 5 note variables
class_notes = (Syllabus_Detail1 + Syllabus_Detail2 + Labhomework_Note1 + Labhomework_Note2 + Labhomework_Note1 )


#print all the variables on 7 seperate lines

print("Hello World")
print("Let's keep in touch.")
print(my_name)
print( my_number)
print (class_notes)


#------------------RUN-------------------------------------------------------------------------------------------------


'''/Users/scawley/PycharmProjects/CS3A04/venv/bin/python /Users/scawley/PycharmProjects/CS3A04/CS3A04_Lab01.py
Hello World
Let's keep in touch.
My last name is Cawley
My random 8 digit number is 45914890
Collaboration with others is a not allowed and copying code is banned (no stack overflow!!!! 
To stay enrolled in class, complete all assignments and labs on time and complete all exams. 
Always make sure your code is readable.  Do not bunch all of your code together 
Remove all the tabs in your settings and change it to four spaces each for spacing 
Always make sure your code is readable.  Do not bunch all of your code together 


Process finished with exit code 0'''


#--------------------------------------------------------------------------------------------------------------------

