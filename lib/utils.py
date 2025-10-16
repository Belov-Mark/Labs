def isTorn(mat):
    row_length = len(mat[0])
    for i in range(len(mat)):
        if len(mat[i]) != row_length:
            raise ValueError("Рваная матрица")