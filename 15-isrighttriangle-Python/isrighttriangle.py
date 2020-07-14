# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math


def distance(x1, y1, x2, y2,):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def isrighttriangle(x1, y1, x2, y2, x3, y3):
    # your code goes here
    s1 = distance(x1, y1, x2, y2)
    s2 = distance(x2, y2, x3, y3)
    s3 = distance(x1, y1, x3, y3)
    hyp = max(s1, s2, s3)
    side1 = min(s1, s2, s3)
    print("side 1 side 2 side3 ", s1, s2, s3)
    if (hyp) <= ((side1) + ((s1 + s2 + s3 - side1 - hyp))):
        print("False")
        return False
    print("True")
    return True


isrighttriangle(13, -1, -9, 3, -3, -9)
