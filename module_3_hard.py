def calculate_structure_sum(data):
    total_sum = 0

    for element in data:
        if isinstance(element, int):  # Если элемент - целое число
            total_sum += element
        elif isinstance(element, str):  # Если элемент - строка
            total_sum += len(element)
        elif isinstance(element, list) or isinstance(element, tuple):  # Если элемент - список или кортеж
            total_sum += calculate_structure_sum(element)  # Рекурсивный вызов
        elif isinstance(element, dict):  # Если элемент - словарь
            total_sum += calculate_structure_sum(element.values())  # Рекурсивный вызов с значениями словаря
            total_sum += calculate_structure_sum(element.keys())  # Рекурсивный вызов с ключами словаря
        elif isinstance(element, set):  # Если элемент - множество
            total_sum += calculate_structure_sum(element)  # Рекурсивный вызов для множества
        # Если элемент другого типа, пропускаем его

    return total_sum


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Ожидаемый вывод: 99


