#find out misleading number in a sequencial numbers of a list
list=[1,2,7,3,4,5,6]
diff1=list[1]-list[0] #1
diff2=list[2]-list[1] #5
if diff1==diff2:
    maindiff=diff1
else:
    maindiff=list[4]-list[3]
for x in range(0,len(list)-1):
    if list[x+1]-list[x]==maindiff:
        continue
    else:
        misleading=list[x]
print("Misleading number:",misleading)

