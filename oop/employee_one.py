"""
Simple Employee class with methods and variables

Note: run the debugger and give point at z = 12; you will get a good picture on how the code is read by compiler
"""
z = 12


class Employee:
    # The below variables location, emp_count, raise_pay is shared amoung all the objects of the class
    # it basically belongs to the class
    _location = "New York"
    _emp_count = 0
    _raise_pay = 1.0

    # Constructor in Python,
    # As we know if there is underscore var, we should not change the val using var;
    # use getters and setters to change; Also some ppl follow that _var shouldn't be even changed
    # use __underscore if the subclass should'nt import these vars, but in Python they do :(
    def __init__(self, first, last, salary, age=43):
        self._first = first
        self._last = last
        self._salary = salary
        self._age = age
        # Can do is by using self._emp_count += 1; works the same way
        Employee._emp_count += 1

    def details(self):
        print("The name of the emp is {} {}, with salary and age {} {}".format(self._first, self._last,
                                                                               self._salary, self._age))

    # Since we are displaying static var, we can make it static method; so both class and object can use
    # This method can be called by class means we need no object to be instantiated
    @staticmethod
    def total_employees():
        print("current employee count is ", Employee._emp_count)

    def change_name(self, first, last):
        self._first = first
        self._last = last
        print("The name has been changed")

    def raise_pay_of_emp(self):
        self._salary = self._salary * Employee._raise_pay
        print("updated pay is", self._salary)

    # Class methods can be used to implement alternative constructor
    @classmethod
    def raise_pay_up(cls, by):
        Employee._raise_pay = by
        print("The raise pay has been increased to ", Employee._raise_pay)

    @staticmethod
    def is_it_leap_year(this_year):
        if this_year % 4 == 0:
            print("Its a leap year")
        else:
            print("Its not a leap year")

    # When say del on the obj this method is invoked
    def __del__(self):
        Employee._emp_count -= 1


def main():
    # Note total_employee is a static method, so it can be called before or without creating the objects of the class
    # while the other instance methods cannot be; same behaviour for class method as static method
    Employee.total_employees()
    Employee.raise_pay_up(1.00)
    print()

    my_emp = Employee(first="sujay", last="joshi", salary=20000, age=25)
    my_emp2 = Employee("john", "Ken", 12000, 29)
    my_emp3 = Employee("c", "Jackson", salary=12211)
    my_emp.details()
    my_emp.change_name("R3volve", "v2")
    my_emp.details()
    print()

    # Can call this total_employee method by class or object
    my_emp.total_employees()
    Employee.total_employees()
    print()

    # Calling the class method
    Employee.raise_pay_up(1.15)
    # The object can even call the class method, but not a good practice
    # my_emp.raise_pay_up(1.20)
    print()

    # Raising the pay of emp
    my_emp.raise_pay_of_emp()
    my_emp.details()
    print()

    my_emp2.details()
    del my_emp2
    # After calling del on the object the
    Employee.total_employees()
    print()

    # Can call static methods by both class and object
    Employee.is_it_leap_year(2018)

    my_emp3.is_it_leap_year(2020)
    print(my_emp3)
    print(str(my_emp3))
    print(my_emp3.__str__())
    print()

    # dictionary representation
    print(my_emp3.__dict__)


if __name__ == "__main__":
    main()