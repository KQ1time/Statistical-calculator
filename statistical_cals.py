# Программа, которая запрашивает набор чисел и вычисляет желаемую метрику в описательной статистике. 

import numpy as np

# Входные данные
data = input("Введи числовой набор через пробелы \n").split(sep=" ")

# Преобразуем все элементы списка в вещественные числа
numbers = np.array(data, dtype=float)

# Основная логика программы
while True:
    print("Вы хотите продолжить?")
    calc_continue = input('Введите "да" или "нет" \n').lower()

    if calc_continue == "нет":
        break
    elif calc_continue == "да":
        print("Выберите статистическую метрику из списка:")
        metric = input("""медиана, среднее, максимум, минимум, размах, дисперсия, стандартное отклонение \n""")
        metric = metric.lower()

        if metric == "медиана":
            print(f"Медиана: {np.median(numbers)}")
        elif metric == "среднее":
            print(f"Среднее: {np.mean(numbers)}")
        elif metric == "максимум":
            print(f"Максимум: {np.max(numbers)}")
        elif metric == "минимум":
            print(f"Минимум: {np.min(numbers)}")
        elif metric == "размах":
            print(f"Размах: {np.max(numbers) - np.min(numbers)}")
        elif metric == "дисперсия":
            print(f"Дисперсия: {np.var(numbers)}")
        elif metric == "стандартное отклонение":
            print(f"Стандартное отклонение: {np.std(numbers)}")

        continue
    else:
        continue
