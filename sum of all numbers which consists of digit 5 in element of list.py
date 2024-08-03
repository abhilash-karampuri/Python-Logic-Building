#If there is a list of random number elements consists of n positive integers such that the digits 
#in each element of list do not exceed 2. Find the sum of all numbers which consists of digit 5 in element of list
import random
n=int(input("Enter Length of list:"))
list=[]

for x in range(n):
    elem=random.randint(0,99)
    list.append(elem)
print(list)
sum=0
for i in list:
    if (i%5==0 and i%10!=0 ) or 50<=i<=59:
        sum+=i   
print(sum)

