# Write the function pascalsTriangleValue(row, col)
# that takes int values row and col, and returns the
# value in the given row and column of Pascal's
# Triangle where the triangle starts at row 0, and
# each row starts at column 0. If either row or col
# are not legal values, return None, instead of crashing.


def fun_pascaltrianglevalue(row, col):
    if (row < col):
        return 0
    a = []
    for ele in range(row + 1):
        a.append([])
        print(a)
        a[ele].append(1)
        for j in range(1, ele):
            a[ele].append(a[ele - 1][j - 1] + a[ele - 1][j])
        if (row != 0):
            a[ele].append(1)
        print(a)
    return a[row][col]


print(fun_pascaltrianglevalue(7, 4))
