print('enter a 3 digit number')
a=int(input())
#ones place digit
oneNO=a%10
#tenth place digit
b=a%100
c=b-oneNO
tenNO=c//10
#hundreds place digit
hundNO=a//100

sum=oneNO+tenNO+hundNO
print('sum of the given 3 digit number=',sum)

