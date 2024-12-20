#Дано целое число N (>0), являющееся некоторой степенью числа 2: N = 2K. Найти
#целое число K — показатель этой степени.

#Ввод числа N
N = int(input("Введите число N: "))

#Инициализация переменной K
K = 0

#Поиск показателя степени
while 2 ** K < N:
    K += 1

if 2 ** K == N:
    print(f"Число {N} является степенью двойки со значением показателя {K}")
else:
    print(f"Число {N} не является степенью двойки")