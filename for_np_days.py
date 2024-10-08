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

import random

print(random.random())

random.seed(0)

for _ in range(5):
    print(random.random())

random.seed(1)

for _ in range(5):
    print(random.randrange(1,6))


print('dull day')

print('dull day')

class Person:
  '''A dummy class'''
  def __init__(self, firstname='John', lastname='Doe'):
    self.firstname = firstname
    self.lastname = lastname
    self.email = ''

  def display(self):
    print(f"The person is {self.firstname} {self.lastname}")

class Bank:
  '''A dummy class to create new banks'''
  def __init__(self, initial_deposit, firstName, lastName, email=' '):
    self.firstname = firstName
    self.lastname = lastName
    self.email = email
    self.balance = initial_deposit

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    if self.balance > amount:
      self.balance -= amount

  def display_balance(self):
    print(f"The current balance is: {self.balance}")

  def update_details(self, email):
    self.email = email 

hdfc = Bank(50000, 'Harish', 'Dhandapani', 'hello@xyz.com')



