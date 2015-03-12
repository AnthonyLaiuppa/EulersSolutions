#! usr/bin/env python
import time

def main():
    i = 20000 # Start here
    stop=False# End Condition
    start = time.time()
    #These encompass all numbers we need it divisible by
    while(stop!=True):    
        if(i%20==0):
            if(i%19==0):
                if(i%18==0):
                    if(i%17==0):
                        if(i%16==0):
                            if(i%14==0):
                                if(i%13==0):
                                    if(i%11==0):
                                        print i
                                        stop = True
                                        print time.time()-start, 's'
                                        #print the resultant
        i+=1
        #iteratively woo!
    

if __name__ == '__main__': main()
