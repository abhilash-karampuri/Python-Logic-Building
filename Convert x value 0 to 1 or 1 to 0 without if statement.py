#a variable x has either value 0 or 1. Convert x to 1 if its 0 and if its 1 convert to 0. Note you cannot use if statement
x=int(input())
#x=(x+1)%2
#x=1-x
x=not x and 1
print(x)