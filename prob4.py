#! usr/bin/env python
#Check if its the same forwards and back
def isPal(n):
    if(str(n)==str(n)[::-1]):
        return True
    return False


#Big loop of multiplication
def findPals():
    
    pals=[]
    for k in range(100,999):
        for j in range(100,999):
            product =k*j
            if isPal(product):
                pals.append(product)
    
    return(max(pals))

def main():

    print(findPals())

if __name__ == '__main__': main()
