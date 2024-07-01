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
