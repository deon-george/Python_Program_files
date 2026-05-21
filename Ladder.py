print("enter the number of steps")
n = int(input())
if n>9:
    exit()
else:
     print('\n')
    #printing the rows
    #very imp line to navigate to next line
     print()
     for i in range(1, n+1):
      #printing numbers
      for j in range(1, i+1):
        
        print(j,end="")
      print()