def calculate_structure_sum(*args):
    total_sum = 0  # объявляем переменную для хранения общей суммы
    for i in args:  # перебираем все элементы структуры
        # если элемент является числом, то прибавляем его к общей сумме
        if isinstance(i, (int, float)):
            total_sum += i
        # если элемент является строкой, то прибавляем его длину к общей сумме
        elif isinstance(i, str):
            total_sum += len(i)
        # если элемент является списком, кортежем или множеством, то мы рекурсивно вызываем функцию
        # calculate_structure_sum, результат выполнения функции добавляем к общей сумме
        elif isinstance(i, (list, tuple, set)):
            total_sum += calculate_structure_sum(*i)
        # если элемент является словарем, то мы рекурсивно вызываем функцию
        # calculate_structure_sum для каждой пары ключ-значение и результат выполнения функции добавляем к общей сумме
        elif isinstance(i, dict):
            for key, value in i.items():
                total_sum += calculate_structure_sum([key, value])
    return total_sum


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
