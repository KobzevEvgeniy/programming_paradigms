if __name__ == '__main__':

    def find_target_imperative(array_number, target):
        for el in array_number:
            if el == target:
                return True
        return False


    array = [1, 5, 7, 8, 9, 12, 45, 444]
    print(find_target_imperative(array, 12))


    def find_target_declarative(array, target):

        return target in array


    target = 100
    array = [1, 5, 7, 8, 9, 12, 45, 444]
    print(find_target_declarative(array, target))


    # Доля чисел в массиве чисел#
    def range_number_imperative(array_number_2):
        positive, negative, nulls = 0, 0, 0
        for el in array_number_2:
            if el == 0:
                nulls += 1
            if el > 0:
                positive += 1
            if el < 0:
                negative += 1
        return positive / len(array_number_2) * 100, nulls / len(array_number_2) * 100, negative / len(
            array_number_2) * 100


    print(range_number_imperative([1, 0, 0, 5, -7, -5, 100]))


    def range_number_declarative(array_number_3):
        positive = len(list(filter(lambda x: x > 0, array_number_3)))
        negative = len(list(filter(lambda x: x < 0, array_number_3)))
        zero = len(list(filter(lambda x: x == 0, array_number_3)))
        counts = [positive, negative, zero]
        shares = list(map(lambda x: x / len(array_number_3)*100, counts))
        return shares


    print(range_number_declarative([1, 0, 0, 5, -7, -5, 100]))
