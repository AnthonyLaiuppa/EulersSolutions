#! usr/bin/env python
    
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
    #Loop seeks out next prime factor and returns it
    while f <= r:
        if n%f == 0: return (False, f)
        if n%(f+2) == 0: return (False, (f+2))
        f +=6
    return True

def main():
       
    number=600851475143 

    while(True):
        #Throw the number in and begin searching for primes
        #Then itll iterate until it finds a prime
        #Then divide the number by the prime to remove the prime 
        #as a factor, then restart the loop
        #By the process of elimination the last number we are
        #Left with is the largest prime number
        prime =isPrime(number)
        prime =prime[1]
        number =number/prime
        if(isPrime(number)==True):
            print 'Largest prime is', number
            break

if __name__ == '__main__': main()
