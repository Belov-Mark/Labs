n = int(input("Количество учеников: "))

count_offline = 0
count_online = 0

for _ in range(n):
    data = input().split()
    format_type = data[-1]
    
    if format_type == "True":
        count_offline += 1
    elif format_type == "False":
        count_online += 1

print(f"out: {count_offline} {count_online}")