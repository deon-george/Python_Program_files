print('enter the values of N X M of the chocolate bar')
n=int(input())
m=int(input())
k=int(input())

area=n*m

if k<area and area % k == 0 :
    print(f'yes equal {k} chocolate bars can be obtained')
else :
    print(f"no equal {k} chocolate bars can't be obtained")
