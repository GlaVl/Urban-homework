def get_matrix(n, m, value):
    matrix = []
    for i in range(n):  # внешний цикл добавления столбцов (списков) в матрицу (список)
        list_ = []  # создаем список под столбец, обнуляем его при каждом цикле
        for j in range(m):  # цикл добавления элементов в столбец
            list_.append(value)
        matrix.append(list_)  # добавляем список (столбец) в матрицу (список)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
