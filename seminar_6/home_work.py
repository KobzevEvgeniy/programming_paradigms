"""БИНАРНЫЙ ПОИСК"""


def binary_search(array, number):
    left = 0
    right = len(array) - 1
    while left <= right:
        centre = (left + right) // 2
        min_number = array[centre]
        if min_number == number:
            return centre
        elif min_number < number:
            left = centre + 1
        else:
            right = centre - 1
    return -1


if __name__ == '__main__':
    arr = [1, 5, 7, 8, 9, 12, 45, 444]
    x1 = 9
    x2 = 45
    x3 = 444
    x4 = 12
    print(arr)
    print(f"Индекс искомого элемента {x1} : {binary_search(arr, x1)}")
    print(f"Индекс искомого элемента {x2} : {binary_search(arr, x2)}")
    print(f"Индекс искомого элемента {x3} : {binary_search(arr, x3)}")
    print(f"Индекс искомого элемента {x4} : {binary_search(arr, x4)}")
