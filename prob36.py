#! usr/bin/python
#Find check to see if its a palindrome
#Add palindromes that pass the check to total
def findPals(i):
    total=0
    for i in range(0, 1000000):
        if(str(i)==str(i)[::-1] and (str(toBin(i))==str(toBin(i))[::-1])):
            total+=i
            i+=1    
        i+=1    
    return(total)
#Convert base 10 to base 2
def toBin(n):
    return("{0:b}".format(n))

def main():
    i=0
    print(findPals(i))
    
if __name__ == '__main__': main()
