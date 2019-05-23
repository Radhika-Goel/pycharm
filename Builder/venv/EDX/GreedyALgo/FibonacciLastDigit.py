#/usr/bin/python2
#memonization
#Last Digit of Fibonacci Number
def fib1(n):
    for i in xrange(n+1):
       if memo1[n] != None:
          return memo1[n]
       if i == 0:
            f = 0
       elif i <= 2:
            f = 1
       else:
            f = memo1[(i-1)] + memo1[(i-2)]
       memo1[i] = f%10
    return memo1[n]
#Fibonacci Table
n = int(raw_input())
memo1 = [None]*(n+1)
print fib1(n)