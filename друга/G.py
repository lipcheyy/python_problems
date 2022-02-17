a,b,c,d=input().split();
a=int(a);
b=int(b);
c=int(c);
d=int(d)
max_ab=max(a,b);
min_ab=min(a,b);
max_bc=max(c,d);
min_bc=min(c,d);
if (max_ab>max_bc) & (min_ab>min_bc) or (max_ab<max_bc) & (min_ab< min_bc):
    print(1);
else:
    print(0);