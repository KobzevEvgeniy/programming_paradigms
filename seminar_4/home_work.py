import numpy as np


def pearson_correlation(x, y):
    # Функция для вычисления корреляции Пирсона между двумя массивами

    # Проверка на одинаковую длину массивов
    if len(x) != len(y):
        raise ValueError("Arrays must have the same length")

    n = len(x)

    # Сумма элементов массивов
    sum_x = sum(x)
    sum_y = sum(y)

    # Сумма квадратов элементов массивов
    sum_x_squared = sum(map(lambda xi: xi ** 2, x))
    sum_y_squared = sum(map(lambda yi: yi ** 2, y))

    # Сумма произведений элементов массивов
    sum_xy = sum(map(lambda xi, yi: xi * yi, x, y))

    # Формула корреляции Пирсона
    numerator = n * sum_xy - sum_x * sum_y
    denominator = np.sqrt((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2))

    # Проверка деления на ноль
    if denominator == 0:
        return 0.0
    else:
        correlation = numerator / denominator
        return correlation


# Пример использования
if __name__ == '__main__':
    array1 = [1, 2, 3, 4, 5]
    array2 = [1, 2, 40, 4, 5]

    result = pearson_correlation(array1, array2)
    print(f"Pearson correlation: {result}")
