def format_record(rec):
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError("Запись должна быть кортежем из 3 элементов")

    fio, group, gpa = rec

    if not isinstance(fio, str):
        raise TypeError("ФИО должно быть строкой")
    if not isinstance(group, str):
        raise TypeError("Группа должна быть строкой")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должно быть числом")

    if not fio.strip():
        raise ValueError("ФИО не может быть пустым")
    if not group.strip():
        raise ValueError("Группа не может быть пустой")
    
    fio_parts = fio.split()

    surname = fio_parts[0].capitalize()

    initials = []
    for i in range(1, min(3, len(fio_parts))):
        name_part = fio_parts[i]
        if name_part:
            initial = name_part[0].upper() + "."
            initials.append(initial)

    formatted_fio = surname
    formatted_fio += " " + "".join(initials)

    formatted_group = group.strip()

    formatted_gpa = f"{gpa:.2f}"

    return f"{formatted_fio}, гр. {formatted_group}, GPA {formatted_gpa}"
