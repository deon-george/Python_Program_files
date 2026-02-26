print('enter a number')
a=int(input())
tenthDigit=a%100
tenthplace=tenthDigit-(tenthDigit%10)
finalAns=tenthplace//10
#print('tenth place digit of the given number=',tenthDigit)
print('tenth place digit of the given number=',finalAns)