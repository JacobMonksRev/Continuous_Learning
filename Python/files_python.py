# #### PYTHON FUNDAMENTALS

# ## CONTROL FLOW STATEMENTS
# # IF-ELSE STATEMENT
# x = 20
# if x == 10:
#     print(x)
#     print('X is equal to 10.')
# elif x == 13:
#     print('X is equal to 13.')
# else:
#     print('X is not equal to 10 or 13.')

# # WHILE LOOP
# x = 0
# while x < 10:
#     print(x)
#     x += 1

# # FOR LOOP
# for x in range(10,20):
#     print(x)

# ## FUNCTIONS
# def my_function():
#     print("This function is running.")

# def my_second_function(x):
#     for num in range(x):
#         print(num)

# def my_third_function(a = 0,b = 4):
#     return a + b

# def my_variable_function(*args):
#     for word in args:
#         print(word)

# my_variable_function(1,2,3,4)
# my_variable_function(1,2,3,4,5,6,7)

# # LAMBDAS
# lambda a, b : a + b

# def addition(x):
#     return lambda a : a + x

# add5 = addition(5)
# print(add5(8))

# # GENERATOR
# def my_gen(x):
#     value = 0
#     for i in range(x):
#         value += i
#         yield value

# x = my_gen(10)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

## PYTHON BUILT-IN COLLECTIONS
# List, Set, Tuple, Dictionary

## LISTS
# lst_fruits = ['apple','orange','banana','grape']
# lst_multiple_types = ['Jacob',45.8, 90, False]

# for item in lst_fruits:
#     print(item)

# print(lst_fruits)
# lst_fruits.append('melon')
# print(lst_fruits)
# lst_fruits.extend(lst_multiple_types)
# print(' '.join(map(lambda a : str(a),lst_fruits)))

# lst_nest = [['Jacob','Monks',2021], ['Bob','Ross',1977],['George','Lucas',1968]]
# print(lst_nest[2][0])

# print(lst_fruits[3:0:-1])

## SETS
# set_fruits = {'apple','banana','lemon','banana'}
# print(set_fruits)

# for item in set_fruits:
#     print(item)

# set_fruits_2 = {'grape','orange','blueberry','lemon'}
# print(set_fruits.union(set_fruits_2))
# print(set_fruits.intersection(set_fruits_2))
# print(set_fruits_2.difference(set_fruits))

## TUPLE
# my_tuple = ('Jacob','Bob','Maria')

# def calc(a,b):
#     return (a+b,a-b,a*b,a/b)

# x = calc(10,5)

## DICTIONARY
# my_dictionary = {'name':'Jacob','job':'trainer'}
# print(my_dictionary['name'])
# for k,v in my_dictionary.items():
#     print(k,v)

# x = int(input("Please input a number: "))
# y = int(input("Please input another number: "))
# print(calc(x,y))

## STRINGS
# mystr = 'this is a string'
# print(mystr[2])
# for word in mystr.split():
#     print(word)
# mystr2 = "    Hello    \n   "
# print(mystr2.strip())
# print(mystr + mystr2)

## FILE HANDLING
# myfile = open('test.txt')
# counter = 0
# for line in myfile:
#     counter += len(line.split())
# print(counter)

# import csv

# mycsv = open('csvfile.csv')
# csvfile = csv.reader(mycsv)
# fields = []
# rows = []
# fields = next(csvfile)
# print('\t'.join(fields))
# for row in csvfile:
#     rows.append(row)

# for row in rows:
#     print('\t'.join(row))
# mycsv.close()

## EXCEPTIONS PYTHON

# try:
#     myfile = open('textfile.txt','r')
# except FileNotFoundError:
#     print("The File could not be found.")
# else:
#     for line in myfile:
#         print(line)
# finally:
#     myfile.close()

# import abc
# from abc import abstractmethod

# class Person:
#     isHuman = True
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def action(self):
#         print(self.name,"Goes for a walk.")
#     @abstractmethod
#     def go_to_office(self):
#         pass

# class Employee(Person):
#     def action(self,salary,department):
#         print(self.name,"works for the",department,"department and makes",salary,"per year.")

# Bob = Employee('Bob',40,'M')

# print(Bob.action(50000,'HR'))

# class Shapes:
#     def __init__(self,name,sides):
#         self.name = name
#         self._sides = sides
#     @abstractmethod
#     def number_of_sides(self):
#         pass

# class Square(Shapes):
#     def number_of_sides(self):
#         print("This",self.name,"has",self.sides,"sides.")

# shape1 = Shapes("square1",4)
# print(shape1._sides)

## EXERCISE 1

myfile = open('input.txt','r')
my_dictionary = {}
punctuation = [',',':',';',"!",'?','.',"'",'-']
for line in myfile:
    words = line.split()
    for word in words:
        for item in punctuation:
            word = word.strip(item).lower()
        if word in my_dictionary:
            value = my_dictionary.get(word) + 1
            my_dictionary[word] = value
        else:
            my_dictionary[word] = 1
myfile.close()

import csv

myoutputfile = open('output.csv','x')
outputwriter = csv.writer(myoutputfile)
for k,v in my_dictionary.items():
    kv = [k,v]
    outputwriter.writerow(kv)