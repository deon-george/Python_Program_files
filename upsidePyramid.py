print("enter the number of steps")
n = int(input())
if n>9:
    exit()
else:
    print('\n')
    #printing the rows
    for i in range(n,0,-1):

        #print spaces
        for j in range(n-i):
               print(" ", end="")

                #print numbers
        for k in range (1,i+1):
             print(k, end="")

        print()  # move to next line
                   

       
          