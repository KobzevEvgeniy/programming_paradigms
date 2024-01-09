if __name__ == '__main__':
    # ИМПЕРАТИВНЫЙ ПОДХОД
    def sort_list_imperative(numbers):

        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] < numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return numbers


    # ДЕКЛАРАТИВНЫЙ ПОДХОД
    def sort_list_declarative(numbers):
        return sorted(numbers, reverse=True)


    numbers_list = [4, 8, 7, 9, 5, 71, 42, 4, 5]

    print("Императивный подход:  ", sort_list_imperative(numbers_list))
    print("Декларативный подход: ", sort_list_declarative(numbers_list))
