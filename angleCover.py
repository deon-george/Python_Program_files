import math
print ('enter the time ')
a= float(input())
b=math.floor(a)
#logic begins
c=a-b
angle=(60*b-11*c)/2
print (f'the angle swept b/w the hour hand and minute hand={angle:0.3f}')