#Find two elements of an array whose product is maximum
def MaxProduct(n):
    list=[]
    for x in range(n):
        elem=int(input())
        list.append(elem)
    list.sort()
    product=list[n-1]*list[n-2]
    print(list[n-1],list[n-2], "are the elements whose product is maximum")
n=int(input("Enter length of list:"))
MaxProduct(n)
