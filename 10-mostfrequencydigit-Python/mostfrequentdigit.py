# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
    # your code goes
    d = {}
    flag = False
    val = str(n)
    for ele in range(len(val)):
        # print(val[ele])
        if val[ele] not in d:
            d[val[ele]] = 0
        else:

            flag = True
            d[val[ele]] += 1
        print(d)
    if flag == True:
        v = list(d.values())

        # taking list of car keys in v
        f = list(d.keys())

        print(f[v.index(max(v))])
    print(min(d))
    return min(d)


mostfrequentdigit(5231123123123)
