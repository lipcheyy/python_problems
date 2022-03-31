def f(m,n):
    if m==0 or m==n:
        return 1
    if 0<m<n:
       return f(m-1,n-1)+f(m,n-1)
l,m=input().split()
l=int(l)
m=int(m)
print(f(l,m))
