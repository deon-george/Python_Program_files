import math
n = int(input())  # km per day
m = int(input())  # total distance
days = math.ceil(m / n)
print(days)