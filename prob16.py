#! usr/bin/python
#This ones pretty self explanatory
def main():
    total=0
    n=2**1000
    n=[int(i) for i in str(n)]
    for i in range(0, len(n)): 
        total+=n[i]

    print total

if __name__ == '__main__': main()

