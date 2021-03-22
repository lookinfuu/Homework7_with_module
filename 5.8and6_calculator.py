def calc(a=1, b=2, operation="+"):
    """Функция, которая выведет результат
    операции над "a" и "b"
    """
    """Выполнить действия над числами.
    
    Ключевые аргументы:
        a -- число, задается пользователем.
        b -- число, задается пользователем.
        operation -- операция, задается
        пользователем, далее определяет род
        операции над числами.

    Возвращает:
        selector[operation](a, b) -- из 
        словаря выбирается соответствующая
        операция по ключу и обращение к 
        функции по значению словаря с данным 
        ключем, которая в свою очередь
        принимает переменные "a" и "b"
    
    """
    def add(a1, b1):
        return a1 + b1

    def remove(a1, b1):
        return a1 - b1

    def multiply(a1, b1):
        return a1 * b1

    def divide(a1, b1):
        return a1 / b1

    def exponentiation(a1, b1):
        return a1 ** b1

    def sqrt(a1, b1):
        return b1 ** (1 / a1)
    
    def remofdiv(a1, b1):
        return a1 % b1

    selector = {
        "+": add,
        "-": remove,
        "*": multiply,
        "/": divide,
        "^": exponentiation,
        "sqrt": sqrt,
        "%": remofdiv
        }
 
    return selector[operation](a, b)


def main_calc():
    print("""*********   Калькулятор   ********* 
    Вводите ваш запрос в следующем виде:
    "число операция число"
    Пример правильного ввода: 3 * 7
    Доступные операции: 
    "+" - сложение 
    "-" - вычитание
    "*" - умножение
    "/" - деление
    "^" - возведение в степень
    "sqrt" - корень по основанию числа (2 sqrt 4 = 2)
    "%" - остаток от деления""")
    n = True
    while n:
        n = input("Введите ваш запрос (Enter - выход):")
        if n:
            ln = list(n.split())
            try:
                ln[0] = float(ln[0])
                ln[2] = float(ln[2])
            except ValueError:
                print("Проверьте правильность ввода.")
                continue
            except OverflowError:
                print("Числа слишком большие.")
                continue
            except IndexError:
                print("Проверьте правильность ввода и повторите снова.")
                continue
            # Проверяем список, не длинее ли он 3х элементов,
            # т.к. вид выражения: число операция число:
            if len(ln) == 3:
                # Проверяем 1 элемент списка, является ли
                # он операцией, доступной для вычислений:
                if (ln[1] == "+" or 
                    ln[1] == "-" or 
                    ln[1] == "*" or 
                    ln[1] == "/" or 
                    ln[1] == "^" or 
                    ln[1] == "sqrt" or 
                    ln[1] == "%"):
                    # Пробуем посчитать выражение:
                    try:
                        answer = calc(ln[0], ln[2], ln[1])
                    except ZeroDivisionError:
                        # Проверяем равенство нулевого элемента нулю,
                        # так как является исключением:
                        if ln[0] == 0:
                            print(f"{ln[0]} {ln[1]} {ln[2]} = indeterminate")
                        else:
                            # Если нулевой элемент не ноль, то результат,
                            # бесконечность:
                            print(f"{ln[0]} {ln[1]} {ln[2]} = inf")
                    except OverflowError:
                        print("Результат слишком большой.")
                    else:
                        # Все прошло успешно, выводим результат
                        # пользователю:
                        print(f"{ln[0]} {ln[1]} {ln[2]} = {answer:.2f}")
                else:
                    print(f"{ln[1]} - неизвестная операция.")
                    continue
            else:
                print("Проверьте правильность ввода и повторите снова.")
                continue
        else:
            print("Увидимся...")


main_calc()
