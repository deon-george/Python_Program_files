#exception
#print("hello wolrd")
while True:
 try:
  x = int(input("what is X="))
  print(f"x is {x}")
  break
    
 except ValueError:
  print("x is not an intger")

