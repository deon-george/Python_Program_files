#10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.

print('enter the 10 numbers')
total=0
for i in range (10):
    total+=int(input())
print("Sum =", total)
