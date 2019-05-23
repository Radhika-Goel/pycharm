def lcm(a,b):
     gcd_value = gcd1(a,b)
     return a*b/gcd_value

def gcd1(a,b):
    new_a = a
    if b == 0:
        return new_a
    else:
        remin = new_a%b
        new_a = b
        b = remin
        return gcd1(new_a, b)



a,b=map(int,raw_input().split())
value = lcm(a,b)
print value
