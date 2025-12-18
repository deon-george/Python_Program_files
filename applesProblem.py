#apple sharing problem 
print('enter no: of students')
students= int(input())
print('no: of apples')
apples= int (input())
if students ==0:
 print('NO students to take apples')
 exit()
s=apples//students
print('no: of apples for each student=', (s))
if students== apples:
 print('remaining apples= zero')
elif  students > apples:
 print('remaining apples= zero')
else :
 print('remaining apples=',apples % students)