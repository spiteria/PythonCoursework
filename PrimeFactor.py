'''
Created on Sep 30, 2014

@author: AndrewSpiteri
'''
from random import randrange

def main():
    x, z, i = 0, 0, 0
    a = [None]*1000
    num = randrange(0,1000)
    print("the original value is: ",num)
    placeHolder = num
    counter = 2
    while counter <= num:
        print("counter is now:",counter)
        x = num%counter
        print("x is now: ",x)
        y = num / counter
        print("y is now: ",y)
        if x == 0:
            a[i] = counter
            i = i + 1
            num = y
            print("num is now: ",num)
            z = z + 1
            counter = 2
            if y == 1:
                counter = num+1
        if x != 0:        
            counter = counter + 1
    '''
    print("The prime factors of",placeHolder,"are: ")
    for i in range(z):
        print(a[i])
    '''
    b = [None] * (z+1)
    c = [None] * (z+1)
    b[0] = a[0]
    count, index, c[0] = 1, 0, 1
    for i in range(z):
        if a[i] == a[i+1]:
            count = count + 1
            c[index] = count
            if b[index] != a[i]:
                index = index + 1
                b[index] = a[i]
        if a[i] != a[i+1] and a[i] != None:
            count = 1
            index = index + 1
            c[index] = count
            b[index] = a[i+1]
    print("The prime factors of",placeHolder,"are: ")
    for i in range(index):
        print(b[i],"^",c[i])
        
main()
