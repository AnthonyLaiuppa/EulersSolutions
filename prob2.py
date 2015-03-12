#! usr/bin/env python

from math import sqrt

def F(n): #Mathmatical Representation of Fibonnaci using Binet
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))) 

def main():
    even=0
    i=0
       
    #When total hits upper bound stop computing 
    while(F(i)<4000000):  
        #If Even add to even for summation
        if(F(i)%2==0):
            even+=F(i)
        i+=1

    #Summation of all even numbers less than 4000k in the sequence
    print('Final even value is %d' % even)

if __name__ == '__main__': main()
