# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g.
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
    # Your code goes here
    if len(str2) != len(str1):
        return False
    temp = str1 + str1
    print(str2)
    print(temp.count(str2))
    if temp.count(str2) > 0:
        return True
    else:
        return False


print(isrotated('12345', '54321'))
