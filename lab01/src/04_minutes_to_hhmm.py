"""
Ввод: m — целые минуты.
Вывод: ЧЧ:ММ минуты вывести как {min:02d}.
"""

minutes = int(input("Минуты: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{hours:02d}:{remaining_minutes:02d}")