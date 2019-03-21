'''Part 1: Find Primes'''

'''
------------------SOURCE------------------------------------
'''
#take a list of numbers from the candidate
candidatePrimes = [10, 12, 15, 17, 31, 89, 97, 7919, 982451653]

#loop through each number in the list
for x in candidatePrimes:
    # if input number is less than or equal to 1, it is not prime
    if x > 1:
        # loop through each number each number greater than two up to x
        for i in range(2, x):
            #divide the number x by each number lower than it and check the remainder
            if (x % i) == 0:
                #print 'x is not a prime number" if the remainder is 0 for x divided by each lower number
                print(x, "is not a prime number")
                break
        #if the remainder is greater than 0 for x x divided by any of the lower numbers
        else:
            #print "x is a prime number"
            print(x, "is a prime number")

    # if input number is less than or equal to 1, it is not prime
    else:
        print(x, "is not a prime number")



'''
---------------------RUN----------------

10 is not a prime number
12 is not a prime number
15 is not a prime number
17 is a prime number
31 is a prime number
89 is a prime number
97 is a prime number
7919 is a prime number
982451653 is a prime number

'''




''' Part 2: Turn your code into a function '''

'''
------------------SOURCE--------------------------------------



'''

#create a function to check if a number is prime
def isPrime(p):
#check if the number is greater than 1
    if p > 1:
        # loop through each number each number greater than two up to x
        for i in range(2, p):
            # divide the number x by each number lower than it and check the remainder
            if (p % i) == 0:
                #if the number is not prime, return 0
                return (0)
                break
       #if the number is prime, return the number
        else:
            return (p)


    else:
        return (p)



#return the function
print (isPrime(int(19)))

'''
-------------------PART 2: RUN--------------------------------------------------------------
19


'''


'''-------------------PART 3: Use your function--------------------------------------'''

'''--------------------PART 3: SOURCE------------------------------------'''



#create a function to check for prime numbers in a range
def primesInRange(low,up):
    #make and empty list to store the prime numbers
    prime_list = []
    #check all the numbers in the range
    for num in range(low,up):
        #for any number greater than 1, use the isPrime function to check if its prime
        if num > 1:
            is_prime = isPrime(num)
            #if the number is prime, add it to the list
            if is_prime:
                prime_list.append(is_prime)
                #when the list contains 3 numbers, return the list
                if len(prime_list) == 3:
                    return prime_list

    #test to make sure the list returns 3 numbers
    if len(prime_list) < 3:
        return prime_list


print (primesInRange(1000,1500))

'''
-------------PART 3: RUN----------------

[1009, 1013, 1019]
'''
