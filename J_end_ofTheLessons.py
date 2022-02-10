n=int(input())
k = 540
for i in range(n-1):
    if i%2==0:
        k+=50
    else:
        k+=60
k+=45
print(k//60, k%60)