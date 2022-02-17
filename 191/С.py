a,b,c=input().split()
a=int(a); b=int(b); c=int(c);
if a+b>c & a+c>b & b+c>a:
    print("Yes")
else: print("No")