#!/usr/bin/python
def party(x):
    segments = []
    left = 0
    while left <= len(x)-1 :
        l , r = x[left],x[left]+2
        print l,r
        #segments.append((l,r))
        left = left + 1
        while left <= len(x)-1 and x[left] <= x[left]+2:
            #segments.append((x[left], r))
            left = left + 1
        print left
        #left = left + 1
    return segments

a = [1,2,3,3,4,5,6,6,6,7]
print party(a)
