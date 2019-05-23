# #!/usr/bin/python
# def gcd(a,b):
#     best = 1
#     for i in range(2,min(a,b)+1):
#         if a%i == 0 and b%i == 0:
#             if i > best:
#                 best = i
#     return best
#
# if __name__  ==  '__main__':
#     best_gcd = gcd(3,9)
#     print best_gcd

##Using Elucid Algorithm
def gcd1(a,b):
    new_a = a
    if b == 0:
        return new_a
    else:
        remin = new_a%b
        new_a = b
        b = remin
        print "Gcd is called with gcd1(%d, %d)"%(new_a,b)
        return gcd1(new_a,b)




a,b=map(int,raw_input().split())
print gcd1(a,b)
