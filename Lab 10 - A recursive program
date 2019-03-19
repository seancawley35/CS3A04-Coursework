'''
CS3A04 Lab 10: A recursive program
Student: Sean CawleyMarch 16, 2019
Submission Date:


'''

'''

PART 1 (5 points)

1.   Write a factorial calculator  that uses looping (a "for loop").

2.  The signature of the main method will be:

    def factorialI(n):


'''


'''create the factorialI function '''
def factorialI(n):
    '''create an object to set the beginning of the range to 1'''
    result = 1
    '''use a for loop to run the factorial 0 - n'''
    for i in range(2, n + 1):
        '''return the product of an integer and all the integers below it'''
        result *= i
        '''return the result of the factorial loop'''
    return result


'''print the result'''
print (factorialI(6))


'''
-------
OUTPUT
-------

720



'''



'''
PART 2

1. Write a factorial calculator that uses recursion.

2.  Write a factorial calculator that uses recursion.

3.  The signature of the main method will be: def factorialR(n):

4.  The base case in the recursive function will be: if n == 1:  return 1


5.  And a return statement for the result of the non-base case, of course: return result


6.  Put in a print statement as the first line of the function:

    print("factorial has been called with n = " + str(n))


7.  Put in a print statement as the "last" line of the function, immediately before you return the result

    print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)


8.  Try factorial(4), and factorial(7) with the printing.

9.  Run the code for a number big enough to take  5 to 10 seconds to calculate.
    Disable the prints before running on big numbers!


'''


'''import the System-specific parameters and functions module to change the recursion limit  '''
import sys

'''set the recursion limit to a larger number'''
sys.setrecursionlimit(1000000000)



'''create the function factorialR'''
def factorialR(n):
    print("factorial has been called with n = " + str(n))
    '''set the limit for the recursion'''
    if n == 1:
        return 1
    else:
        '''use the recursion to return the factorial of a number'''
        result = n * factorialR(n - 1)
        print("intermediate result for ", n, " * factorial(", n - 1, "): ", result)
        return result

print (factorialR(5))
print (factorialR(4))
print (factorialR(7))
print (factorialR(19000))


'''
-------
OUTPUT
-------

#output of factorialR(5) run


factorial has been called with n = 5
factorial has been called with n = 4
factorial has been called with n = 3
factorial has been called with n = 2
factorial has been called with n = 1
intermediate result for  2  * factorial( 1 ):  2
intermediate result for  3  * factorial( 2 ):  6
intermediate result for  4  * factorial( 3 ):  24
intermediate result for  5  * factorial( 4 ):  120
120





#output of factorialR(4) run

factorial has been called with n = 4
factorial has been called with n = 3
factorial has been called with n = 2
factorial has been called with n = 1
intermediate result for  2  * factorial( 1 ):  2
intermediate result for  3  * factorial( 2 ):  6
intermediate result for  4  * factorial( 3 ):  24
24


#output of factorialR(7) run

factorial has been called with n = 7
factorial has been called with n = 6
factorial has been called with n = 5
factorial has been called with n = 4
factorial has been called with n = 3
factorial has been called with n = 2
factorial has been called with n = 1
intermediate result for  2  * factorial( 1 ):  2
intermediate result for  3  * factorial( 2 ):  6
intermediate result for  4  * factorial( 3 ):  24
intermediate result for  5  * factorial( 4 ):  120
intermediate result for  6  * factorial( 5 ):  720
intermediate result for  7  * factorial( 6 ):  5040
5040



#output of factorialR(1900) run without the additional print statements


18269664890451808503759816441495224075060017015236339048166631794963702284859618077510730648594200258970571398395418855799288427113031285351275436795719246317177488972144058281682147836635539382577209947423541640728543394827552

'''




'''

PART 3 (7 points)

1.  Add the benchmarking code to your two programs.

2.  Run them both on the big number you used in part 2 (or such smaller number needed
    to get it to run in less than a few seconds). Disable print statements in the
    code-to-be-measured before benchmarking.

3.  Explain the difference in times between the iterative and the recursive code.

    #first run with factorial using recursion for int (5)
    starting timer
    elapsed time: 14.425366765994113 secs


    #second run with factorial using recursion for int (5)
    starting timer
    elapsed time: 14.425366765994113 secs


    #third run with factorial using recursion for int (30)
    starting timer
    elapsed time: 99.67518130198005 secs




    #first run with factorial using a for loop for for int (5)
    starting timer
    elapsed time: 11.90581857500365 secs

    #second run with factorial using a for loop for int (5)
    starting timer
    elapsed time: 12.098595732008107 secs

    ##third run with factorial using a for loop for int (30)
    starting timer
    elapsed time: 47.51407868301612 secs


    #both recursive  and for loop run at the same time for int (30)
    recursive factorial
    starting timer
    elapsed time: 96.2751155020087 secs

    for loop factorial
    starting timer
    elapsed time: 49.17202572801034 secs


    #The reason for the difference in recursion vs iteration run times

    For the difference in times, the recursive code took longer to run than the
    iteration code. As the integer increases in size, the difference in run time
    grows bigger between iteration and recursion runs

    The difference between recursion and iteration is that recursion is a method call in "which the method
    being called is the same as the one making the call while iteration is when a loop is repeatedly
    executed until a certain condition is met."
    ("Iteration vs Recursion". Feb 25, 2018, https://medium.com/backticks-tildes/iteration-vs-recursion-c2017a483890)

    "A conditional statement decides the termination of recursion while a control variable’s
    value decide the termination of the iteration statement. Infinite recursion can lead to
    system crash whereas, infinite iteration consumes CPU cycles."
    ("Iteration vs Recursion". Feb 25, 2018, https://medium.com/backticks-tildes/iteration-vs-recursion-c2017a483890)

     Recursion and iteration perform the same kinds of tasks. In Python, iterative functions can be changed to
     recursion because iteration is just a version of recursion known as tail recursion. "Recursion is usually slower
     and uses more memory because of the overhead of creating and maintaining stack frames. However,recursion is the
     better choice when exploring/manipulating recursive data structures like linked lists and trees or parsing
     expressions"
     ("Iteration vs. recursion". https://www.ocf.berkeley.edu/~shidi/cs61a/wiki/Iteration_vs._recursion)


'''


'''import the System-specific parameters and functions module to change the recursion limit  '''
import sys
'''import the timeit module to test the I/O or both the for loop and recursion factorial functions'''
from timeit import default_timer as timer
'''set the recursion limit to a larger number'''
sys.setrecursionlimit(1000000000)



'''create the function factorialR'''
def factorialR(n):
    #print("factorial has been called with n = " + str(n))
    '''set the limit for the recursion'''
    if n == 1:
        return 1
    else:
        '''use the recursion to return the factorial of a number'''
        result = n * factorialR(n - 1)
        #print("intermediate result for ", n, " * factorial(", n - 1, "): ", result)
        return result

def func_to_measure():
    result = factorialR(30)
    return result

print("recursive factorial")
print("starting timer")
start = timer()
for i in range(20000000):  # Adjust this number down, to get shorter runtimes!!!
    func_to_measure()
end = timer()

elapsed = end - start
print("elapsed time:", elapsed, "secs")
print(" ")



'''
Factorial using a for loop
'''

'''create the factorialI function '''
def factorialI(n):
    '''create an object to set the beginning of the range to 1'''
    result = 1
    '''use a for loop to run the factorial 0 - n'''
    for i in range(2, n + 1):
        '''return the product of an integer and all the integers below it'''
        result *= i
        '''return the result of the factorial loop'''
    return result

'''use the func_to_measure function to test the I/O runtime of the program'''
def func_to_measure():
    result = factorialI(30)
    return result

print("for loop factorial")
print("starting timer")
start = timer()
'''use a for loop to check the run time of the program'''
for i in range(20000000):  # Adjust this number down, to get shorter runtimes!!!
    func_to_measure()
end = timer()

elapsed = end - start
print("elapsed time:", elapsed, "secs")


'''
-------
OUTPUT
-------

#first run with factorial using recursion for int (5)
starting timer
elapsed time: 14.425366765994113 secs


#second run with factorial using recursion for int (5)
starting timer
elapsed time: 14.425366765994113 secs


#third run with factorial using recursion for int (30)
starting timer
elapsed time: 99.67518130198005 secs




#first run with factorial using a for loop for for int (5)
starting timer
elapsed time: 11.90581857500365 secs

#second run with factorial using a for loop for int (5)
starting timer
elapsed time: 12.098595732008107 secs

##third run with factorial using a for loop for int (30)
starting timer
elapsed time: 47.51407868301612 secs


#both recursive  and for loop run at the same time for int (30)


recursive factorial
starting timer
elapsed time: 96.2751155020087 secs

for loop factorial
starting timer
elapsed time: 49.17202572801034 secs


'''


