#! usr/bin/env python

def main():
     n = 0
     total = 0
     while n<1000:
        if(n%3 ==0):
            total+=n
            n+=1
        elif(n%5 ==0):
            total +=n
            n+=1
        else:
            n+=1
            continue

     print(total)


main()

