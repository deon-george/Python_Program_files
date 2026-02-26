print('enter the first cell co-ordinates')
a=int(input())
b=int(input())
if not (1 <= a <= 8 and 1 <= b <= 8):

   print('Error, enter a valid co-oridnate')
   exit()

print('enter the second cell co-ordinates')
c=int(input())
d=int(input())
if not (1 <= c <= 8 and 1 <= d <= 8):

    print('Error, enter a valid co-oridnate')
    exit()

#logic begins
if abs(a-c)==1 and abs(b-d) ==1:
    print('kings movt is possible')
else:
    print('kings movt not possible')
 
