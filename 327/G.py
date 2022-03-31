from math import gcd
def nGcd(n,m):
    return gcd(n,m)
l,m=input().split()
l=int(l)
m=int(m)
print(nGcd(l,m))