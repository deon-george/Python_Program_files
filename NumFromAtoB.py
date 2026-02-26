#Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.

print("enter the first number")
a=int(input())
print("enter the second number")
b=int(input())
if a>=b:
    print("the first number is greater than the second number")
    exit()
else:
 print(f"The numbers from {a} to {b} are ")
 for i in range(a,b+1):
  print(i)