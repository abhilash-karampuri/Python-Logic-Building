'''
Priya is having x buckets where each buckets have some squares in each buckets(number of squares may or may not be equal) 
If number of buckets and number of squares in each buckets are given then find whether Priya can make a square with those blocks or not. 
Note that no such block can be borrowed from any other bucket or no block can be left in any such buckets.
'''
def Bucket(buckets):
    blocks=[]
    block=[]
    sum=0
    for x in range(1,buckets+1):
        print("Enter number of blocks in",x,"st bucket:")
        block=int(input())
        blocks.append(block)
    for i in range(buckets):
        sum+=blocks[i]
    sqrofsum=sum**(0.5)
    if sqrofsum.is_integer():
        print("Possible")
    else:
        print("Impossible") 
buckets=int(input("Enter Number of Buckets:"))
Bucket(buckets)