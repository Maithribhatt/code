import random
for i in range(5) :
    print(random.randint(1,100))
    
import sys
while True :
    print('type exit to exit')
    response=input()
    if response== "exit":
        sys.exit()
    print('you typed'+response+'.')
