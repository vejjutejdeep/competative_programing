# Write the function isFactor(f, n) that takes
# two int values f and n, and returns True
# if f is a factor of n, and False otherwise.
# Note that every integer is a factor of 0.


def fun_isfactor(f, n):
    if n == 0:
        print("true")
        return True
    if f == 0:
        print("false")
        return False
    if f % n == 0:
        print("true")
        return True
    print("false")
    return False


fun_isfactor(2, 5)
