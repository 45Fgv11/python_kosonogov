#Дано трехзначное число. Вывести вначале его последнюю цифру(единицы), а затем — его среднюю цифру (десятки).

#проверка
try:

    #ввод
    number = int(input("Введите трехзначное число: "))

    #нахождение
    last_digit: int = number % 10
    middle_digit = (number // 10) % 10
    print(last_digit)
    print(middle_digit)

except ValueError:
    print("что-то пошло не так")
