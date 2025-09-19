fio = input("ФИО: ").strip()

fio_clean = ' '.join(fio.split())

parts = fio_clean.split()
initials = ''.join([part[0].upper() for part in parts])

length = len(fio_clean)

print(f"Инициалы: {initials}.")
print(f"Длина: {length}")