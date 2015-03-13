#! usr/bin/env python
#This one is pretty self explanatory
#I could style it or format it but this works so....
def main():

   squaresSum=0
   sumSquared=0

   for i in range(1, 101):
      sumSquared+=i
      i+=1
   
   for i in range(1, 101):
      squaresSum+= i**2  
      i+=1

   print((sumSquared**2) - squaresSum)
   
if __name__ == '__main__': main()
