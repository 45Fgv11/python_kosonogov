#Дана строка. Подсчитать общее количество содержащихся в ней строчных
#латинских и русских букв.

def count_lower_letters(s):
    # Считаем только строчные буквы
    lower_latin = 'abcdefghijklmnopqrstuvwxyz'
    lower_russian = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    count: int = 0
    for char in s:
        if (char in lower_latin) or (char in lower_russian):
            count += 1

    return count
 count_lower_letters(s)