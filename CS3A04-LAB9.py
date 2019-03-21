'''
ASSIGNMENT NAME: LAB 9: How Fast Benchmark
STUDENT NAME: Sean Cawley
SUBMISSION DATE: March 10, 2019


PART 1:



1.
    a. We want to know how fast Sample Answer 2 runs. - $
        Answer - Rutime = 0.024259090423583984
    b. Make a local copy of Sample Answer 2 - $
    c. Do a test run of Sample Answer 2 without any benchmark code. - $
    d. Check that the Sample Answer 2 app runs perfectly and delivers expected results. - $
        * Hint: always assume there are bugs in any code you are asked to look at.
        *Sample Answer 2 does not print the translations correctly - find the bug and fix it.



2. Find the bug in the program and fix it
    a. Read the source code for Sample Answer #2 - $
       -Complete

    b. Write down the expected output from this code.
        -The expected output of the code is a translated word from in either english, spanish, or greek

    c. Download the 3 data files of 1000 common words. - $
      -Download complete

    d. Run Sample Answer #2, and compare your expected output to the actual output. - $
       ----RUN WITH BUG--------

       dict_language[to][i]
       dict_language[to][i]
       dict_language[to][i]
       dict_language[to][i]
       dict_language[to][i]
       dict_language[to][i]
       The word you want to look up is not in the dictionary.

      ---END RUN WITHOUT BUG -----

    e. The difference is caused by the bug.  Find the bug and correct it  (4 marks) - $

      -ANSWER - The bug was caused by the return('dict_language[to][i]') in the translate() function,
                which returns the string dict_language[to][i] instead of the translated word due to the
                dict_language[to][i] being encased in ' '.

      ----RUN WITHOUT BUG -----

      φως
      luz
      moment
      στιγμή
      multiply
      multiplicar
      The word you want to look up is not in the dictionary.

       ---END RUN WITHOUT BUG------------


'''

'''-------------PART 1 RUN WITH BUG -------------'''

#program with bug

def makeDict(input_file_name):
   with open(input_file_name, 'r', encoding = 'utf-8') as f:
      dict_list = f.readlines()
      index = 0
      while index < len(dict_list):
         dict_list[index] = dict_list[index].rstrip('\n')
         index += 1
   keys = (x for x in range(1,1001))
   return dict(zip(keys, dict_list))

en_dict = makeDict('1kwords.en.txt')
sp_dict = makeDict('1kwords.sp.txt')
gr_dict = makeDict('1kwords.gr.txt')

dict_language = {'en': en_dict, 'sp': sp_dict, 'gr': gr_dict}

def translate(fm, to, word):
   if fm not in dict_language.keys():
      return("from is not a valid language code.")
   elif to not in dict_language.keys():
      return("to not a valid language code.")
   else:
      for i in range(1,1001):
         if fm == to:
            return(word)
         if word not in dict_language[fm].values():
            #print(word)
            #print(dict_language[fm].values())
            return("The word you want to look up is not in the dictionary.")
         if dict_language[fm][i] == word:
            #The bug is located in the return function with returns 'dict_language[to][i]' as a string
            return('dict_language[to][i]')


#use this to test the translate function before the bug is fixed
print(translate("en", "gr", "light"))
print(translate("en", "sp", "light"))
print(translate("sp", "en", "momento"))
print(translate("sp", "gr", "momento"))
print(translate("gr", "en", "πολλαπλασιάστε"))
print(translate("gr", "sp", "πολλαπλασιάστε"))
print(translate("en", "gr", "giraffe"))
print('\n')



'''

-------------PART 1 OUTPUT WITH BUG -------------


dict_language[to][i]
dict_language[to][i]
dict_language[to][i]
dict_language[to][i]
dict_language[to][i]
dict_language[to][i]
The word you want to look up is not in the dictionary.




'''





'''

-------------PART 1 RUN WITHOUT BUG -------------

'''


#program without bug

def makeDict(input_file_name):
   with open(input_file_name, 'r', encoding = 'utf-8') as f:
      dict_list = f.readlines()
      index = 0
      while index < len(dict_list):
         dict_list[index] = dict_list[index].rstrip('\n')
         index += 1
   keys = (x for x in range(1,1001))
   return dict(zip(keys, dict_list))

en_dict = makeDict('1kwords.en.txt')
sp_dict = makeDict('1kwords.sp.txt')
gr_dict = makeDict('1kwords.gr.txt')

dict_language = {'en': en_dict, 'sp': sp_dict, 'gr': gr_dict}

def translate(fm, to, word):
   if fm not in dict_language.keys():
      return("from is not a valid language code.")
   elif to not in dict_language.keys():
      return("to not a valid language code.")
   else:
      for i in range(1,1001):
         if fm == to:
            return( word )
         if word not in dict_language[fm].values():
            return("The word you want to look up is not in the dictionary.")
         if dict_language[fm][i] == word:
            return(dict_language[to][i])


#use this to test run the translate function after the bug is fixed
print(translate("en", "gr", "light"))
print(translate("en", "sp", "light"))
print(translate("sp", "en", "momento"))
print(translate("sp", "gr", "momento"))
print(translate("gr", "en", "πολλαπλασιάστε"))
print(translate("gr", "sp", "πολλαπλασιάστε"))
print(translate("en", "gr", "giraffe"))
print('\n')



'''

-------------PART 1 OUTPUT WITHOUT BUG -------------

φως
luz
moment
στιγμή
multiply
multiplicar
The word you want to look up is not in the dictionary.

'''

'''----END PART 1--------------'''


'''
------
PART 2
------


1.  Modify Sample Answer 2 to add benchmark code. (copying all these pieces from Sample Answer 4). )
   a. After you have Sample Answer 2 running on your PC, add in
      I) the import
      II)  the half dozen statements needed to determine program elapsed times
      III)  the func_to_measure() function


2. Write some tests, and print the output to confirm the code is working correctly so far.

   ----PART 2: OUTPUT--------


   starting timer
   10 words translated in 0.08605490499758162 secs


'''

from timeit import default_timer as timer

def makeDict(input_file_name):
   with open(input_file_name, 'r', encoding = 'utf-8') as f:
      dict_list = f.readlines()
      index = 0
      while index < len(dict_list):
         dict_list[index] = dict_list[index].rstrip('\n')
         index += 1
   keys = (x for x in range(1,1001))
   return dict(zip(keys, dict_list))

en_dict = makeDict('1kwords.en.txt')
sp_dict = makeDict('1kwords.sp.txt')
gr_dict = makeDict('1kwords.gr.txt')

dict_language = {'en': en_dict, 'sp': sp_dict, 'gr': gr_dict}

def translate(fm, to, word):
   if fm not in dict_language.keys():
      return("from is not a valid language code.")
   elif to not in dict_language.keys():
      return("to not a valid language code.")
   else:
      for i in range(1,1001):
         if fm == to:
            return( word )
         if word not in dict_language[fm].values():
            return("The word you want to look up is not in the dictionary.")
         if dict_language[fm][i] == word:
            return(dict_language[to][i])



def func_to_measure():
   spbee = translate("gr", "sp", "μέλισσα")
   translate("sp", "en", spbee)
   translate("en", "sp", "heart")
   translate("en", "gr", "heart")
   translate("en", "gr", "diegetic")
   translate("gr", "en", "μέλισσα")
   spneck = translate("en", "sp", "neck")
   translate("en", "gr", "neck")
   translate("sp", "gr", spneck)
   translate("en", "sp", "beauty")


#tests to confirm the output is working
print("starting timer")
start = timer()
func_to_measure()
end = timer()

elapsed = end - start
print("10 words translated in", elapsed, "secs")


'''
----PART 2: OUTPUT--------


starting timer
10 words translated in 0.08605490499758162 secs



'''

'''---END PART 2----------'''



'''
------
PART 3
------

1. Then benchmark Sample Answer 2, to find out how quickly it can process 10 thousand translations.

2. You will make the Sample Answer 2 app call the func_to_measure() function one thousand times in a loop.

3. Each loop iteration does 10 translations, so overall, 10 thousand translations are done.  (10 marks)

   ----PART 3: OUTPUT --------

   starting timer
   10,000 words translated in 81.91925943100068 secs

'''




from timeit import default_timer as timer

def makeDict(input_file_name):
   with open(input_file_name, 'r', encoding = 'utf-8') as f:
      dict_list = f.readlines()
      index = 0
      while index < len(dict_list):
         dict_list[index] = dict_list[index].rstrip('\n')
         index += 1
   keys = (x for x in range(1,1001))
   return dict(zip(keys, dict_list))

en_dict = makeDict('1kwords.en.txt')
sp_dict = makeDict('1kwords.sp.txt')
gr_dict = makeDict('1kwords.gr.txt')

dict_language = {'en': en_dict, 'sp': sp_dict, 'gr': gr_dict}

def translate(fm, to, word):
   if fm not in dict_language.keys():
      return("from is not a valid language code.")
   elif to not in dict_language.keys():
      return("to not a valid language code.")
   else:
      for i in range(1,1001):
         if fm == to:
            return( word )
         if word not in dict_language[fm].values():
            return("The word you want to look up is not in the dictionary.")
         if dict_language[fm][i] == word:
            return(dict_language[to][i])


def func_to_measure():
   spbee = translate("gr", "sp", "μέλισσα")
   translate("sp", "en", spbee)
   translate("en", "sp", "heart")
   translate("en", "gr", "heart")
   translate("en", "gr", "diegetic")
   translate("gr", "en", "μέλισσα")
   spneck = translate("en", "sp", "neck")
   translate("en", "gr", "neck")
   translate("sp", "gr", spneck)
   translate("en", "sp", "beauty")



print("starting timer")
start = timer()
for i in range(1000):
    func_to_measure()
end = timer()

elapsed = end - start
print("10,000 words translated in", elapsed, "secs")


'''
----PART 3: OUTPUT --------

starting timer
10,000 words translated in 81.91925943100068 secs


'''



'''-------END PART 3----------'''




'''
PART 4:


QUESTIONS AND ANSWERS


1. Make sure that Sample Answer 2 can translate 9 of the 10 words given in func_to_measure
   a. Prove this by printing out the translations in a test run which is included and
      labelled in your submitted answer.
   b. Don't do any printing in your performance test runs
   c. Comment out the print statement(s) before benchmarking.


2. Relate the speed results to the speed results from Sample Answer 4.
   a. Why is one app faster or slower, and by how much?
      -----------
      Answer to A
      -----------
      I. The difference in run time is because Sample Answer 2 doesn't use a dictionary for fast access
      II. #Speed results from Performance test run of Sample Answer 2
         starting timer
         10,000 words translated in 81.33077845699154 secs


         #Speed results from Performance test run of Sample Answer 4
         starting timer
         10M words translated in 3.0607449309900403 secs

         Sample Answer 4 - Sample Answer 2 = 78.2700335260015 secs difference



   b. Write a couple of paragraphs of English text analyzing the performance and
      explaining speed differences, embedded in a doc string at the end of your file

      ------------
      Answer to B:
      ------------

      The performance of test run of Sample Answer 2 is 78.2700335260015 longer than that of
      the performance run of Sample Answer 4.


      Sample Answer 2 design choice eliminates the performance advantage of dictionaries by assigning the key as the
      index instead of the word and uses a linear search to look up each word.  This code will have
      performance problems when scaling up to thousands of words.


      Sample Answer 4 meanwhile assigns the value of a given word in each dictionary to all of the translations
      of that word in each of the three languages. This cuts down on the performance time.

      The program in Sample Answer 4 also cuts down the code significantly, by the use of aliases to simplify
      some of the references.



'''

from timeit import default_timer as timer



def makeDict(input_file_name):
   with open(input_file_name, 'r', encoding = 'utf-8') as f:
      dict_list = f.readlines()
      index = 0
      while index < len(dict_list):
         dict_list[index] = dict_list[index].rstrip('\n')
         index += 1
   keys = (x for x in range(1,1001))
   return dict(zip(keys, dict_list))

en_dict = makeDict('1kwords.en.txt')
sp_dict = makeDict('1kwords.sp.txt')
gr_dict = makeDict('1kwords.gr.txt')

dict_language = {'en': en_dict, 'sp': sp_dict, 'gr': gr_dict}

def translate(fm, to, word):
   if fm not in dict_language.keys():
      return("from is not a valid language code.")
   elif to not in dict_language.keys():
      return("to not a valid language code.")
   else:
      for i in range(1,1001):
         if fm == to:
            return( word )
         if word not in dict_language[fm].values():
            return("The word you want to look up is not in the dictionary.")
         if dict_language[fm][i] == word:
            return(dict_language[to][i])



#Program test of 10 translations
print(translate("en", "gr", "light"))
print(translate("en", "sp", "light"))
print(translate("en", "sp", "bee"))
print(translate("sp", "en", "momento"))
print(translate("sp", "gr", "momento"))
print(translate("sp", "en", "hizo"))
print(translate("gr", "en", "πολλαπλασιάστε"))
print(translate("gr", "sp", "πολλαπλασιάστε"))
print(translate("gr", "en", "είναι"))
print(translate("en", "gr", "diegetic"))

print('\n')



def func_to_measure():
   spbee = translate("gr", "sp", "μέλισσα")
   translate("sp", "en", spbee)
   translate("en", "sp", "heart")
   translate("en", "gr", "heart")
   translate("en", "gr", "diegetic")
   translate("gr", "en", "μέλισσα")
   spneck = translate("en", "sp", "neck")
   translate("en", "gr", "neck")
   translate("sp", "gr", spneck)
   translate("en", "sp", "beauty")


#Perfomance test
print("starting timer")
start = timer()
for i in range(1000):
    func_to_measure()
end = timer()

elapsed = end - start
print("10,000 words translated in", elapsed, "secs")


'''

----PART 4 OUTPUT-----
#Program test run without performance test
φως
luz
abeja
moment
στιγμή
that
multiply
multiplicar
is
The word you want to look up is not in the dictionary.



#Performance test run of Sample Answer 2  without the program test
starting timer
10,000 words translated in 81.33077845699154 secs



'''



'''------END PART 4---------'''


