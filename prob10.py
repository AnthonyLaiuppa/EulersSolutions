#! usr/bin/python
def isPrime(n):
    """Verify if its prime or not and
    eliminate simple cases
    we only want to be working with primes in 
    this scenario so we look through only primes
    in order to save time"""  
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    #Loop checks for factors 
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def main():
    primeSum=0
    i=2
    while(i<2000000):
        if(isPrime(i)==True):
            primeSum+=i
            i+=1
        i+=1

    print(primeSum)

if __name__ == '__main__': main()
