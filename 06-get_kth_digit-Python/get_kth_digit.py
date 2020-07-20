# Write the function getKthDigit(n, k) that takes
# a possibly-negative int n and a non-negative int k,
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0


def fun_get_kth_digit(digit, k):
    if(digit < 0):
        digit = -digit
    if (len(str(digit))):
        return 0
    n = digit
    cout = 0
    while (n > 0):
        m = n % 10
        if (cout == k):
            return m
        n = n//10
        cout += 1
