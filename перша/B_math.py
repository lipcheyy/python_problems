import math
digit=int(input())
first_dig=math.floor(digit/10);
last_dig=digit%10;
shutka=math.floor(((digit-(first_dig+last_dig))/9)+1);
conv= str(shutka)+str(last_dig)
print(int(conv)-10)