import math
n,m,k=int(input()),int(input()),int(input());
j=0;
l=0;
while j<=n:
    j+=m;
    l+=1;
    if j>=n:
        print(l);
        break;
    else:
        j-=k;