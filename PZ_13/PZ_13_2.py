# В двумерном списке найти среднее арифметическое элементов последних двух
# столбцов.
import random
from functools import reduce
spisok = [[random.randint(1, 10) for i in range(4)] for i in range(4)]
for i in spisok:
    print(i)
a = list(map(lambda x: sum(x[-2:]), spisok))

b = reduce(lambda x,y: (x+y), a)
print(b / (len(a) * 2))