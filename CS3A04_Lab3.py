'''CS3A04 Lab 3'''

#PART 1: Lists
'''-----------------Source-------------------------------------------'''
# program that returns dir () on the class 'list'
print (dir(list))




'''-------------------RUN-----------------------------

/Users/scawley/PycharmProjects/CS3A04/venv/bin/python "
/Users/scawley/Library/Preferences/PyCharmCE2018.3/scratches/CS3A04_Lab 3.py"
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
 '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
 '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
  '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear',
 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

 '''



#PART 2: Loops


'''---------------SOURCE-----------------------------------'''



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 8, 7, 5, 9, 10, 11, 34, 12, 13]

#check each element in the first list A
for x in a:
    #compare the elements in list A to the elements in list b
    if x in b:
        #return any matching element from list a and list b
        print (x)

'''---------------RUN-------------------------------------------


1
1
2
3
5
8
13
34
'''



# PART 3: Nested Lists

'''--------------SOURCE-----------------------------------------------'''



#First Item
'''  For each film title, make one list.
  The list name must match the film'''

#Second Item
'''The second item on the list will be a nested list.
The items in the nested list will be the three actors in each film.'''

#create a list for each film with a nested list within the film
dogs_purpose = ['Dogs Purpose', ['Buddie', 'Margot Robbie', 'Carrie Fisher']]
star_wars = ['Star Wars',['Mark Hamill','Harrison Ford', 'Carrie Fisher']]
Iam_legend= ['I am Legend',['Kona', 'Will Smith', 'Carrie Fisher']]
suicide_squad = ['Suicide Squad', ['Viola Davis', 'Margot Robbie', 'Will Smith']]



#Third Item
'''  Make a top level list called movies
with the four movies in them  '''

#create a list containing movies with all 4 movie lists
movies = [dogs_purpose, star_wars, Iam_legend, suicide_squad]



#Write some code to process the following

# create three empty lists to store the movies each actress is in
cf_films = []; no_vdavis_films = []; mr_no_of_films = []
#go through each movie in the list movie
for movie in movies:
    #store the title of the movie in a new variable
    movie_name = movie[0]
    #store the cast list of of each movie in a new variable
    cast = movie[1]

#check each movie for each actress.  If the actress is in the movie, add it to their list
    if 'Carrie Fisher' in cast:
        cf_films.append(movie_name)
    if 'Margot Robbie' in cast and "Viola Davis" not in cast:
        mr_no_of_films.append(movie_name)
    if "Viola Davis" not in cast:
        no_vdavis_films.append(movie_name)


#1.  Print the titles of movies Carrie Fisher is in


print ('Movies Carrie Fisher is in:',  '\n', '\n'.join(cf_films), '\n','\n')


#2.  Print the titles of movies Viola Davis is not in


print ('Movies Viola Davis is not in:', '\n', '\n'.join(no_vdavis_films),'\n','\n')



#3.  Print the name of movies Margot Robbie is in, but not Carrie Fisher



print ("Movies that Margot Robbie is in that Viola Davis is not in:",'\n','\n'.join(mr_no_of_films),'\n')


'''--------------RUN---------------------------------------



Movies Carrie Fisher is in:
Star Wars
I am Legend
Dogs Purpose

Movies Viola Davis is not in:
Star Wars
I am Legend
Dogs Purpose

Movies that Margot Robbie is in that Viola Davis is not in:
Dogs Purpose
'''
