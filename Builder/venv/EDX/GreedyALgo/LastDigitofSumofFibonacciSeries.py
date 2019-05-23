#!/usr/bin/python2
def fib(n):
    first = 0
    second = 1
    value = get_pisano_method(3)
    remainder = n % value
    res = remainder
    if n == 1 or n == 0 :
        return n%10
    else:
        for i in xrange(2,remainder+1):
            res = (first + second)
            first = second
            second = res
        return res%10

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


# def fib1(n):
#     for i in xrange(n+1):
#        memo1[i] = fib(i)
#        print memo1[i]
#     return memo1




n = int(raw_input())
#memo1 = [None]*(n+1)
print (fib(n+2)-1)%10


#New Method Based on Matrix Multiplication
MAX = 1000

# Create an array for memoization
f = [0] * MAX


# Returns n'th Fibonacci number
# using table f[]
def fib(n):
    n = int(n)

    # Base cases
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        return (1)

        # If fib(n) is already computed
    if (f[n] == True):
        return f[n]

    k = (n + 1) / 2 if (n & 1) else n / 2

    # Applying above formula [Note value n&1
    # is 1 if n is odd, else 0].
    f[n] = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1)) if (n & 1) else (2 * fib(k - 1) + fib(k)) * fib(k)
    return f[n]


# Computes value of first Fibonacci numbers
def calculateSum(n):
    return fib(n + 2) - 1


#Dynammic programming is suppose you are calculationg power(2,x) , and that is recursive power(2,x/2 ) + power ( 2,x/2) , Then no need to calculate two times power(2,x/2) , it
#will reuse the first calculation
