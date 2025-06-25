#Дана строка. Подсчитать общее количество содержащихся в ней строчных
#латинских и русских букв.

s = "Hello! Привет! How are you? Как дела?"

latin_lower = sum(1 for c in s if 'a' <= c <= 'z')
russian_lower = sum(1 for c in s if 'а' <= c <= 'я')

print(f"Латинских строчных: {latin_lower}")
print(f"Русских строчных: {russian_lower}")
print(f"Всего строчных: {latin_lower + russian_lower}")