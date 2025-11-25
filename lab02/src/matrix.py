def isTorn(mat):
    row_length = len(mat[0])
    for i in range(len(mat)):
        if len(mat[i]) != row_length:
            raise ValueError("Рваная матрица")


print("Тесты transpose")


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


tests = [[[1, 2, 3]], [[1], [2], [3]], [[1, 2], [3, 4]], [], [[1, 2], [3]]]

for array in tests:
    try:
        result = transpose(array)
        print(f"{array} - {result}")
    except ValueError as e:
        print(f"{array} - ValueError: {e}")

print("\n")


print("Тесты row_sums")


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


tests = [[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]]

for array in tests:
    try:
        result = row_sums(array)
        print(f"{array} - {result}")
    except ValueError as e:
        print(f"{array} - ValueError: {e}")

print("\n")


print("Тесты col_sums")


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


tests = [[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]]

for array in tests:
    try:
        result = col_sums(array)
        print(f"{array} - {result}")
    except ValueError as e:
        print(f"{array} - ValueError: {e}")
