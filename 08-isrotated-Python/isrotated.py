# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g.
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
    # Your code goes here
    l = len(str2)
    if l != len(str1):
        return False
    l = l - 1
    for ele in range(0, round(len(str1) / 2)):
        print(str2[l])
        if str1[ele] != str2[l]:
            return False
        l -= 1
    return True


isrotated("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "BCDEFGHIJKLMNOPQRSTUVWXYZA")
