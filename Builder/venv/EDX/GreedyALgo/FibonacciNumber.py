#/usr/bin/python2
#memonization
def fib(n):
    if n in memo:
        return memo[n]
    if n == 0:
        f = 0
    elif n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    memo[n] = f
    return f

n = int(raw_input())
memo = {}
print fib(n)

def fib1(n):
    for i in xrange(n+1):
       if memo1[n] != -1:
           return memo1[n]
       elif i == 0:
            f = 0
       elif i <= 2:
            f = 1
       else:
            f = memo1[i-1] + memo1[i-2]
       memo1[i] = f
    return memo1[n]
#Fibonacci Table
n = int(raw_input())
memo1 = [-1]*(n+1)
print fib1(n)

#Last Digit of Fibonacci Number
def fib(n):
    if n in memo:
        return memo[n]
    if n == 0:
        f = 0
    elif n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    memo[n] = f%n
    return memo[n]

n = int(raw_input())
memo = {}
print fib(n)

def fib1(n):
    for i in range(n+1):
       if memo1[n] != None:
           return memo1[n]
       elif i == 0:
            f = 0%10
       elif i <= 2:
            f = 1%10
       else:
            f = memo1[(i-1)%10] + memo1[(i-2)%10]
       memo1[i] = f
    return memo1[n]%10
#Fibonacci Table
n = int(raw_input())
memo1 = [None]*(n+1)
print fib1(n)


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