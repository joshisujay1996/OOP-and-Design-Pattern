"""
OOP inheritance testing
"""
class Employee:
    raise_pay = 1.00

    def __init__(self, salary):
        self.salary = salary

    def raise_pay_by(self, by_val):
        self.salary = by_val * self.salary


class Developer(Employee):
    def __init__(self, salary, lang):
        # Employee.__init__(self, salary)
        super().__init__(salary)
        self.lang = lang


my_dev = Developer(1212, "C#")
print(Developer.raise_pay)
my_dev.raise_pay_by(10)
print(my_dev.salary)
