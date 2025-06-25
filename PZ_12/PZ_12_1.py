#1.В последовательности на n целых чисел найти и вывести:
#1. максимальный среди положительных
#2. минимальный среди отрицательных
#3. произведение элементов

def analyze_sequence(sequence):
    max_positive = max(filter(lambda x: x > 0, sequence), default=None)

    min_negative = min(filter(lambda x: x < 0, sequence), default=None)

    from functools import reduce
    product = reduce(lambda x, y: x * y, sequence, 1)

    return {
        "max_positive": max_positive,
        "min_negative": min_negative,
        "product": product
    }


numbers = [3, -5, 2, 10, -8, 0, 4, -1]
result = analyze_sequence(numbers)

print("Максимальный среди положительных:", result["max_positive"])
print("Минимальный среди отрицательных:", result["min_negative"])
print("Произведение элементов:", result["product"])