# MODULES

# import math
# from math import cos,sin,pi                        #if u need only cos
# from math import *


# print(m.pi)
# print(cos(3.14))
# print(sin(3.14))
# print(pi)


# def greet():
#     print('Good Morning Ankit!')
# greet()

# def greet(name):
#     print('Good Morning',name)
# greet('Ankit')

# def greet(name,dish = 'chicken'):
#     print('good morning',name)
#     print('plz eat',dish)
# greet('Ankit','maggie')
# greet('Ankit')


# def sum_of_list(a):
#     print('Calculating...')
#     return sum(a)
# marks = [45,16,87,98,45]
# sum_of_marks = sum_of_list(marks)
#
# print('my sum of marks',sum_of_marks)



# Write a function whichtakes a list of names as argument and greets "Hello" to everyone

def greetings(names):
    for name in names:
        print('Hello',name)

names = ['Ankit','Raman','Haris']
greetings(names)
