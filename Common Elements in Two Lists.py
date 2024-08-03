#find common elements from two lists
def CommonElements(list1,list2):
    list=[]
    for i in list1:
        if i in list2:
        list.append(i)
    print(list) 
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
CommonElements(list1,list2)
