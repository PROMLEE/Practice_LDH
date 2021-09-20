def gcd_sub(a, b):
    while a*b !=0:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a+b

def gcd_mod(a, b):
    while a*b != 0:
        if a>b:
            a = a%b
        else:
            b = b%a
    return a+b

def gcd_rec(a, b):
    if a*b == 0:
        return a + b
    else:
        if a >= b:
            return gcd_rec(a-b, b)
        else:
            return gcd_rec(a, b-a)
        return a + b

n=list(map(int,input().split()))

x = gcd_sub(n[0], n[1])
y = gcd_mod(n[0], n[1])
z = gcd_rec(n[0], n[1])
print(x, y, z)