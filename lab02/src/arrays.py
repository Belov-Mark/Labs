print("Тесты min_max")
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

tests = [
    [3, -1, 5, 5, 0],
    [42],
    [-5, -2, -9],
    [],
    [1.5, 2, 2.0, -3.1]
]

for array in tests:
    try:
        result = min_max(array)
        print(f"{array} - {result}")
    except ValueError as e:
        print(f"{array} - ValueError: {e}")

print("\n")


print("Тесты unique_sorted")

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

tests = [
    [3, 1, 2, 1, 3],
    [],
    [-1, -1, 0, 2, 2],
    [1.0, 1, 2.5, 2.5, 0],
]

for array in tests:
    try:
        result = unique_sorted(array)
        print(f"{array} - {result}")
    except ValueError as e:
        print(f"{array} - ValueError: {e}")

print("\n")


print("Тесты flatten")

def flatten(mat):
    for row in mat:
        if type(row) not in (list, tuple):
            raise TypeError("Все элементы матрицы должны быть списками или кортежами.")

    result = []
    for row in mat:
        for el in row:
            result += [el]
    return result

tests = [
    [[1, 2], [3, 4]],
    [[1, 2], (3, 4, 5)],
    [[1], [], [2, 3]],
    [[1, 2], "ab"],
]

for array in tests:
    try:
        result = flatten(array)
        print(f"{array} - {result}")
    except TypeError as e:
        print(f"{array} - TypeError: {e}")