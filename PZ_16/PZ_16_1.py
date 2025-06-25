#Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.Добавьте методы для вычисления
# процентных начислений и снятия денег

class Bank:
    def __init__(self, balance=0, rate=0):
        self.balance = balance
        self.rate = rate

    def interest(self):
        return self.balance * self.rate / 100

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Баланс: {self.balance:.2f}, Ставка: {self.rate}%"


if __name__ == "__main__":
    acc = Bank(1000, 5)
    print(acc)
    print(f"Проценты: {acc.interest():.2f}")
    print("Снятие успешно" if acc.withdraw(300) else "Недостаточно средств")
    print(acc)