# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
    # your code goes here
    val = str(n)
    for ele in range(len(val) - 1):
        if val[ele] == val[ele + 1]:
            print("True")
            return True
    print("False")
    return False


hasconsecutivedigits(26011)
