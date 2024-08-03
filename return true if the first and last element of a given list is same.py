#write a function to return true if the first and last element of a given list is same
def same(arr):
    print("Given list:", arr)
    first=arr[0]
    last=arr[-1]
    if first==last:
        return True
    else:
        return False
arr=[]
len=int(input("Enter Length of List:"))
for i in range(len):
    num=int(input("Enter number:"))
    arr.append(num)
same(arr)

