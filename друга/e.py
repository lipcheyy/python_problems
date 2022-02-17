n=[int(i) for i in input().split()]
for i in range(1,n[1]):
    n[0]*=n[0]
print(n[0]%10000)