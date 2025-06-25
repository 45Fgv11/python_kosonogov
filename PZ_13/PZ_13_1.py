#В двумерном списке найти суммы элементов каждого столбца и поместить их в
#новый массив. Выполнить замену элементов второй строки исходной матрицы на
#полученные суммы.

import random as r
matrix = [[r.randint(1, 10) for _ in range(4)] for _ in range(4)]

column_sums = [sum(col) for col in zip(*matrix)]

matrix[1] = column_sums

print("Итоговая матрица:")
for row in matrix:
    print(row)