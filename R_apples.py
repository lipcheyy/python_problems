n,m=input().split();
n=int(n)
m=int(m)
res=n-(m-1)%n-1;
print(res)