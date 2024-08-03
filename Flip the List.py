#print flip of a Random positive numbers list evenly if length of list is even and if length of list is odd, 
#flip the list based on max sum of numbers on each flip
#example: [1,2,3,    4,5,6,7]
import random
list=[]
flip1=[]
flip2=[]
n=int(input())
for x in range(n):
    elem=random.randint(1,100)
    list.append(elem)
    list.sort()
print(list)

if n%2==0:
    low=0
    high=n-1
    mid=(low+high)//2
    print("Middle element:", list[mid])

    # Append the first half of the list to flip1
    flip1 = list[:mid+1]  # This slices the list from the start to the middle
    print("First half (flip1):", flip1)
    flip2=list[mid+1:]
    print("Second half (flip2):",flip2)
else:
    low=0
    high=n-1
    mid=(low+high)//2
    print("Middle element:", list[mid])
    leftsum=0
    rightsum=0
    for  i in range(0,mid):
        leftsum+=i
    for  j in range(mid+1,n-1):
        rightsum+=j
    if leftsum> rightsum:
        flip1=list[:mid+1]
        
    else:
        flip2=list[mid:]
print("First half:(flip1):",list[:mid])
print("Second half (flip2):", flip2)
    