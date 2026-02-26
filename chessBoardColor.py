print (' enter the row and col of BOX1')
a=int(input())
b=int(input())
if not (0 <= a <= 9) or not (0 <= b <= 9):
    print('pls enter a valid box number')
    exit()

print (' enter the row and col of BOX2')
c=int(input())
d=int(input())
if not (0 <= a <= 9) or not (0 <= b <= 9):
    print('pls enter a valid box number')
    exit()

if (a-b)%2 ==0 and (c-d)%2 ==0 or (a+b+1)%2 ==0 and (c+d+1)%2 ==0:
 print("Yes")
else:
 print("NO")




