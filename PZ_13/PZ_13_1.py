# В двумерном списке элементы кратные 3 увеличить в 3 раза.
import random
spisok = [[random.randint(1, 10) for i in range(3)] for i in range(3)]
for i in spisok:
    print(i)
spisok = list(map(lambda y: list(map(lambda x: x * 3 if x % 3 == 0 else x, y)), spisok))

print(spisok)