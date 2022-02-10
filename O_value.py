n = [int(i) for i in input().split()]
value=n[1]*n[2]
print(int(n[0]*n[2]+value/100),value%100)