"""
Inheritance Example for the Employee and Dev class

"""


class Employee:
    raise_pay = 1.15

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@gmail.com"

    def details(self):
        print(f"{self.first} {self.last} {self.pay}")

    def apply_raise(self):
        # or Employee.raise_pay
        self.pay = int(self.pay * self.raise_pay)    

    # when you call the object
    def __str__(self):
        return f"{self.first} {self .last} - {self.pay}"


# By default the developer class will inherit all the methods and variables, as long as you dont override it;
# when you override it you need to call the super class method or variable if you need it, wont get called on its own
# See Example three to understand this in detail; basically its overiding
class Developer(Employee):    
    raise_pay = 1.30

    # all methods and variables are inheritance; No need to add this constructor also; but since we are adding extra
    # variable pgm_language we need to call the parent class constructor in childs and define the other variable
    def __init__(self, first, last, pay, pg_lang="Java"):  # default if nothing given then it will become as Java
        super().__init__(first, last, pay)             # dose'nt take self
       # Employee.__init__(self,first,last,pay); can also do this way
        self.pg_lang = pg_lang

    def details(self):
        super().details()
        # Employee.details(self)
        print("and the pgm_language ", self.pg_lang)


if __name__ == "__main__":
    emp1 = Employee('sujay', 'joshi', 120000)
    emp1.details()
    emp1.apply_raise()
    emp1.details()

    dev2 = Developer('mj', 'joshi', 120000, "c++")
    dev2.details()
    dev2.apply_raise()
    # raise_pay exists in dev class so its going to get form there itself, else would have got from the employee class
    dev2.details()

    # there was after implementing _str__
    print(emp1)
    print(str(emp1))
    print(emp1.__str__())
    print(emp1.__str__)
    print(dev2.__dict__)