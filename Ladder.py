print("enter the number of steps")
n = int(input())
if n>9:
    exit()
else:
    for i in range(1,n+1):
        print(i)
        print('\n')
        for j in range(i):
            print(j)
            print('\n')
            for k in range(1):
              print(k)