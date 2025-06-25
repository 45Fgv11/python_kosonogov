#Сгенерировать словарь вида {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216},
#удалить из него первый и последний элементы. Отобразить исходный и
#получившийся словарь. Использовать for, range.

#Генерация исходного словаря
original_dict = {}
for i in range(7):
    original_dict[i] = i ** 3

#Создание копии словаря для удаления элементов
modified_dict = original_dict.copy()

if len(modified_dict) > 0:
    del modified_dict[0]
    del modified_dict[max(modified_dict.keys())]

#Вывод результатов
print("Исходный словарь:", original_dict)
print("Изменённый словарь:", modified_dict)