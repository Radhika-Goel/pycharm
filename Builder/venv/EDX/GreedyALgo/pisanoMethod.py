#!/usr/bin/python
def get_pisano_method(m):
    a = 0
    b = 1
    c = a + b
    for i in range(0,m*m):
        c = (a + b) % m
        a = b
        b = c
        print c
        if ( a == 0 and b == 1 ):
            return i + 1

value = get_pisano_method(3)
print value