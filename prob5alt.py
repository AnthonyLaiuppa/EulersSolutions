#! usr/bin/env python
import time
import math
def main(): 
   """Based on how I derived the last solution
   I figured using the inverse would yield the correct
   answer. What I dont know is why in both scenarios
   I didnt account for 16 but adding it in got the correct
   answer."""
   answer = (math.factorial(20)/(16*15*12*math.factorial(10)))
   print answer  
if __name__ == '__main__': main()

