'''program to find middle element of a list  consting of ramdom integers(post or neg)
if its even list then find the two middle elements and find its avg and result of avg value is near to middle elements'''
n=int(input())
list=[]
for x in range(n):
    elm= int(input())
    list.append(elm)
len =n
if n %2 !=0:
    midind1 =(len-1)/2
    print(list[midind1])
else:
    ind1=(len-1)/2
    ind2=(len-2)/2
    midind2=(ind1+ind2)/2
    print(list[int(midind2)])