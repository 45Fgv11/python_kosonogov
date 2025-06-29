# Приложение РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ для автоматизированного
# контроля затрат на производство продукции. БД должна содержать таблицу Расходы со
# следующей структурой записи: Дата, Код продукта, Наименование продукта, Расходы,
# Сумма.

import sqlite3
from datetime import datetime


class ExpenseTracker:
    def __init__(self, db_name='production_expenses.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Расходы
                              (Дата TEXT, Код_продукта INTEGER, 
                               Наименование_продукта TEXT, 
                               Расходы TEXT, Сумма REAL)''')
        self.conn.commit()

    def add_expense(self, date, product_code, product_name, expense_type, amount):
        self.cursor.execute('''INSERT INTO Расходы 
                              VALUES (?, ?, ?, ?, ?)''',
                            (date, product_code, product_name, expense_type, amount))
        self.conn.commit()

    def get_all_expenses(self):
        self.cursor.execute("SELECT * FROM Расходы")
        return self.cursor.fetchall()

    def get_expenses_by_product(self, product_code):
        self.cursor.execute("SELECT * FROM Расходы WHERE Код_продукта=?", (product_code,))
        return self.cursor.fetchall()

    def get_total_expenses(self):
        self.cursor.execute("SELECT SUM(Сумма) FROM Расходы")
        return self.cursor.fetchone()[0]

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    tracker = ExpenseTracker()

    today = datetime.now().strftime("%Y-%m-%d")
    tracker.add_expense(today, 1, "Хлеб", "Мука", 1500.50)
    tracker.add_expense(today, 1, "Хлеб", "Дрожжи", 300.25)
    tracker.add_expense(today, 2, "Торт", "Сахар", 1200.75)

    print("Все расходы:")
    for row in tracker.get_all_expenses():
        print(row)

    print("\nРасходы по продукту с кодом 1:")
    for row in tracker.get_expenses_by_product(1):
        print(row)

    print(f"\nОбщая сумма расходов: {tracker.get_total_expenses():.2f}")

    tracker.close()