"""
Ввод: price (₽), discount (%), vat (%) — вещественные.
Формулы:
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
Вывод: по строкам, 2 знака после запятой.
"""

price = float(input("Цена: "))
discount = float(input("Скидка: "))
vat = float(input("НДС: "))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} ₽")
print(f"НДС: {vat_amount:.2f} ₽")
print(f"Итого к оплате: {total:.2f} ₽")
