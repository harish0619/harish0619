# This file is created for days which are not so productive. 

# These are zip and map functions 
print(list(map(lambda x: x+x, [1,2])))

num1 = [1,2,3]

num2 = [4,5,6]

print(list(map(lambda x,y: x+y, num1, num2)))

list(zip([1,2,3],[4,5,6]))


# This is python closures

def outer(func):
  def inner(*args, **kwargs):
    print(f'calling {func.__name__}')
    result = func(*args, **kwargs)
    print('Function called and executed')
  return inner 

f = outer(lambda a,b: a+b)

f(1,2) 

# How to raise exceptions 

name = 'Jane'

if name.casefold() == 'jane':
  print('Right name is passed')
else:
  raise ValueError('Please pass the name Jane')

# File reading 

with open('requirements.txt') as f:
    print(f.readlines()) 

# print factorial using recursion 

def fact(n):
    if n == 1:
        return n
    else:
        return n* fact(n-1)

print("Hello world!")

# Write to file 

with open('dummy.txt', 'w') as f:
  f.write("Hello, i'm learning how to write to a file\n")

print("Dummy print statement")

print("Not well") 

print("Not well")

with open('dummy.txt', 'a') as f:
  f.write("Appending to an existing file\n")

# print fibonacci using recursion 

def fib(n):
  if n<=1:
    return n
  else:
    return (fib(n-1) + fib(n-2))

print("Not well")

print("Not well")


# Import exercises 
import matplotlib as mpl

import math 

from math import sin, cos, tan, pi

# Learning time and date modules 

import time, calendar 

gm_time = time.gmtime(0) # Converts an epoch time to normal time 

calendar.timegm( gm_time ) # Converts a normal time to epoch time 

print('dull day')

print('dull day') 

print('dull day')

print('dull day') 

print('dull day')

import csv
with open('text.csv') as f:
  reader = csv.reader(f)
  for row in reader:
    print(row)


