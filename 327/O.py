def f(x,y):
    if x<=0 or y<=0:
        return 0;
    if x<=y:
        return f(x-1,y-2)+f(x-2,y-1)+2
    if x>y:
        return f(x-2,y-2)+1


n,m=input().split()
n=int(n)
m=int(m)
print(f(n,m))