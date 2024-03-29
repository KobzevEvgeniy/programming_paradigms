if __name__ == '__main__':
    def multiplication_table(n):
        # Используем парадигму процедурного программирования
        # для простоты и понятности кода

        for i in range(1, n + 1):
            for j in range(1, 10):
                result = i * j
                print(f"{i} * {j} = {result}")


    # Пример использования
    test = int(input('Введите целое число: '))
    multiplication_table(test)

    """Обоснование выбора парадигмы
Выбор парадигмы зависит от конкретной задачи и её требований. В данном случае, использование процедурного 
программирования обосновано следующими причинами:

Простота и читаемость кода: Процедурное программирование предоставляет простую структуру, что делает код более 
читаемым и понятным, особенно для начинающих разработчиков.

Линейность задачи: Задача вывода таблицы умножения представляет собой линейную последовательность шагов, что
 соответствует простым процедурам.

Отсутствие необходимости в сложных структурах данных: Для данной задачи не требуются сложные структуры данных или
сложные взаимодействия между объектами, что характерно для объектно-ориентированного программирования.

В итоге, процедурное программирование обеспечивает достаточный уровень абстракции и простоты для эффективного
 решения данной конкретной задачи."""
