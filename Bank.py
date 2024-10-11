class BankAccount:
    def __init__(self,balance):
        self.__balance = balance#приватная переменая
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print('Недостаточно средств')
    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
# account.__balance #вызовет ошибку,так как __balance приватная
# Этот код создает класс BankAccount,который позволяет хранить и преобразовывать баланс,
#Давайте разберем его поподробнее:
#1.Конструктор __init__
# При создании объекта класса BankAccount в него передается баланс(balance).Это значение
#сохраняется в приватеную переменную __balance.Приватная переменная означает,что она не
#доступна напрямую извне,что позволяет защитить внутренние данные класса от изменения
#2 метод deposit
#Этот метод добавляет что-то к balance,если сумма больше нуля
#3 метод withdraw
#Этот метод забирает весь balance , если  0 < amount <= self.__balance,то
# self.__balance -= amount , и тогда напишет 'Недостаточно средст'
#Таким образом,класс взависимости от суммы может добвить,может и отнять все.