import random
import string
import mymodule
from mymodule import read_file_b, write_file_b


def key(text):
    """Создает ключ.

    Ключевые аргументы:
        text -- строка, задается пользователем или
        берется из файла.

    Возвращает:
        key -- ключ, который будет использован для
        шифрования/расшифрования.
    
    """
    key = input("Введите ключ (Enter - ключ будет создан автоматически):")
    if not key:
        # numsymbl включает в себя цифры, английские строчные и заглавные буквы:
        numsymbl = string.digits + string.ascii_letters
        # Создаем ключ в одну строку, объединяя каждый элемент ключа, который
        # берется случайным образом из numsymbl. Ключ будет длинной от 1 до
        # длины текста:
        key = "".join(random.choice(numsymbl) 
              for i in range(random.randint(1, len(text))))
        print(f"Ключ был создан автоматически:{key}")
    key = bytearray(key, "utf-8")
    return key


def XOR_code(text, key):
    """Делает XOR-шифрование.

    Ключевые аргументы:
        text -- строка, задается пользователем или
        берется из файла.
        key -- ключ, задается пользователем или
        создается программой.

    Возвращает:
        xor_code -- зашифрованный текст.
    
    """
    xor_code = bytearray()
    for i in range(len(text)):
        # Cовершаем преобразование операцией "^" - xor:
        xor_code.append(text[i] ^ key[i % len(key)])
    return xor_code


def XOR():
    print("****  XOR-шифрование  ****\nДля выхода введите:\"выход\"")
    road_to_file = ""
    while road_to_file.lower() != "выход":
        road_to_file = input("Укажите путь к файлу:\n")
        if road_to_file.lower() != "выход":
            text = input("Введите текст (Enter - взять данные из файлы):")
            if not text:
                # Читаем данные из файла пользуясь mymodule:
                text = read_file_b(road_to_file)
                if not text:
                    continue
            else:
                # Пользователь что-то ввел, преобразуем
                # текст к бинарному представлению:
                text = bytearray(text, "utf-8")
            xor = XOR_code(text, key(text))
            # Создаем флаг, для проверки записи в файл,
            # модуль mymodule вернет False и уведомит об ошибке
            # пользователя, если что-то пошло не так:
            flag = write_file_b(road_to_file, xor)
            if not flag:
                continue
            else:
                print("Успешно. Результат записан в файл.")


XOR()
