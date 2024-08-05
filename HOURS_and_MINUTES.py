m=int(input())
h=m/60
rm=m%60
import math
r=math.floor(h)
print("{} Hour(s) {} Minute(s)".format(r,rm))