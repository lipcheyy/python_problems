import math
n = int(input())
hours=n//3600
minuten=n%3600//60
sec=n-minuten*60-hours*3600
hours%=24
if hours<10:
    print("0"+str(hours), ":", end='',sep="")
else:
    print(str(hours),":", end='',sep="")

if minuten<10:
    print("0"+str(minuten), ":", end='',sep="")
else:
    print(str(minuten), ":", end='',sep="")

if sec<10:
    print("0"+str(sec))
else:
    print(str(sec))