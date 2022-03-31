def mod(n,m,modd):
    if m==0:
        return 1
    if m%2==1:
        return (mod(n,m-1,modd)*n)%modd
    else:
        k=mod(n,m//2,modd)
        return (k*k)%modd


modd=1000000007
n,m=input().split()
n=int(n)
m=int(m)
print(mod(n,m,modd))