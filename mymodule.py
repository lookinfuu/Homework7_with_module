def check_int_number(x):
    """Проверяет правильность ввода.
    
    Ключевые аргументы:
        x -- какие-либо данные.

    Возвращает:
        number(x) -- результат всех
        проверок.

    """

    def view_bad_number(x):
        #Проверка на дробное число:
        if x.find('.') != -1 and x.count('.') == 1: 
            return f"{x} - дробное число."
        elif x:
            return f"{x} - не число."
        else:
            return "Вы ничего не ввели."

    def number(x):
        try:
            x = int(x)
        except ValueError:
            # Проверяем что привело к ошибке:
            return view_bad_number(x)
        except OverflowError:
            return "Число слишком большое."
        else:
            return x
    
    return number(x)


def check_float_number(x):
    try:
        x = float(x)
    except ValueError:
        return f"{x} - не число." if x else "Вы ничего не ввели."
    except OverflowError:
        return f"{x} - число слишком большое."
    else:
        return x


def read_file_b(road_to_file):
    try:
        with open(road_to_file, "rb") as f:
            f = f.read()
            return f
    except PermissionError:
        print("Недостаточно прав для работы с файлом.")
        return False
    except FileNotFoundError:
        print("Неверный путь к файлу или такого файла не существует.")
        return False


def write_file_b(road_to_file, text):
    try:
        with open(road_to_file, "wb") as f:
            f.write(text)
    except PermissionError:
        print("Недостаточно прав для работы с файлом.")
        return False
    except FileNotFoundError:
        print("Неверный путь к файлу или такого файла не существует.")
        return False
    else:
        return True
