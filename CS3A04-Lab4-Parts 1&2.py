'''CS3A04: Lab 4'''

'''
Part 1: SpongeBob's Year Conjecture

Write python code to prove or disprove
the theory that every year between 1988
- 2002 has repeated digits in the 4 year
digit identifier.  '''


'''-------------------SOURCE-------------------------------'''
# create a variable that stores every year from 1988 - 2012
sponge_bob = range(1988,2013)
#Check every year within that time range
for x in sponge_bob:
    #convert each year into a string
    sy = str(x)
    #create a number tracker that tracks number in a range (0,9)
    number_tracker = [0] * 10
    #check each number in the year
    for d in sy:
        #convert the number from a string to an integer
        di = int(d)
        #for each use of a number in a year, record it in the number tracker
        number_tracker[di] +=1

    #print out each year within the time range
    string_answer = "The year " + str(x)
    #check to see how times a number occurs in the number tracker
    for digit, occurance in enumerate(number_tracker):
        #check to see if a number appears more than once
        if occurance > 1:
            # if a number occurs more than once, return a string that states the year has duplicate numbers
            dup_numbers = " has duplicate numbers: "
            #check all of the variables used in string answer
            for b in string_answer:
                # check the answer to see if variable dup_numbers has been used
                if dup_numbers not in string_answer:
                    #add dup_numbers to string_answer if it has not been used
                    string_answer += dup_numbers
            #add any duplicate numbers to the string_answer variable if used
            string_answer += str(digit)
            # for strings in string_answer:
            #     strings = "{1:20} {0:25}".format(strings[0], strings[0])

    #return the answer for every year
    print (string_answer)


''' ----------------------RUN---------------------------------------------------
The year 1988 has duplicate numbers: 8
The year 1989 has duplicate numbers: 9
The year 1990 has duplicate numbers: 9
The year 1991 has duplicate numbers: 19
The year 1992 has duplicate numbers: 9
The year 1993 has duplicate numbers: 9
The year 1994 has duplicate numbers: 9
The year 1995 has duplicate numbers: 9
The year 1996 has duplicate numbers: 9
The year 1997 has duplicate numbers: 9
The year 1998 has duplicate numbers: 9
The year 1999 has duplicate numbers: 9
The year 2000 has duplicate numbers: 0
The year 2001 has duplicate numbers: 0
The year 2002 has duplicate numbers: 02
The year 2003 has duplicate numbers: 0
The year 2004 has duplicate numbers: 0
The year 2005 has duplicate numbers: 0
The year 2006 has duplicate numbers: 0
The year 2007 has duplicate numbers: 0
The year 2008 has duplicate numbers: 0
The year 2009 has duplicate numbers: 0
The year 2010 has duplicate numbers: 0
The year 2011 has duplicate numbers: 1
The year 2012 has duplicate numbers: 2

'''

'''
Part 2: The non-integral Multiplication Table

Write python code to print a non-integral multiplication table
for the range 0.5 to 5.5.
'''

'''---------------SOURCE---------------------------------------'''

# create variables for starting values for the range (0.5,5.5)
mutli_table = 6
# create a variable to hold the start of the range in each row
row_value = 0.5

# for formatting, set a variable with spacing for the column headers
heading_row = "".ljust(10)
answers = ""

# loop through the range for each number
while row_value < mutli_table:
    # for each number between 0.5 to 5.5, create a column and row
    heading_row += str(row_value).ljust(10)

    # create a space in each column and row to hold the answers
    answers += str(row_value).ljust(10)
    # create a variable to hold the start of the range in each column
    column_value = 0.5
    # loop each number in the first column
    while column_value < mutli_table:
        # multiply the first number in each row by the header number in each column
        answer = row_value * column_value
        ##add the answer to each empty space in the column
        answers += str(answer).ljust(10)
        column_value += 1

    # create a new a new space for each answer
    answers += "\n"
    row_value += 1.0

# print the headings for the column and rows
print(heading_row)
# print the answers in each row
print(answers)

'''-------------RUN-------------------------------

          0.5       1.5       2.5       3.5       4.5       5.5
0.5       0.25      0.75      1.25      1.75      2.25      2.75
1.5       0.75      2.25      3.75      5.25      6.75      8.25
2.5       1.25      3.75      6.25      8.75      11.25     13.75
3.5       1.75      5.25      8.75      12.25     15.75     19.25
4.5       2.25      6.75      11.25     15.75     20.25     24.75
5.5       2.75      8.25      13.75     19.25     24.75     30.25




'''
