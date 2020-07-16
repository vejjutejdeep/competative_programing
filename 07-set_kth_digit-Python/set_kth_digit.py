# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative
# single digit (between 0 and 9 inclusive). This function returns the number n with
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left,
# so the 0th digit is the rightmost digit.

def divide(n):
    lis = []
    print(n)
    while(n != 0):
        lis.append(n % 10)
        n = n // 10
    # print(lis[::-1])
    return lis[::-1]


def fun_set_kth_digit(n, k, d):
    lis = divide(n)
    if len(lis) <= k:
        lis.append(0)
        for pos in range(len(lis) - 1, 0, -1):
            lis[pos] = lis[pos - 1]
            # print(lis)
        lis[0] = d
        print(lis)
    else:
        lis[k] = d
        print(lis)


fun_set_kth_digit(468, 3, 1)
