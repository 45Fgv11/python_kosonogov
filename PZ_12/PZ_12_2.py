#2.Составить генератор (yield), который выводит из строки только буквы.

def letters_generator(text):
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            yield char


text = "Hello, World! 123"
gen = letters_generator(text)

print("Буквы в строке:")
for letter in gen:
    print(letter, end=" ")