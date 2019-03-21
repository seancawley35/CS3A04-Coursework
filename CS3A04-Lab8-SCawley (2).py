Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 



'''--------SOURCE-------------------'''


#import the random function
import random


# 1. Create a class called TripleString

class TripleString:
    # Class level constants
    MIN_LEN = 1
    MAX_LEN = 50
    #DEFAULT_STRING = "cherries", "bar", "7", "space"
    DEFAULT_STRING = 'none'

    #Create the constructor method
    def __init__(self, string1 = DEFAULT_STRING, string2 = DEFAULT_STRING, string3 = DEFAULT_STRING):
        # class-defined instance attributes (attributes)
        self.string1 = string1
        self.string2 = string2
        self.string3 = string3

    # mutator ("Set") methods
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

    # Accessor ("Set") methods
    def get_string1(self):
        return self.string1

    def get_string2(self):
        return self.string2

    def get_string3(self):
        return self.string3

    # Helper methods
    def valid_string(self, string_to_set):
        if len(string_to_set) < 1 or len(string_to_set) > 50:
            return False
        else:
            return True

    def to_string(self):
        master_string = ("strings are:\n\t{}\n\t{}\n\t{}\n".format(self.string1, self.string2, self.string3) )
        return master_string






#Constant for the slot wheels:
wheel_options = ["cherries","BAR","7","space"]



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


#create a function for the user to pull the lever and return TripleString()
#with three random slot characters
def pull():
    wheels = TripleString()
    wheels.set_string1(rand_string())
    wheels.set_string2(rand_string())
    wheels.set_string3(rand_string())
    return wheels



#create a function that returns a random string of three characters from the pull function
def rand_string():
    #create an object that creates a random integer between 0 - 100
    rand_int = random.randrange(0,101)
    #return the string "cherries" if the number is between 0 - 40
    if rand_int in range(0,41):
        return ("cherries")
    # return the string "BAR" if the number is between 41 - 78
    elif rand_int in range(41,79):
        return ("BAR")
    # return the string "7" if the number is between 79 - 93
    elif rand_int in range(79, 94):
        return ("7")
    # return the string "space" if the number is between 0 - 40
    elif rand_int in range(94, 101):
        return ("space")



# #create a function for the payout of the returned slot figures from the play
def get_pay_multiplier(wheels, bet):
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


#display the three strings inside reels along with "sorry - you lost" or "congrats, you won $X."
def display(reels, winnings, current_win):
    global stake
    variable1 = reels.get_string1()
    variable2 = reels.get_string2()
    variable3 = reels.get_string3()
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



#create the main function to run the entire program
def main():
    winnings = 0
    bet = True
    while bet:
        bet = get_bet()
        outcome = pull()
        current_win = get_pay_multiplier(outcome, bet)
        winnings = winnings + current_win
        if winnings <= 0:
            winnings = 0
        display(outcome, winnings,current_win)

#create a function to test 40 runs of the main function
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
OUTPUT main()

Place your bet: -2
Invalid bet
Place your bet: -4
Invalid bet
Place your bet: 10
Your bet is $10
7     BAR     BAR
Sorry you lost
You total $ is 0

Place your bet: 9
Your bet is $9
BAR     space     7
Sorry you lost
You total $ is 0

Place your bet: 25
Your bet is $25
BAR     BAR     cherries
Sorry you lost
You total $ is 0

Place your bet: 40
Your bet is $40
7     cherries     BAR
Sorry you lost
You total $ is 0

Place your bet: 10
Your bet is $10
BAR     space     cherries
Sorry you lost
You total $ is 0

Place your bet: 30
Your bet is $30
cherries     7     BAR
Congrats, you won $150
You total $ is 150

Place your bet: 7
Your bet is $7
BAR     cherries     7
Sorry you lost
You total $ is 143

Place your bet: 0
Game over
BAR     cherries     cherries
Sorry you lost
You total $ is 143




'''





test_main()


'''
OUTPUT test_main()

Your bet is: $16
BAR     BAR     7
Sorry you lost
You total $ is 0
 
Your bet is: $2
7     cherries     cherries
Sorry you lost
You total $ is 0
 
Your bet is: $14
cherries     BAR     BAR
Congrats, you won $70
You total $ is 70
 
Your bet is: $37
cherries     cherries     BAR
Congrats, you won $555
You total $ is 625
 
Your bet is: $34
7     cherries     space
Sorry you lost
You total $ is 591
 
Your bet is: $1
cherries     cherries     cherries
Congrats, you won $30
You total $ is 621
 
Your bet is: $51
7     BAR     cherries
Sorry you lost
You total $ is 570
 
Your bet is: $26
7     space     cherries
Sorry you lost
You total $ is 544
 
Your bet is: $50
cherries     cherries     cherries
Congrats, you won $1500
You total $ is 2044
 
Your bet is: $31
cherries     BAR     BAR
Congrats, you won $155
You total $ is 2199
 
Your bet is: $4
BAR     space     cherries
Sorry you lost
You total $ is 2195
 
Your bet is: $21
cherries     cherries     BAR
Congrats, you won $315
You total $ is 2510
 
Your bet is: $32
BAR     cherries     BAR
Sorry you lost
You total $ is 2478
 
Your bet is: $39
BAR     BAR     BAR
Congrats, you won $1950
You total $ is 4428
 
Your bet is: $32
cherries     cherries     7
Congrats, you won $480
You total $ is 4908
 
Your bet is: $2
cherries     cherries     space
Congrats, you won $30
You total $ is 4938
 
Your bet is: $11
space     cherries     BAR
Sorry you lost
You total $ is 4927
 
Your bet is: $50
cherries     BAR     7
Congrats, you won $250
You total $ is 5177
 
Your bet is: $30
BAR     BAR     cherries
Sorry you lost
You total $ is 5147
 
Your bet is: $32
cherries     7     cherries
Congrats, you won $160
You total $ is 5307
 
Your bet is: $14
BAR     cherries     cherries
Sorry you lost
You total $ is 5293
 
Your bet is: $36
7     BAR     cherries
Sorry you lost
You total $ is 5257
 
Your bet is: $12
cherries     cherries     cherries
Congrats, you won $360
You total $ is 5617
 
Your bet is: $8
cherries     7     BAR
Congrats, you won $40
You total $ is 5657
 
Your bet is: $38
cherries     BAR     7
Congrats, you won $190
You total $ is 5847
 
Your bet is: $26
cherries     cherries     7
Congrats, you won $390
You total $ is 6237
 
Your bet is: $20
cherries     BAR     BAR
Congrats, you won $100
You total $ is 6337
 
Your bet is: $17
cherries     space     cherries
Congrats, you won $85
You total $ is 6422
 
Your bet is: $30
7     BAR     7
Sorry you lost
You total $ is 6392
 
Your bet is: $16
cherries     cherries     BAR
Congrats, you won $240
You total $ is 6632
 
Your bet is: $47
cherries     7     7
Congrats, you won $235
You total $ is 6867
 
Your bet is: $26
BAR     7     space
Sorry you lost
You total $ is 6841
 
Your bet is: $18
cherries     cherries     BAR
Congrats, you won $270
You total $ is 7111
 
Your bet is: $31
cherries     BAR     BAR
Congrats, you won $155
You total $ is 7266
 
Your bet is: $17
cherries     cherries     space
Congrats, you won $255
You total $ is 7521
 
Your bet is: $30
7     cherries     BAR
Sorry you lost
You total $ is 7491
 
Your bet is: $33
BAR     BAR     7
Sorry you lost
You total $ is 7458
 
Your bet is: $10
cherries     BAR     cherries
Congrats, you won $50
You total $ is 7508
 
Your bet is: $39
BAR     BAR     space
Sorry you lost
You total $ is 7469
 
Your bet is: $32
cherries     BAR     BAR
Congrats, you won $160
You total $ is 7629
 
Your bet is: $44
BAR     BAR     BAR
Congrats, you won $2200
You total $ is 9829
 
Your bet is: $17
BAR     cherries     cherries
Sorry you lost
You total $ is 9812
 
Your bet is: $48
BAR     space     7
Sorry you lost
You total $ is 9764
 
Your bet is: $25
BAR     cherries     space
Sorry you lost
You total $ is 9739
 
Your bet is: $40
BAR     BAR     cherries
Sorry you lost
You total $ is 9699
 
Your bet is: $36
7     BAR     7
Sorry you lost
You total $ is 9663
 
Your bet is: $2
BAR     7     BAR
Sorry you lost
You total $ is 9661
 
Your bet is: $39
BAR     BAR     cherries
Sorry you lost
You total $ is 9622
 
Your bet is: $37
BAR     BAR     BAR
Congrats, you won $1850
You total $ is 11472
 
Your bet is: $1
cherries     space     BAR
Congrats, you won $5
You total $ is 11477
 
True
True


'''


