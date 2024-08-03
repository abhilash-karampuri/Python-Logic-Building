#Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.
list=[]
nelems=int(input())
for x in range(nelems):
    elem=input()
    list.append(elem)
n=int(input())
nthelem=list[n-1]
prevelem=list[n-2]
if prevelem in nthelem and prevelem!=nthelem:
    print("True")
else:
    print("False")