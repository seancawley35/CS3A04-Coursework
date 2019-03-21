'''---------------CS3A04: LAB 7--------------------'''

'''---------------CODE------------------------------'''

'''No user input should be done in this program'''

# 1. Create a class called TripleString

class TripleString:
    # Class level constants
    MIN_LEN = 1
    MAX_LEN = 50
    DEFAULT_STRING = "Ready, Steady, Go"

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
        print (master_string)



# Client

# 1. Create 4 TripleString objects
print ("#1 Create 4 TripleString objects")
triple_string_num_1 = TripleString() # Use defaults
triple_string_num_2 = TripleString("And the Raven", "never flitting", "still is sitting") # Different values for all strings
triple_string_num_3 = TripleString("Only the first string is not a default") # One string
triple_string_num_4 = TripleString("One", "Two", "Three")


#2. Immediately display all objects.
print ("\n")
print ("#2 Display all objects:")
print( ""
       .format(triple_string_num_1.to_string(),
                triple_string_num_2.to_string(),
                triple_string_num_3.to_string(),
                triple_string_num_4.to_string(),
                ))


#3. Mutate one or more attributes of every object.
print ("\n")
print ("#3. Mutate one or more attributes of every object")

# Set strings 1 and 2 for first object
triple_string_num_1.set_string1("And my soul from out that shadow ")
triple_string_num_1.set_string2("La la la")

# Set string 2 for second object
triple_string_num_2.set_string2('that lies floating on the floor')

# Set string 1 for third object
triple_string_num_3.set_string1("Shall be lifted")

#Set string 1 and 3 for fourth object
triple_string_num_4.set_string1("Adding another string")
triple_string_num_4.set_string3("nevermore")


#4.Display all objects a second time.
print ("\n")
print ("#4. Display all objects")
print( ""
       .format(triple_string_num_1.to_string(),
                triple_string_num_2.to_string(),
                triple_string_num_3.to_string(),
                triple_string_num_4.to_string(),
                ))


#5. Mutator tests
print ("\n")
print ("#5. Mutator tests:")

# Should succeed
if triple_string_num_1.set_string1("And the Raven"):
    print ("Success")
else:
    print ("Fail")

# Should fail
if triple_string_num_2.set_string1(""):
    print ("Success")
else:
    print ("Fail")

#6. Make two accessor calls to demonstrate that they work.
print ("\n")
print ("#6.  Two accessor calls")
print ("Object 1, string 1:")
print (triple_string_num_1.get_string1())
print ("Object 2, string 3: ")
print (triple_string_num_2.get_string3())




'''
------------------OUTPUT----------------------------------

#1 Create 4 TripleString objects


#2 Display all objects:
strings are:
	Ready, Steady, Go
	Ready, Steady, Go
	Ready, Steady, Go

strings are:
	And the Raven
	never flitting
	still is sitting

strings are:
	Only the first string is not a default
	Ready, Steady, Go
	Ready, Steady, Go

strings are:
	One
	Two
	Three




#3. Mutate one or more attributes of every object


#4. Display all objects
strings are:
	And my soul from out that shadow 
	La la la
	Ready, Steady, Go

strings are:
	And the Raven
	that lies floating on the floor
	still is sitting

strings are:
	Shall be lifted
	Ready, Steady, Go
	Ready, Steady, Go

strings are:
	Adding another string
	Two
	nevermore




#5. Mutator tests:
Success
Fail


#6.  Two accessor calls
Object 1, string 1:
And the Raven
Object 2, string 3: 
still is sitting



'''
