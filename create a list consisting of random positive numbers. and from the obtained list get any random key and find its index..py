#create a list consisting of random positive numbers. and from the obtained list get any random key and find its index.
import random
list = []
n=int(input("Enter the length of list:"))
for x in range(n):
    elem=random.randint(1,20)
    list.append(elem)
key=random.choice(list)
print("Key value is" ,key)
print(list)
index=list.index(key)
print("Key is found at index" ,index)

#Method2
'''
def BinarySearch(list,key):
    Found=False
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        if key==list[mid]:
            Found=True
            index=mid
            break
        elif key>list[mid]:
            low=mid+1
        else:
            high=mid-1
    if Found:
        print("Key is found at index", index)
    else:
        print("Key is not found")
list=[2,8,19,17,18]
list.sort()
print(list)
key=int(input("Enter Key value:"))
BinarySearch(list,key)
'''