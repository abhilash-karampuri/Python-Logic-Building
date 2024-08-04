'''
check whether two strings are rotational of each other
note: two strings are in lower case and of same length.
abbca   ababc   acabb  acabb
'''
def checkrotation(str1,str2):
    newstr=str1+str1
    if len(str1)==len(str2):
        if str1.upper or str2.upper:
            str1.lower()
            str2.lower()
        if str2 in newstr:
            print("Both are Rotational of each other")
        else:
            print("Both arent Rotational of each other")
    else:
        return False
        

str1=input()
str2=input()
checkrotation(str1,str2)
    