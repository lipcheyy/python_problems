n=int(input())
k = 0
while n > 0:
    res=n%10
    n//=10
    k*=10
    k+=res
print(k)