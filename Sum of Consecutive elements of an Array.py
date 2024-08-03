#sum of consecutive elements of an array to form a new array
def SumOfConsecutive(arr):
    newarr=[]
    len=0
    for i in arr:
        len+=1
    for x in range(0,len-1):
    if x%2==0:
        elem=arr[x]+arr[x+1]
        newarr.append(elem)  
    print(newarr)
arr=[1,2,3,4,5,6,7,8]
SumOfConsecutive(arr)