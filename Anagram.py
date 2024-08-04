def CheckAnagram(str1,str2):
    list1=[]
    list2=[]
    for x in str1:
        list1.append(x)
    for y in str2:
        list2.append(y)
    list1.sort()
    list2.sort()
    if list1==list2:
        print("Anagram")
    else:
        print("Not anagram")
str1=input()
str2=input()
CheckAnagram(str1,str2)