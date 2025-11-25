def min_max(nums):
    if not nums:
        raise ValueError("Список пуст — невозможно определить минимум и максимум.")

    min_val = max_val = nums[0]
    for n in nums[1:]:
        if n < min_val:
            min_val = n
        elif n > max_val:
            max_val = n
    return (min_val, max_val)


def unique_sorted(nums):
    unique = []
    for n in nums:
        exists = False
        for u in unique:
            if n == u:
                exists = True
                break
        if not exists:
            unique.append(n)

    n = len(unique)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if unique[j] > unique[j + 1]:
                unique[j], unique[j + 1] = unique[j + 1], unique[j]

    return unique


def flatten(mat):
    for row in mat:
        if type(row) not in (list, tuple):
            raise TypeError("Все элементы матрицы должны быть списками или кортежами.")

    result = []
    for row in mat:
        for el in row:
            result += [el]
    return result
