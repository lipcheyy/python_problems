def noABCrows(n):
    arr=[None]*101
    if n==0:
        return 1;
    if n==1:
        return 3
    arr[n]=3*noABCrows(n-1)-noABCrows(n-2)
    return arr[n]
n=int(input())
print (noABCrows(n))
    