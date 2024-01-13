# Count IF надо написать программу на вход получаем массив Li И число n.
# Программа считает кол-во чисел равных n

if __name__ == '__main__':
    """Структурная реализация"""
    li = [1, 5, 4, 8, 1, 4, 5, 2, 7, 1, 2, 0, 0, 0, 0, 0]
    n = 0
    count = 0
    for el in li:
        if el == n:
            count += 1
    print(count)

    """Процедурная реализация"""


    def count_if(arr, n):
        count = 0
        for el in arr:
            if el == n:
                count += 1
        return count


    li = [1, 5, 4, 8, 1, 4, 5, 2, 7, 1, 2, 0, 0, 0, 0, 0]
    n = 0
    print(count_if(li, n))

    """Сортировка пузыоьком"""

    def sort_buble(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


    li = [1, 5, 4, 8, 1, 4, 5, 2, 7, 1, 2, 0, 0, 0, 0, 0]
    print(sort_buble(li))
