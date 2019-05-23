#!/usr/bin/python2
def change(n):
    s = 0
    if n <= 1:
        return n
    if n >= 10:
        s  = n/10 + change(n%10)
    elif n >= 5:
        s = n/5 + change(n%5)
    elif n >= 1:
        s = n/1

    return s





n = int(raw_input())
print change(n)
