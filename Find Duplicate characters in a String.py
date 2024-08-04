#find the duplicate elements of a string
def Duplicates(str):
    count_dict = {}
    result_list = []
    for x in str:
        if x in count_dict:
            count_dict[x] += 1
        else:
            count_dict[x] = 1
    for i in count_dict:
        if count_dict[i] > 1:
            result_list.append(i)
    print("Character counts:", count_dict)
    print("Characters appearing more than once:", result_list)
str=input()
Duplicates(str)