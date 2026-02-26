print("enter the first number")
a=int(input())
print("enter the second number")
b=int(input())
if a>=b:
 #print the numbers in descending order
 print(f"The numbers from {a} to {b} are ")
 for i in range(a,b-1,-1):
  print(i)
if a<b:
 #print the numbers in ascending order
 print(f"The numbers from {a} to {b} are ")
 for i in range(a,b+1):
  print(i)
