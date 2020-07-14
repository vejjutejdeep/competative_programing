# isevenpositiveint(x)
# Write the function isevenpositiveint(x) that takes an arbitrary value x, return True if it is an
# integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not
# crashing if the value is not an integer. So, isevenpositiveint("yikes!") returns False (rather
# than crashing), and isevenpositiveint(123456) returns True.

def isevenpositiveint(x):
    # your code goes here
    string = isinstance(x, str)
    if string == True:
        print("False")
        return False
    check = str(x).isnumeric()
    if check == False:
        print("False")
        return False
    if x < 0:
        print("False")
        return False
    if x % 2 != 0:
        print("False")
        return False
    print("True")
    return True


isevenpositiveint(1)
