class BankAcc:

    def __init__(self, pin):
        self.__balance = 0
        self.__pin = pin
        self.is_authentication = False

    def get_pin(self):
        if not self.is_authentication:
            self.is_authentication = self.__pin == int(input("Enter your pin: "))

    @property
    def acc(self):
        self.get_pin()
        if self.is_authentication:
            return self.__balance

    @acc.setter
    def acc(self, value):
        if self.is_authentication:
            self.__balance = value


my_acc = BankAcc(pin=1234)

my_acc.acc += 100
print(my_acc.acc)
