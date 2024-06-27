# This file is created for days which are not so productive. 

print(list(map(lambda x: x+x, [1,2])))

num1 = [1,2,3]

num2 = [4,5,6]

print(list(map(lambda x,y: x+y, num1, num2)))

list(zip([1,2,3],[4,5,6]))

def outer(func):
  def inner(*args, **kwargs):
    print(f'calling {func.__name__}')
    result = func(*args, **kwargs)
    print('Function called and executed')
  return inner 

f = outer(lambda a,b: a+b)

f(1,2) 
