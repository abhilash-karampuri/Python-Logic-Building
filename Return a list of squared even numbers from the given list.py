#Write a Python function that takes a list of integers and returns a new list containing only the even numbers from the original list, squared
def squarearray(newarray):
    newarray=[]
    for x in arr:
        if x%2==0:
            newarray.append(x*x)
    return newarray
arr=[12,23,45,78]
squarearray(newarray)
