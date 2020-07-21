# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
    # Your code goes here
    lis = ""
    for ele in text:
        if ele not in lis:
            lis += ele
    print(lis)
    return lis


removeduplicate("Helloworld")
