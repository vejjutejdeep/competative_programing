# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
    two = list(s3)
    main = list(s1)
    count = 0
    for i in range(len(s1)):
        if main[i] in s2:
            main[i] = two[count]
            count += 1
    s = str(main)
    print(s)
