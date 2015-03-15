#! usr/bin/python
#Digit Counter
def digits(n):
    n=[int(i) for i in str(n)]
    if len(n)==1000:
        return True
    return False

#Fibonnaci Generator
def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b


def main():
    stop = False
    a = fib()
    i=-1
    #Stop when N is a length of 1000
    while stop!=True:
        i+=1 #Use I to track where in the sequence we are
        n=a.next()
        stop=digits(n)
        
    
    print(i)

if __name__ == '__main__': main()

        
