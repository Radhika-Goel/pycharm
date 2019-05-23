#!/usr/bin/python2
def fib1(n,m):
    first = 0
    second = 1
    value = get_pisano_method(m)
    remainder = n % value
    res = remainder
    if n == 1 or n == 0:
        return n%m
    else:
        for i in range(2,remainder+1):
            res = (first + second)%m
            first = second
            second = res
        print res
        return res%m

def get_pisano_method(m):
        a = 0
        b = 1
        c = a + b
        for i in xrange(0, m * m):
            c = (a + b) % m
            a = b
            b = c
            if (a == 0 and b == 1):
                return i + 1


# #Fibonacci Table
n , m = map(int , raw_input().split())
#memo1 = [None]*(n+1)
print fib1(n,m)