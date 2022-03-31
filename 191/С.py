s = [int(i) for i in input().split()]
if( (s[0]+s[1])>s[2] and (s[1]+s[2])>s[0] and (s[0]+s[2])>s[1]): print("Yes")
else: print("No")

