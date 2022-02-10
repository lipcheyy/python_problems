import math
n=[float(i) for i in input().split()]
r=math.sqrt((n[0]-n[2])**2+(n[1]-n[3])**2)
print("{0:.3f}".format(r))