# Программа, которая запрашивает набор чисел и вычисляет желаемую метрику в описательной статистике. 

import numpy as np

# Входные данные
data = input("Введите числовой набор через пробелы \n").split()

# Обработка
new_data = []

for el in data:
    if el != " ":
        new_data.append(el)

# Преобразуем все элементы списка в вещественные числа
numbers = np.array(new_data, dtype=float)

# Основная логика программы
while True:
    print("\n ----------Statistical calculator version 0.0.1---------- \n")
    print("Вы хотите продолжить?")
    calc_continue = input('Введите "да" или "нет" \n').lower()

    if calc_continue == "нет":
        break
    elif calc_continue == "да":
        print("\n Выберите статистическую метрику из списка:")
        metric = input("""медиана, среднее, максимум, минимум, размах, дисперсия, стандартное отклонение \n""")
        metric = metric.lower()

        if metric == "медиана":
            print()
            print(f"Медиана: {np.median(numbers)}")
        elif metric == "среднее":
            print()
            print(f"Среднее: {np.mean(numbers)}")
        elif metric == "максимум":
            print()
            print(f"Максимум: {np.max(numbers)}")
        elif metric == "минимум":
            print()
            print(f"Минимум: {np.min(numbers)}")
        elif metric == "размах":
            print()
            print(f"Размах: {np.max(numbers) - np.min(numbers)}")
        elif metric == "дисперсия":
            print()
            print(f"Дисперсия: {np.var(numbers)}")
        elif metric == "стандартное отклонение":
            print()
            print(f"Стандартное отклонение: {np.std(numbers)}")
