def count(n):
    n//=10
    if not n:
        return 1;
    return 1+count(n)     
n=int(input())
print(count(n))
