Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #-------------Lab 2 for CS3A04: Arithmetic-----------------------------------------------------------------------

'''


You will create two int variables,
my_id and num_let respectively,
into which you will store:

-The 8-digit number 12345678
-The number of letters in your family (last) name.

Your program will compute some values based on these two numbers.



The following five expressions assume that
you have stored the 8 digit number into the
variable myId, and the number of letters in
your last (family) name into the variable numLet.

You manually set both of these variables using assignment statements in your program source.

No user input is needed or allowed.

Compute the following five values:
#1: my_id % 17
#2: (num_let + 17) % 11
#3: float(my_id/(num_let+800))
#4  1 + 2 + 3 ... +num_let
#5  float(15000/(80+((my_id - 123456)/((num_let+20)*(num_let + 20)))))


First do the math on paper so you know what answers your program should generate
(but don't hand this stage in).


Write a program that computes and displays these five values.


Your run should look something like this (although the values will differ for each student):

Note that the first three lines are output from your program, not added after the run.

This should all be done in one run of a single program, not several runs.


'''



#-----------------------SOURCE-----------------------------------------------------------------------------------------
#create variable that stores an 8 digit number as an integer
my_id =  12345678

#create a variable that stores a string input of my  family lst name
family_name = 'Cawley'

#create a variable that stores that calculates the number of chrs in family_name
num_let = len(family_name)

#create 5 variables that calculate the formula's provided for the problem
expression_1 = my_id % 17
expression_2 = (num_let + 17) % 11
expression_3 = float(my_id/(num_let+800))
expression_4 = 1+2+3+4+5+6
expression_5 = float(15000/(80+((my_id - 123456)/((num_let+20)*(num_let + 20)))))

#store all 5 expression variables in a single variable and print each one individually
result = ('Expression #1 : ' + str(expression_1) + '\n'
          'Expression #2 : ' + str(expression_2) + '\n'
          'Expression #3 : ' + str(expression_3) + '\n'
          'Expression #4 : ' + str(expression_4) + '\n'
          'Expression #5 : ' + str(expression_5) + '\n')


print ('My family name is ' + family_name)
print ('Number is ' + str(my_id))
print  ('The number of characters in my last name is ' + str(num_let) + '\n')
print (result)

#--------------------------RUN-----------------------------------------------------------------------------------------


# /Users/scawley/PycharmProjects/CS3A04/venv/bin/python /Users/scawley/PycharmProjects/CS3A04/CA3A04_Lab02.py
# My family name is Cawley
# Number is 12345678
# The number of characters in my last name is 6
#
# Expression #1 : 6
# Expression #2 : 1
# Expression #3 : 15317.218362282878
# Expression #4 : 21
# Expression #5 : 0.8259816351862311
#
#
# Process finished with exit code 0
