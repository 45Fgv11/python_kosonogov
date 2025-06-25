#В двумерном списке найти минимальный элемент в предпоследней строке

import random as r

matrix = [[r.randint(1, 10) for _ in range(3)] for _ in range(3)]

pre_last_row = matrix[-2]
min_element = min(pre_last_row)

print(f"Минимальный элемент в предпоследней строке: {min_element}")