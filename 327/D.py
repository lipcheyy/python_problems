def simple(n):
    if n==2 or n==3:
        return 'yes'
    if n%2==0 or n<2:
        return 'no'
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return 'no'
    return 'yes'
n=int(input())
print(simple(n))

