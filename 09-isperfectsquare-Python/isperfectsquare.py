# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.
import math


def isperfectsquare(n):
    # your code goes here
    if (type(n) == int):
        if (n < 0):
            return False
        print(math.sqrt(n))
        print(type(math.sqrt(n)) == int)
        return (type(math.sqrt(n)) == int)
    elif (type(n) == float):
        return False
    if(n.isnumeric()):
        n = int(n)
        if (n < 0):
            return False
        return (type(math.sqrt(n)) == int)
    return False


isperfectsquare(625)
