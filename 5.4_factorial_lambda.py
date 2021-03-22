from functools import reduce

import mymodule
from mymodule import check_int_number


def number_in():
    """Проверит соответствие введенных данных
    классу int.
    
    Возвращает:
        x -- число типом int.
    
    """
    while True:
        x = input("Введите число:")
        x = check_int_number(x)
        if type(x) == int:
            if x < 0:
                print("Число должно быть положительным.")
                continue
            else:
                return x
        else:
            print(x)


def factorial_norec():
    """Вычисляем факториал числа без использования рекурсии"""
    print("*********   Вычисление факториала числа (не рекурсия)   *********")
    step = lambda a: [i for i in range(1,a + 1)]
    x = number_in()
    # Проверяем на ноль, исключение: факториал нуля = единице:
    if x != 0:
        sp = step(x)
        # Применяет указанную reduce к элементам последовательности, 
        # сводя её к единственному значению, которое является результатом 
        # вычислений факториала:
        factorial = reduce(lambda c, d: c * d, sp)
        print(f"{x}! = {factorial}")
    else:
        print(f"{x}! = 1")


factorial_norec()
