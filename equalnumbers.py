print('enter the numbers')
a=int(input())
b=int(input())
c=int(input())

if a==b==c :
 print('All 3 numbers are equal')
elif a==b or b==c or a==c :
 print('two numbers are equal')
else : print('the numbers are different')