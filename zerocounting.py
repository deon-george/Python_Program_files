count = 0
n = int(input("Enter the number limit:"))

print('enter the numbers')

for i in range(n):
    number = int(input())
    if number == 0:
        count += 1

print("Number of zeros:", count)