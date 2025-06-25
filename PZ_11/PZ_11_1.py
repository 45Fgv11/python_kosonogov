#1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов: Исходные данные:
#Количество элементов: Индекс последнего минимального элемента: Умножаем все элементы на первый элемент:

numbers = [5, -3, 10, -8, 2, -1, 15, -4, 0, 7]
with open('numbers.txt', 'w') as f:
    f.write(' '.join(map(str, numbers)))


with open('numbers.txt') as f:
    nums = list(map(int, f.read().split()))

count = len(nums)
min_index = len(nums) - nums[::-1].index(min(nums)) - 1
multiplied = [x * nums[0] for x in nums]


with open('result.txt', 'w') as f:
    f.write(f"""Исходные данные: {' '.join(map(str, nums))}
Количество элементов: {count}
Индекс последнего минимального элемента: {min_index}
Умножаем все элементы на первый элемент: {' '.join(map(str, multiplied))}""")