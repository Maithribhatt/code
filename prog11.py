def hello(name):
    print('hello '+name)
hello('alice')
hello('bob')

def hello():
    print('hello')
    print('world')
    print('in python')
hello()
hello()
hello()

import random
print(random.randint(0,5))

print('hello',end=' ')
print('world')
print('cats','dogs','mice')
print('cats','dogs','mice',sep=',')

def spam(divby):
    try :
         return 42/divby
    except ZeroDivisionError:
        print('error:Invalid argument')
     
print(spam(42))
print(spam(23))
print(spam(0))
