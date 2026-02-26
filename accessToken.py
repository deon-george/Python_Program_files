print("Pls, Enter the Access Token")
access=int(input())
if access < 2 :
 print('Acesss denied')
 exit()

is_prime = True
for i in range(2,access):
  if access % i ==0 :
     is_prime = False
     break
  
total=0
temp=access
while temp>0:
   a=temp%10
   total+=a
   temp=temp//10
   
for i in range(2,total):
   if total %  i ==0 :
      is_prime=False
      break
  
  
if is_prime:
    print("Access granted")
else:
    print("Access denied")