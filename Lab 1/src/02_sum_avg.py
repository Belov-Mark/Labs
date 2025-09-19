num1 = float(input("a: ").replace(',', '.'))
num2 = float(input("b: ").replace(',', '.'))

total = num1 + num2
average = total / 2

print(f"sum = {total:.2f}; avg = {average:.2f}")