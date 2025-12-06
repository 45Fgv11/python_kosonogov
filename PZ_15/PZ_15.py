#Приложение УЧЕБНЫЙ ПЛАН для автоматизированного контроля учебной нагрузки по кафедре. Таблица Дисциплины должна иметь
#следующую структуру записи: Код дисциплины, Наименование дисциплины, Специальность, Лекции(кол-во часов),
#Практические (кол-во часов), Лабораторные (кол-во часов), Форма отчётности.
# Простое приложение "Учебный план" (консольная версия)
import sqlite3

con = sqlite3.connect("plan.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS lessons(
    code TEXT PRIMARY KEY,
    name TEXT,
    spec TEXT,
    lec INTEGER,
    prac INTEGER,
    lab INTEGER,
    exam TEXT
);
""")

data = [
    ("CS1", "Программирование", "Информатика", 36, 18, 18, "Экзамен"),
    ("CS2", "Алгоритмы", "Информатика", 45, 15, 0, "Зачёт"),
    ("DB1", "Базы данных", "Информатика", 30, 15, 0, "Экзамен"),
    ("MA1", "Математика 1", "Математика", 60, 0, 0, "Экзамен"),
    ("PH1", "Физика", "Физика", 40, 10, 10, "Экзамен"),
    ("OS1", "Операционные системы", "Информатика", 34, 16, 0, "Зачёт"),
    ("CH1", "Химия", "Химия", 28, 14, 8, "Зачёт"),
    ("EN1", "Английский", "Гуманитарные", 20, 20, 0, "Зачёт"),
    ("ML1", "Машинное обучение", "Информатика", 48, 12, 0, "Экзамен"),
    ("PR1", "Практикум", "Информатика", 10, 20, 0, "Зачёт")
]

cur.execute("SELECT COUNT(*) FROM lessons;")
if cur.fetchone()[0] == 0:
    cur.executemany("INSERT INTO lessons VALUES(?,?,?,?,?,?,?);", data)
    con.commit()

def search_code(c):
    return cur.execute("SELECT * FROM lessons WHERE code = ?;", (c,)).fetchall()

def search_name(n):
    return cur.execute("SELECT * FROM lessons WHERE name LIKE ?;", (f"%{n}%",)).fetchall()

def search_spec(s):
    return cur.execute("SELECT * FROM lessons WHERE spec = ?;", (s,)).fetchall()

def delete_code(c):
    cur.execute("DELETE FROM lessons WHERE code = ?;", (c,))
    con.commit()

def delete_spec(s):
    cur.execute("DELETE FROM lessons WHERE spec = ?;", (s,))
    con.commit()

def delete_no_lec():
    cur.execute("DELETE FROM lessons WHERE lec = 0;")
    con.commit()

def change_lec(c, h):
    cur.execute("UPDATE lessons SET lec = ? WHERE code = ?;", (h, c))
    con.commit()

def change_exam(n, e):
    cur.execute("UPDATE lessons SET exam = ? WHERE name = ?;", (e, n))
    con.commit()

def change_spec(c, s):
    cur.execute("UPDATE lessons SET spec = ? WHERE code = ?;", (s, c))
    con.commit()