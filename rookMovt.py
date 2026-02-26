print('enter the first cell co-ordinates')
a=int(input())
b=int(input())
if a <0 and b <0:
    print('Error, enter a valid co-oridnate')
    exit()
if a<=8 and b<=8 :
    print('Error, enter a valid co-oridnate')
    exit()
     
print('enter the second cell co-ordinates')
c=int(input())
d=int(input())
if c <0 and d <0:
    print('Error, enter a valid co-oridnate')
    exit()
if c<=8 or d<=8:
    print('Error, enter a valid co-oridnate')
    exit()

if(a==c) or (b==d):
    print('the Rook can move')
else:
   print("the Rook can't move ")