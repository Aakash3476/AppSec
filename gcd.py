#!/usr/bin/python
import sys
def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)

def main():
	
	A = [12,24,6,18]
	res = A[0]
	for c in A[1::]:
	    rse = gcd(res , c)
	print res

if __name__=='__main__':
	main()
