# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list
# is sorted (either smallest-first or largest-first) and False otherwise. Your function
# must only consider each value in the list once (so, in terms of big-oh, which we will
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort
# the list.

def issorted(a):
    flag1 = True
    flag2 = True
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            flag1 = False
        if a[i] < a[i + 1]:
            flag2 = False
    if flag1 or flag2:
        return True
    return False


print(issorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 10]))
