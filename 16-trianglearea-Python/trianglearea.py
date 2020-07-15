# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.
import math


def trianglearea(s1, s2, s3):
    # your code goes here
    if max(s1, s2, s3) > (s1 + s2 + s3 - max(s1, s2, s3)):
        print(0)
        return 0
    per = (s1 + s2 + s3) / 2
    area = math.sqrt(per * (per - s1) * (per - s2) * (per - s3))
    print(area)
    return area
