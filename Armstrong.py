#arm-strong number
def armstrong(num):
    sum=0
    num=str(num)
    length=len(num)
    for x in range(length):
        digit=num[x]
        digit=int(digit)
        sum=sum+digit**len(num)
    if str(sum)==num:
        print("arm")
    else:
        print("not arm")
num=int(input("Enter a number:"))
armstrong(num)
