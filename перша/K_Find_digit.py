n=int(input())
if n<0:
    n*=-1
    last_dig=(n-(n%10))//10;
    print(str(n%10),last_dig,sep="");
    
else:
    last_dig=(n-(n%10))//10;
    print(str(n%10),last_dig,sep="");