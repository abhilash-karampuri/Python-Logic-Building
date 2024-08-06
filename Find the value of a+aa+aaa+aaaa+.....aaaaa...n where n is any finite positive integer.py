#Find the value of a+aa+aaa+aaaa+.....aaaaa...n where n is any finite positive integer
n=int(input("Enter the limit:"))
a=input()
sum=0
for x in range(n):
  num=a*x
  num=int(num)
  sum+=num
print(sum)
