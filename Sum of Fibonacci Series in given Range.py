#sum of fibonacci series numbers between x and y
def SumOfFibonacci(x,y):
    sum=0
    for i in range(x,y+1):
        sum+=i
    sum+=1
    print(sum)
x=int(input("Enter starting value:"))
y=int(input("Enter second value:"))
SumOfFibonacci(x,y)