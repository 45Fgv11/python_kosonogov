# Приложение РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ для автоматизированного
# контроля затрат на производство продукции. БД должна содержать таблицу Расходы со
# следующей структурой записи: Дата, Код продукта, Наименование продукта, Расходы,
# Сумма.

import sqlite3 as sq

with sq.connect('PZ15/curriculum.db') as con:
    cursor = con.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Disciplines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Discipline_code TEXT,
            Name_discipline TEXT,
            Specialization TEXT,
            Lectures INTEGER,
            Practical INTEGER,
            Laboratory INTEGER,
            Reporting_form TEXT
        )
    ''')

    discipline = [
        ('0a1', 'Гуманитарная', 'Архитектура', 38, 20, 10, 'Курсовая работа'),
        ('0b2', 'Общественная', 'Социология', 25, 15, 10, 'Эссе'),
        ('0c3', 'Прикладная', 'Журналистика', 35, 15, 20, 'Курсовая работа'),
        ('0d4', 'Естественная', 'Химия', 20, 10, 10, 'Экзамен'),
        ('0e5', 'Гуманитарная', 'Философия', 27, 10, 20, 'Зачёт'),
        ('0f6', 'Формальная', 'Математика', 25, 15, 10, 'Экзамен'),
        ('0g7', 'Общественная', 'Политология', 20, 10, 10, 'Зачёт'),
        ('0h8', 'Естественная', 'Физика', 25, 10, 15, 'Экзамен'),
        ('0i9', 'Гуманитарная', 'История', 22, 20, 10, 'Эссе'),
        ('j10', 'Прикладная', 'Инженеринг', 25, 15, 15, 'Курсовая работа')
    ]

    # cursor.executemany('''
    #     INSERT INTO Disciplines (Discipline_code, Name_discipline, Specialization, Lectures, Practical, Laboratory, Reporting_form)
    #     VALUES (?, ?, ?, ?, ?, ?, ?)
    # ''', discipline)



with sq.connect('PZ15/curriculum.db') as con:
    cursor = con.cursor()

    cursor.execute('SELECT * FROM Disciplines')
    print("Все позиции в таблице:")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT * FROM Disciplines WHERE Laboratory > 15 AND Name_discipline = 'Прикладная'")
    print("\nВсе прикладные дисциплины, у которых на лабораторные отведено больше 15 часов: ")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT * FROM Disciplines WHERE Name_discipline = 'Гуманитарная' AND Lectures > 25")
    print("\nВсе гуманитарные дисциплины, у которых на Лекции отведено больше 25 часов:")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT * FROM Disciplines WHERE Reporting_form = 'Экзамен'")
    print("\nВсе дисциплины, сдающиеся в форме экзамена:")
    for row in cursor.fetchall():
        print(row)


with sq.connect('PZ15/curriculum.db') as con:
    cursor = con.cursor()

    cursor.execute("UPDATE Disciplines SET Reporting_form = 'Эссе' WHERE Name_discipline = 'Общественная'")
    cursor.execute("UPDATE Disciplines SET Reporting_form = 'Курсовая работа' WHERE Specialization = 'История'")
    cursor.execute("UPDATE Disciplines SET Practical = 15 WHERE  Lectures < 25")
    cursor.execute('SELECT * FROM Disciplines')
    print("\nВсе позиции в таблице после update:")
    for row in cursor.fetchall():
        print(row)


with sq.connect('PZ15/curriculum.db') as con:
    cursor = con.cursor()

    cursor.execute("DELETE FROM Disciplines WHERE Lectures < 25")
    cursor.execute("DELETE FROM Disciplines WHERE Specialization = 'Математика'")
    cursor.execute("DELETE FROM Disciplines WHERE Reporting_form = 'Экзамен'")

    cursor.execute('SELECT * FROM Disciplines')
    print("\nВсе позиции в таблице после удаления:")
    for row in cursor.fetchall():
        print(row)