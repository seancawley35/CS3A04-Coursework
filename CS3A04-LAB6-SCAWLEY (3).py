Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''-----------------LAB 6--------------------------'''



'''----------------PART 1-------------------------'''


'''
-----------------PART 1: CODE------------------------
'''

# import the math function to use sqrt in the function
import math

#create a function to determine if two balls are colliding
def isColliding(a,b):
    #create variables that determine the distance between two objects
    c = ((a[0] - b[0])**2)
    d = ((a[1] - b[1])**2)
    e = (c + d)
    #create a variable to check the sqrt of variable e
    distance = math.sqrt(e)
    #create a variable to determine the radii of both objects
    combined_radii = (a[2] + b[2])
    #check if the distance between both objects is less than the radii
    if distance <= combined_radii:
        #return True if the distance is objects are colliding
        return True
    #return False if the if the objects are not colliding
    else:
        return False



#circle = (x_a, y_a, r_a)
a = (3, -4,0)
#circle = (x_b, y_b, r_b)
b = (-1,3,0)

#use a variable to run the function
state = isColliding(a,b)
#print the result of the function
print(state)



'''
-----------------PART 1: OUTPUT-------------------------------
False



'''


'''------------------PART 2-------------------------------'''

'''
------------------PART 2: CODE-----------------------------
'''

# set up a list to iterate on
myCheeseList = ["Apple", "Asiago", "Brie", "Caerphilly", "Emmental", "Gloucester", "Gouda", ]

for i in range(len(myCheeseList)):

    if i == 2:
        del (myCheeseList[4])

    print(i, myCheeseList[i])


'''
---------------------PART 2: OUTPUT--------------------------------

Traceback (most recent call last):
0 Apple
1 Asiago
  File "/Users/scawley/Library/Preferences/PyCharmCE2018.3/scratches/I/test i/scratch.py", line 9, in <module>
2 Brie
    print(i, myCheeseList[i])
3 Caerphilly
IndexError: list index out of range
4 Gloucester
5 Gouda


#My Answer:

Elements of a list can not change while iterating over the list with a for loop.
To properly change the elements of a list,use a while loop because len(myCheeseList)
recalculates each time around the loop

The error occurs because the loop is trying to access myCheeseList[4] at the end of the list
which used to be the value Gloucestor. After the value Emmental is deleted, myCheeseList[4]
is deleted from the list.


If you append an item to your list while running the for loop,
the loop will not process them because the range iterator
functions on the length of your list when the for loop begins.



'''


'''--------------PART 3 ----------------------------------'''


'''
--------------PART 3: FILES---------------------------------

Fact 1: Opening a file

Opening the file communicates with your operating system, which
knows where the data for each file is stored.  When you open a file,
you are asking the operating system to find the file by name and
make sure the file exists. If the file does not exist, open will fail
with a traceback and you will not get a handle to access the contents
of the file


Fact 2: Searching through a file

When you are searching through data in a file, it is a very common pattern
to read through a file, ignoring most of the lines and only processing lines
which meet a particular condition.  The basic idea of the search loop is that
you are looking for “interesting” lines and effectively skipping “uninteresting”
lines.


'''


'''

--------------PART 3: DICTIONARIES-----------------------------

Fact 1: Get Method


Dictionaries have a method called get that takes a key and a default value.
If the key appears in the dictionary, get returns the corresponding value;
otherwise it returns the default value.


Fact  2: Dictionaries and Files

One of the common uses of a dictionary is to count the occurrence of words in
a file with some written text.

'''



'''

--------------PART 3: TUPLES-----------------------------------

Fact 1: Tuples are immutable

A tuple1 is a sequence of values much like a list. The values stored in a tuple
can be any type, and they are indexed by integers. The important difference is
that tuples are immutable. Tuples are also comparable and hashable so we can sort
lists of them and use tuples as key values in Python dictionaries.


Fact  2: Comparing tuples


The comparison operators work with tuples and other sequences. Python starts by
comparing the first element from each sequence.  If they are equal, it goes on
to the next element, and so on, until it finds elements that differ. Subsequent
elements are not considered (even if they are really big).
'''


'''-----------PART 4-----------------------------------'''


'''
--------------PART 4: CODE--------------------------------
'''


#create a dictionary that stores words in english, spanish, and greek
animal_names = {
    "en" :{
        "bee": {
            "sp": "abeja", "gr":"μέλισσα"
        },
        "iguana":{
             "sp":'iguana', "gr":'ιγκουάνα'
        },
        "scorpion" :{
             "sp":'alacrán', "gr": 'σκορπιός'
        },
         "giraffe":{
            "sp":'jirafa', "gr": 'καμηλοπάρδαλη'
         },
          "spider": {
            "sp": 'araña', "gr": 'αράχνη'
        }
    },
    "sp" :{
        "abeja": {
            "en": "bee", "gr":"μέλισσα"
        },
        "iguana":{
            "en": 'iguana', "gr": 'ιγκουάνα'
        },
        "alacrán":{
            "en": 'scorpion', "gr": 'σκορπιός'
        },
        "jirafa":{
            "en": 'giraffe', "gr": 'καμηλοπάρδαλη'
        },
        "araña":{
            "en": 'spider', "gr": 'αράχνη'
        }

    },
    "gr": {
        "μέλισσα" : {
            "en": "bee","sp": "abeja"
        },
    "ιγκουάνα":{
          "en": 'iguana', "sp": 'iguana'
        },
    "σκορπιός":{
          "en": 'scorpion', "sp":'alacrán'

    },
    "καμηλοπάρδαλη":{
          "en": 'giraffe', "sp": 'jirafa'
    },
    "αράχνη":{
           "en": 'spider', "sp": 'araña'
    }

    }
}


#create a dictionary that stores spanish translations of english words
spanish_names = {'bee': 'abeja', 'iguana': 'iguana', 'scorpion': 'alacrán', 'giraffe': 'jirafa', 'spider':'araña'}

#Part II
#create the the function translate(word) for converting english words to spanish
def translate(word):
    #check if the english word exists in the dictionary
    if word in spanish_names:
        #if the word is in the dictionary, return the spanish translation
        print (spanish_names[word])
    #if the word does not exist in the dictionary, return an empty string
    else:
        print ('')

#run four successful test cases of the function
translate('bee')
translate('iguana')
translate('giraffe')
translate('scorpion')
#test one unsuccessful test case with the word 'flea' not in dictionary
translate('flea')

print ('\n')



#create a function that translates words from dictionaries in english, spanish, and greek
def translate(fm, to, word):
    #check if the word exists in the input dictionary
    if word in animal_names[fm]:
        #if the word exists in the fm dictionary, return the to translation of the word
        print(animal_names[fm][word][to])
    #if the word does not exist in the fm dictionary, return an empty string
    else:
        print('')


#run ten successful and one unsuccessful test cases of the function
translate('en','sp','bee')
translate('sp', 'gr','iguana')
translate('gr', 'en', 'σκορπιός')
translate('en', 'gr', 'giraffe')
translate('sp','en','araña')
translate('gr','sp','μέλισσα')
translate('en','sp','spider')
translate('gr','en','ιγκουάνα')
translate('en','gr','scorpion')
translate('sp','gr','abeja')
#non-existent word
translate('gr', 'sp', 'dog')


'''
------------------PART 4: OUTPUT-----------------------

abeja
iguana
jirafa
alacrán



abeja
ιγκουάνα
scorpion
καμηλοπάρδαλη
spider
abeja
araña
iguana
σκορπιός
μέλισσα






'''



'''-----------------PART 5---------------------'''

'''-----------------PART 5: CODE-----------------'''


# create a function to read the english, spanish, and german word files
def transfer_words(file_name):
    # use an empty list to store all three files
    word_list = []
    try:
        # open each word file
        with open(file_name, "r", encoding='utf-8') as f:
            # add all of the words to the in each file to the list
            for next in f:
                word_list.append(next.strip())
    # if the words do not exist, return except
    except:
        print('except')
    # return the list of words
    return word_list


# create a function to hold each file of words in English, Spanish, and Greek

def create_dictionary():
    # create variables to hold each file of words in English, Spanish, and Greek
    en_words = transfer_words('1kwords.en.txt')
    sp_words = transfer_words('1kwords.sp.txt')
    gr_words = transfer_words('1kwords.gr.txt')

    giant_dictionary = {'en': {}, 'sp': {}, 'gr': {}}

    # check for words in the English dictionary and add there translations from the other two dictionaries
    for i, word in enumerate(en_words):
        giant_dictionary['en'][word] = {'sp': sp_words[i], 'gr': gr_words[i]}

    # check for words in the Spanish dictionary and add there translations from the other two dictionaries
    for j, word in enumerate(sp_words):
        giant_dictionary['sp'][word] = {'en': en_words[i], 'gr': gr_words[i]

        # check for words in the Greek dictionary and add there translations from the other two dictionaries
        for k, word in enumerate(gr_words):
            giant_dictionary['gr'][word] = {'en': en_words[i], 'sp': sp_words[i]}

            # return the new dictionary that contains all three word dictionaries
    return giant_dictionary


all_words = create_dictionary()


# create a function that translates words from dictionaries in english, spanish, and greek
def translation(frm, too, word):
    # check if the word exists in the input dictionary
    if word in all_words[frm]:
        # if the word exists in the fm dictionary, return the to translation of the word
        print(all_words[frm][word][too])
    # if the word does not exist in the fm dictionary, return an empty string
    else:
        print('')


# test four cases of the program
translation('en', 'sp', 'man')
translation('en', 'sp', 'this')
translation('en', 'sp', 'is')
translation('en', 'sp', 'dog')

'''
----------PART 5: OUTPUT----------------------------

usted
este
es
perro



'''
