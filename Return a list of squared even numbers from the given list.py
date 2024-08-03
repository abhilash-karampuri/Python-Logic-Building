#Write a Python function that takes a list of integers and returns a new list containing only the even numbers from the original list, squared
arr=[1,2,3,4,5,6]
newarray=[]
for x in range(1,7):
    if x%2==0:
        square=x*x
        newarray.append(square);
print(newarray)