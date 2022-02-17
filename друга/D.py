n=int(input());
f1=f2=1;
for i in range(2,n):
    f1,f2=f2,f1+f2+1
print(f2%1000000007)