# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value,
# which is the value of the middle element, or the average of the two middle elements if there is no single middle
# element. If the list is empty, return None.
import math


def median(a):
    # your code goes here
    if len(a) % 2 != 0:
        return a[len(a) // 2]
    print(len(a)/2)
    print(a[math.ceil(len(a) / 2)])
    me = (a[math.ceil(len(a) / 2)] + a[math.floor(len(a) / 2)]) / 2
    print(me)


median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
