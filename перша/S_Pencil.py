n= [int(i) for i in input().split()]
m = [int(i) for i in input().split()]
k=n[0]*100+n[1];
l=m[0]*100+m[1]
res1=int(l/k)
res2=l-(res1*k)
print(res1)
print(int(res2/100),int(res2%100))