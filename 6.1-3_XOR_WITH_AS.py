import mymodule
import random
import string


def key(text):
    key = input("Введите ключ (Enter - ключ будет создан автоматически):")
    if not key:
        # numsymbl включает в себя цифры, английские строчные и заглавные букв.
        numsymbl = string.digits + string.ascii_letters
        # Создаем ключ в одну строку, объединяя каждый элемент ключа, который
        # берется случайным образом из numsymbl. Ключ будет длинной от 1 до
        # длины текста 
        key = "".join(random.choice(numsymbl) 
              for i in range(random.randint(1, len(text))))
        print(f"Ключ был создан автоматически:{key}")
    # Преобразуем ключ к битовому представлению
    key = bytearray(key, "utf-8")
    return key

def XOR_code(text, key):
    xor_code = bytearray()
    # Для каждого символа в тексте, мы совершаем преобразование
    # операцией "^" - xor
    for i in range(len(text)):
        xor_code.append(text[i] ^ key[i % len(key)])
    return xor_code

def XOR():
    print("****  XOR-шифрование  ****\nДля выхода введите:\"выход\"")
    road_to_file = ""
    while road_to_file.lower() != "выход":
        road_to_file = input("Укажите путь к файлу:\n")
        if road_to_file.lower() != "выход":
            text = input("Введите текст (Enter - взять данные из файлы):")
            # Проверяем ввел ли что-то пользователь, если нет,
            # то читаем данные из файла пользуясь mymodule 
            if not text:
                text = mymodule.read_file_b(road_to_file)
                # Если текст так и нет, то возвращаемся в начало цикла
                if not text:
                    continue
            # Если пользователь что-то ввел, то преобразуем
            # текст к бинарному представлению 
            else:
                text = bytearray(text, "utf-8")
            xor = XOR_code(text, key(text))
            # Создаем флаг, для проверки записи в файл,
            # модуль mymodule вернет False и уведомит об ошибке
            # пользователя, если что-то пошло не так
            flag = mymodule.write_file_b(road_to_file, xor)
            if not flag:
                continue
            else:
                print("Успешно. Результат записан в файл.")

XOR()
