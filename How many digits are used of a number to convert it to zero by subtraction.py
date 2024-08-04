#count number of times a least digit of a number is subtracted to become zero.
def NoOfTimes(digit):
    count = 0
    while digit > 0:
        strdigit = str(digit)
        if len(strdigit) == 1:  # Single digit case
            x = int(strdigit)
            digit -= x
            count += 1
        else:  # Multiple digits case
            x = int(strdigit[0])
            y = int(strdigit[1])
            if x > y:
                digit -= x
            else:
                digit -= y
            count += 1
    print(count)
digit = int(input)
NoOfTimes(digit)
