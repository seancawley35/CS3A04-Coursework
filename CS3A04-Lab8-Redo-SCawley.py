
'''
CS3A04 Lab 8: How to Cheat at Vegas
Student Name: Sean Cawley
Submission Date: March 3, 2019 at 11:00pm PT

The program is designed to run a Las Vegas style slot machine
with and uses the Triple String Class function from week 7
'''


'''--------SOURCE-------------------'''




'''Import the random string function'''
import random


'''1. Create a class called TripleString'''

class TripleString:
    '''Create the  Class level constants'''
    MIN_LEN = 1
    MAX_LEN = 50
    DEFAULT_STRING = 'none'

    '''Create the constructor method'''
    def __init__(self, string1 = DEFAULT_STRING, string2 = DEFAULT_STRING, string3 = DEFAULT_STRING):
        '''Create class-defined instance attributes (attributes)'''
        self.string1 = string1
        self.string2 = string2
        self.string3 = string3

    ''' Create the mutator ("Set") methods'''
    def set_string1(self, the_mg):
        if self.valid_string(the_mg):
            self.string1 = the_mg
            return True
        else:
            self.string1 = TripleString.DEFAULT_STRING
            return False

    def set_string2(self, the_mg):
        if self.valid_string(the_mg):
            self.string2 = the_mg
            return True
        else:
            self.string2 = TripleString.DEFAULT_STRING
            return False

    def set_string3(self, the_mg):
        if self.valid_string(the_mg):
            self.string3 = the_mg
            return True
        else:
            self.string3 = TripleString.DEFAULT_STRING
            return False

    '''Create the Accessor ("Set") methods'''
    def get_string1(self):
        return self.string1

    def get_string2(self):
        return self.string2

    def get_string3(self):
        return self.string3

    '''Create the Helper methods'''
    def valid_string(self, string_to_set):
        if len(string_to_set) < 1 or len(string_to_set) > 50:
            return False
        else:
            return True

    def to_string(self):
        master_string = ("strings are:\n\t{}\n\t{}\n\t{}\n".format(self.string1, self.string2, self.string3) )
        return master_string






'''Create the constant for the slot wheels:'''
wheel_options = ["cherries","BAR","7","space"]


'''
Create a function for the user to place a bet
between the range of 0 - 50 dollars USD.  The 
function will check if the bet is a legal bet up
to $50 and will play until the player inputs
$0, at which point the game ends
'''
#create a function for the user to place a bet
def get_bet():
    valid_bet = False
    #create ab object to get the input bet from the user
    while not valid_bet:
        bet = int(input("Place your bet: "))
        #set the range for the bet as a legal bet between $1 - $50
        if 0 < bet < 51:
            #if the bet is a legal bet, diplay the bet
            print("Your bet is $" + str(bet))
            valid_bet = True
            return bet
        #if the user bets $0, the game ends
        elif bet == 0:
            print ("Game over ")
            valid_bet = True
            return bet
        else:
            print("Invalid bet")


'''Create a function for the user to pull the lever and return TripleString()
with three random slot characters. The function creates a a variable wheels
that is set three times to return a random string generation, simulating the three
 wheels in a real slot machine'''
def pull():
    wheels = TripleString()
    wheels.set_string1(rand_string())
    wheels.set_string2(rand_string())
    wheels.set_string3(rand_string())
    return wheels



'''Create a function that returns a random string of three 
characters from the pull function.  The function will be used in 
the pull function '''
def rand_string():
    '''Create an object that creates a random integer between 0 - 100
    that creates the odds of returning string'''
    rand_int = random.randrange(0,101)
    '''Return the string "cherries" if the number is between 0 - 40'''
    if rand_int in range(0,41):
        return ("cherries")
    # return the string "BAR" if the number is between 41 - 78
    elif rand_int in range(41,79):
        return ("BAR")
    # return the string "7" if the number is between 79 - 93'''
    elif rand_int in range(79, 94):
        return ("7")
    # return the string "space" if the number is between 0 - 40
    elif rand_int in range(94, 101):
        return ("space")



'''
Create a function for the payout of the returned slot figures from the play.  The payout 
is based on the following combinations in the specific orders below from left to right
in the wheel display. 
'''
def get_pay_multiplier(wheels, bet):
    '''If the returned string matches a defined set,
    returns a payout that multiplies the win parameter
    times the amount of the users bet '''
    if ((wheels.get_string1() == "cherries") and (wheels.get_string2() != "cherries")):
        win = 5 * bet
    elif ((wheels.get_string1() == "cherries") and (wheels.get_string2() == "cherries") and (wheels.get_string3() != "cherries")):
        win = 15 * bet
    elif ((wheels.get_string1() == "cherries") and (wheels.get_string2() == "cherries") and (wheels.get_string3() == "cherries")):
        win = 30 * bet
    elif ((wheels.get_string1() == "BAR") and (wheels.get_string2() == "BAR") and ((wheels.get_string3() == "BAR"))):
        win = 50 * bet
    elif ((wheels.get_string1() == "7") and (wheels.get_string2() == "7") and ((wheels.get_string3() == "7"))):
        win = 100 * bet
    else:
        win = -bet

    return win


'''Display the three strings inside reels along with "sorry - you lost" or "congrats, you won $X."'''
def display(reels, winnings, current_win):
    global stake
    '''create three objects to display the slot reals'''
    variable1 = reels.get_string1()
    variable2 = reels.get_string2()
    variable3 = reels.get_string3()
    '''If the player wins a slot pull, return the string that displays how much they won'''
    if (current_win > 0):
        print(variable1 + '     ' + variable2 + '     ' + variable3)
        print('Congrats, you won $' + str(current_win))
        print ('You total $ is ' + str(winnings))
        print(' ')
    else:
        print(variable1 + '     ' + variable2 + '     ' + variable3)
        print('Sorry you lost')
        print ('You total $ is ' + str(winnings))
        print(' ')



'''Create the main function to run the entire program'''
def main():
    '''The default parameter winnings sets the users winnings as 0'''
    winnings = 0
    '''create a default parameter that allows the user to place a bet when the program starts'''
    bet = True
    '''Create a loop that allows the player to play for a longs as they wish to
       that runs the get-bet() and pull() functions and displays the users wins and losses'''
    while bet:
        bet = get_bet()
        outcome = pull()
        current_win = get_pay_multiplier(outcome, bet)
        winnings = winnings + current_win
        if winnings <= 0:
            winnings = 0
        display(outcome, winnings,current_win)

'''Create a function to test 40 runs of the main function'''
def test_main():
    winnings = 0
    count = 0
    flag30seen = False
    flag50seen = False
    while count < 50:
        count = count + 1
        bet = random.randint(1,51)
        print ("Your bet is: $" + str(bet))
        outcome = pull()
        current_win = get_pay_multiplier(outcome, bet)
        winnings = winnings + current_win
        if outcome.to_string() == TripleString("cherries", "cherries", "cherries").to_string():
            flag30seen = True
        if outcome.to_string() == TripleString("BAR", "BAR", "BAR").to_string():
            flag50seen = True
        if winnings <= 0:
            winnings = 0
        display(outcome,winnings, current_win)
    print(flag30seen)
    print(flag50seen)


main()

'''
-------------------------------------
OUTPUT: Running the main() function 10 times
-------------------------------------

Place your bet: 10
Your bet is $10
BAR     BAR     BAR
Congrats, you won $500
You total $ is 500
 
Place your bet: 20
Your bet is $20
cherries     cherries     cherries
Congrats, you won $600
You total $ is 1100
 
Place your bet: 10
Your bet is $10
cherries     BAR     space
Congrats, you won $50
You total $ is 1150
 
Place your bet: 30
Your bet is $30
cherries     cherries     BAR
Congrats, you won $450
You total $ is 1600
 
Place your bet: 50
Your bet is $50
BAR     BAR     7
Sorry you lost
You total $ is 1550
 
Place your bet: 20
Your bet is $20
cherries     cherries     BAR
Congrats, you won $300
You total $ is 1850
 
Place your bet: 10
Your bet is $10
cherries     BAR     cherries
Congrats, you won $50
You total $ is 1900
 
Place your bet: 50
Your bet is $50
BAR     BAR     BAR
Congrats, you won $2500
You total $ is 4400
 
Place your bet: 7
Your bet is $7
cherries     cherries     BAR
Congrats, you won $105
You total $ is 4505
 
Place your bet: 8
Your bet is $8
7     space     cherries
Sorry you lost
You total $ is 4497
 
Place your bet: 0
Game over 
cherries     cherries     cherries
Sorry you lost
You total $ is 4497






'''

test_main()

'''
-------------------------------------
OUTPUT: Running the test() function 
-------------------------------------

Your bet is: $40
7     cherries     cherries
Sorry you lost
You total $ is 0
 
Your bet is: $49
cherries     cherries     BAR
Congrats, you won $735
You total $ is 735
 
Your bet is: $9
cherries     BAR     7
Congrats, you won $45
You total $ is 780
 
Your bet is: $24
cherries     cherries     BAR
Congrats, you won $360
You total $ is 1140
 
Your bet is: $35
BAR     cherries     cherries
Sorry you lost
You total $ is 1105
 
Your bet is: $15
cherries     cherries     BAR
Congrats, you won $225
You total $ is 1330
 
Your bet is: $33
7     BAR     BAR
Sorry you lost
You total $ is 1297
 
Your bet is: $40
BAR     cherries     BAR
Sorry you lost
You total $ is 1257
 
Your bet is: $43
cherries     cherries     7
Congrats, you won $645
You total $ is 1902
 
Your bet is: $43
7     7     7
Congrats, you won $4300
You total $ is 6202
 
Your bet is: $37
cherries     cherries     cherries
Congrats, you won $1110
You total $ is 7312
 
Your bet is: $25
7     cherries     7
Sorry you lost
You total $ is 7287
 
Your bet is: $37
cherries     BAR     BAR
Congrats, you won $185
You total $ is 7472
 
Your bet is: $2
cherries     cherries     BAR
Congrats, you won $30
You total $ is 7502
 
Your bet is: $3
cherries     space     cherries
Congrats, you won $15
You total $ is 7517
 
Your bet is: $16
7     BAR     space
Sorry you lost
You total $ is 7501
 
Your bet is: $2
BAR     cherries     cherries
Sorry you lost
You total $ is 7499
 
Your bet is: $32
BAR     cherries     cherries
Sorry you lost
You total $ is 7467
 
Your bet is: $25
BAR     cherries     BAR
Sorry you lost
You total $ is 7442
 
Your bet is: $12
BAR     7     BAR
Sorry you lost
You total $ is 7430
 
Your bet is: $30
BAR     BAR     7
Sorry you lost
You total $ is 7400
 
Your bet is: $34
cherries     cherries     cherries
Congrats, you won $1020
You total $ is 8420
 
Your bet is: $30
cherries     BAR     cherries
Congrats, you won $150
You total $ is 8570
 
Your bet is: $51
cherries     cherries     cherries
Congrats, you won $1530
You total $ is 10100
 
Your bet is: $20
BAR     BAR     space
Sorry you lost
You total $ is 10080
 
Your bet is: $12
BAR     BAR     BAR
Congrats, you won $600
You total $ is 10680
 
Your bet is: $12
space     cherries     7
Sorry you lost
You total $ is 10668
 
Your bet is: $25
cherries     BAR     cherries
Congrats, you won $125
You total $ is 10793
 
Your bet is: $5
cherries     cherries     BAR
Congrats, you won $75
You total $ is 10868
 
Your bet is: $33
cherries     7     7
Congrats, you won $165
You total $ is 11033
 
Your bet is: $2
BAR     cherries     cherries
Sorry you lost
You total $ is 11031
 
Your bet is: $7
BAR     cherries     BAR
Sorry you lost
You total $ is 11024
 
Your bet is: $22
space     BAR     cherries
Sorry you lost
You total $ is 11002
 
Your bet is: $8
BAR     cherries     cherries
Sorry you lost
You total $ is 10994
 
Your bet is: $5
space     BAR     BAR
Sorry you lost
You total $ is 10989
 
Your bet is: $16
cherries     cherries     BAR
Congrats, you won $240
You total $ is 11229
 
Your bet is: $21
cherries     BAR     cherries
Congrats, you won $105
You total $ is 11334
 
Your bet is: $38
7     cherries     cherries
Sorry you lost
You total $ is 11296
 
Your bet is: $3
BAR     cherries     BAR
Sorry you lost
You total $ is 11293
 
Your bet is: $42
cherries     BAR     7
Congrats, you won $210
You total $ is 11503
 
Your bet is: $51
7     BAR     cherries
Sorry you lost
You total $ is 11452
 
Your bet is: $24
BAR     space     BAR
Sorry you lost
You total $ is 11428
 
Your bet is: $11
cherries     cherries     cherries
Congrats, you won $330
You total $ is 11758
 
Your bet is: $12
cherries     BAR     BAR
Congrats, you won $60
You total $ is 11818
 
Your bet is: $50
BAR     cherries     BAR
Sorry you lost
You total $ is 11768
 
Your bet is: $33
cherries     7     cherries
Congrats, you won $165
You total $ is 11933
 
Your bet is: $8
7     cherries     cherries
Sorry you lost
You total $ is 11925
 
Your bet is: $2
BAR     cherries     BAR
Sorry you lost
You total $ is 11923
 
Your bet is: $8
space     7     cherries
Sorry you lost
You total $ is 11915
 
Your bet is: $12
BAR     BAR     cherries
Sorry you lost
You total $ is 11903
 
True
True




'''
