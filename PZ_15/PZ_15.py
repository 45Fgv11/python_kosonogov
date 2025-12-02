#Приложение УЧЕБНЫЙ ПЛАН для автоматизированного контроля учебной нагрузки по кафедре. Таблица Дисциплины должна иметь
#следующую структуру записи: Код дисциплины, Наименование дисциплины, Специальность, Лекции(кол-во часов),
#Практические (кол-во часов), Лабораторные (кол-во часов), Форма отчётности.
import os
import sqlite3 as sq

os.makedirs('PZ15', exist_ok=True)

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

    cursor.execute('SELECT COUNT(*) FROM Disciplines')
    if cursor.fetchone()[0] == 0:
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
        for rec in discipline:
            cursor.execute('''
                INSERT INTO Disciplines 
                (Discipline_code, Name_discipline, Specialization, Lectures, Practical, Laboratory, Reporting_form)
                VALUES (?, ?, ?, ?, ?, ?, ?)''', rec)

    print("\nВсе позиции в таблице:")
    cursor.execute('SELECT * FROM Disciplines')
    for row in cursor.fetchall():
        print(row)

    print("\n Дисциплины с лабораторными > 15 и название 'Прикладная':")
    cursor.execute("SELECT * FROM Disciplines WHERE Laboratory > 15 AND Name_discipline = 'Прикладная'")
    for row in cursor.fetchall():
        print(row)

    print("\nГуманитарные дисциплины с лекциями > 25:")
    cursor.execute("SELECT * FROM Disciplines WHERE Name_discipline = 'Гуманитарная' AND Lectures > 25")
    for row in cursor.fetchall():
        print(row)

    print("\nДисциплины в форме 'Экзамен':")
    cursor.execute("SELECT * FROM Disciplines WHERE Reporting_form = 'Экзамен'")
    for row in cursor.fetchall():
        print(row)