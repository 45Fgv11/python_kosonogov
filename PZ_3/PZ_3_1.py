#Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно одно из чисел A, B, C положительное».

#ввод
A = int (input("Введите число A: "))
B = int (input("Введите число B: "))
C = int (input("Введите число C: "))
#нахождение
if A>0 and B<=0 and C<=0 or A<=0 and B>0 and C<=0 or A<=0 and B<=0 and C>0:
    print("Ровно одно из чисел положительное.")
else:
    print("Не одно или больше одного числа положительное ")