print('enter the first time in 24hr format')
a=int(input())
b=int(input())
c=int(input())
if a <=24 :
 print('TIme1 in hr min sec=',a,":",b,":",c)
else :
 print('time1 not in 24 format ,pls enter in the correct format')
 exit()
print('enter the second time in 24hr format')
a1=int(input())
b1=int(input())
c1=int(input())
if a1  <= 24 :
 print('TIme1 in hr min sec=',a1,":",b1,":",c1)
else :
 print('time2 not in 24 format ,pls enter in the correct format')
 exit()

print('The net difference in times=',abs(a-a1),':',abs(b-b1),':',abs(c-c1))