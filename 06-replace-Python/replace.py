# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
    two = list(s3)
    main = list(s1)
    count = 0
    lis = []
    for i in range(len(main) - 1):
        if main[i] in s2:
            if len(two) > count:
                main[i] = two[count]
                count += 1
            else:
                lis.append(main[i])
    print(lis)
    if len(lis) != 0:
        for ele in lis:
            main.pop(ele)
    s = str(main)
    print(s)


fun_replace("helloworld123", "hello", "345")
