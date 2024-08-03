'''Suppose that there are two lists: list1=[1,2,3,4,5,6,7....n]
list2=[0,1,2,3,....n-1] where n is any positive integer . 
Find the sum of two lists such that the first element of list1 is added to last element of list2 and so on... 
The result is store into a list find its mode
of the obtained list.'''
import random
n=int(input("enter length of lists:"))
list1=[]
list2=[]
for i in range(n):
    elem1=random.randint(0,9)
    list1.append(elem1)
for j in range(n):
    elem2=random.randint(0,9)
    list2.append(elem2)
print(list1)
print(list2)
list2.reverse()
print(list2)
final_list=[]
for x in range(n):
    elem=list1[x]+list2[x]
    final_list.append(elem)
print(final_list)

#mode Calculation

from collections import Counter

count = Counter(final_list)

max_freq = max(count.values())

modes = [num for num, freq in count.items() if freq == max_freq]

if len(modes) == len(final_list):
    print("No unique mode")
else:
    print(f"The mode(s) of the list are: {modes}")

