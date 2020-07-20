# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
    # your code goes
    d = {}
    val = str(n)
    for ele in range(len(val)):
        if ele not in d:
            d[val] = 0
        else:
            flag = True
            d[val] += 1
    if flag:
        Keymax = max(d, key=lambda x: d[x])
        print(Keymax)
        return(Keymax)
    print(min(d))
    return min(d)
