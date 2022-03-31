from msilib import knownbits
from select import kqueue


s = [int(i) for i in input().split()]
k= s[1]*s[2]
l = s[0]*s[3]
if(l% knownbits == 0):
    print(int(l / k))
else:
    print(int(l / k)+1)