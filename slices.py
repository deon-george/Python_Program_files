#In the first line, print the third character of this string.
string1=input('enter the first string1=')
print(string1[2])

#In the second line, print the second to last character of this string.
string2=input("enter the second string2= ")
length2 = len(string2)
for i in range (1,length2):
     print(string2[i])
 
#In the third line, print the first five characters of this string.
string3 = input('enter the string3=\n')
for j in range (0,4):
 print(string3[j])

#In the fourth line, print all but the last two characters of this string.
string4 = input('enter the string4=')
length4 = len(string4)
for i in range (0,length4-2):
  print(string4[i])

#In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).
  
string5 = input('enter the string5=')
length5 = len(string5)
for i in range (0,length5,2):
   print(string5[i])

#In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).

string6 = input('enter the string6=')
length6 = len(string6)
for i in range (1,length6,2):
    print(string6[i])

#In the seventh line, print all the characters of the string in reverse order.

string7 = input('enter the string7=')
length7 = len(string7)
for i in range (length7-1,-1,-1):
    print(string7[i],end=" ")
print()

#pallindrome

string7 = input('enter the string=')
length7 = len(string7)
l = length7//2
for i in range (0,l):
    if string7[i]==string7[length7-i-1]:
        print('string is pallindrome')
        break
else:       
  print('string is not pallindrome')


 
