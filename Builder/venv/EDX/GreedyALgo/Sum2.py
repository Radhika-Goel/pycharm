#/usr/bin/python2
import sys
a,b=map(int,raw_input().split())
if a <= 0 and b > 9:
    sys.exit("Dont fulfil the constraints of input parameters")
else:
    print a+b