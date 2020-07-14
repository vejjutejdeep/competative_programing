# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math


def isrighttriangle(x1, y1, x2, y2, x3, y3):
    # your code goes here
    s1 = distance(x1, y1, x2, y2)
    s2 = distance(x2, y2, x3, y3)
    s3 = distance(x1, y1, x3, y3)
    hyp = max(s1, s2, s3)
    side1 = min(s1, s2, s3)
    if (hyp ** 2) == (side1 ** 2) + ((s1 + s2 + s3 - side1 - hyp) ** 2):
        return True
    return False


def distance(x1, y1, x2, y2,):
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
