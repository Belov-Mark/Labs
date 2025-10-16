from . import isTorn


def transpose(mat):
    if not mat:
        return []
    
    isTorn(mat)
    
    result = []
    for i in range(len(mat[0])):
        new_row = []
        for j in range(len(mat)):
            new_row.append(mat[j][i])
        result.append(new_row)
    
    return result


def row_sums(mat):
    if not mat:
        return []

    isTorn(mat)
    
    result = []
    for i in range(len(mat)):
        row_sum = 0
        for j in range(len(mat[i])):
            row_sum += mat[i][j]
        result.append(row_sum)
    
    return result


def col_sums(mat):
    if not mat:
        return []

    isTorn(mat)

    result = []
    for j in range(len(mat[0])):
        col_sum = 0
        for i in range(len(mat)):
            col_sum += mat[i][j]
        result.append(col_sum)
    
    return result
