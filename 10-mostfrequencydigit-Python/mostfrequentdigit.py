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
        k = list(d.keys())
        m = max(v)
        val = []
        for ele in range(len(k)):
            if d[k[ele]] == m:
                val.append(k[ele])
        print(int(min(val)))
        return int(min(val))
    print(int(min(d)))
    return int(min(d))


mostfrequentdigit(24)
