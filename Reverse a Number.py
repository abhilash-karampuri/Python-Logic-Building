#reverse a number program
def ReverseNumber(num):
    while num!=0:
        a=num%10
        print(a,end="")
        num=num//10
num=int(input())
