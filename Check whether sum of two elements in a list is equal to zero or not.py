#A list containg random integers. Check whether sum of any elements in the list equal to zero or not
def has_zero_sum_pair(lst):
    seen = set()
    for number in lst:
        if -number in seen:
            return True
        seen.add(number)
    return False

lst = [4, 2, -4, 3, 5]
result = "Yes" if has_zero_sum_pair(lst) else "No"
print(result)
            