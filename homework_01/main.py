"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if 1 < number < 4:
        return True
    else:
        for n in range(2, number):
            if number % n == 0:
                return False
            else:
                n += 1
    return True


def filter_numbers(num_list, filter_types):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_types == ODD:
        return [number for number in num_list if number % 2 != 0]
    if filter_types == EVEN:
        return [number for number in num_list if number % 2 == 0]
    if filter_types == PRIME:
        return [number for number in num_list if is_prime(number)]
