import math
n = [int(i) for i in input().split()]
m = [int(i) for i in input().split()]
k=(n[0]+m[0])*3600 + (n[1]+m[1])*60 + n[2]+m[2]
hours=k//3600
minuten=k%3600//60
sec=k-minuten*60-hours*3600
print(hours%24,minuten,sec)