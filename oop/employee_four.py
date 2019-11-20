# Here we utilizing getters and setters for the same Employee class; comes default with python

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last



emp_1 = Employee('John', 'Smith')


print("To get attribute first name: ", getattr(emp_1, 'first'))
print("To set a new first name for emp_1 ", setattr(emp_1, 'first', 'sujay'))
print("To check if name has been chanegd: ", getattr(emp_1, 'first') )
print("Check is lastname exists :", hasattr(emp_1, 'last'))
print("delet last name attribute: ", delattr(emp_1, 'first'))
print("check if first name exists: ", hasattr(emp_1, 'first'))



"""
Another way to things
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last


@property is used to get the value of a private attribute without using any getter methods. not sure for private
We have to put a line @property in front of the method where we return the private variable.

To set the value of the private variable, we use @method_name.setter in front of the method. We have to use it as a setter.
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


    @property                                       #needs to exist in order to make setters and getters for fullname
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    @fullname.setter
        def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None



emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)

print(emp_1.email)

print(emp_1.fullname)

del emp_1.fullname


When to use @property decorator?
When an attribute is derived from other attributes in the class, so the derived attribute will update whenever the source attributes is changed.
Normally this dosent happn, like say you have first and last name variables in a class, but the email is derived from first and lastname. email is not update after you change the last name
but here using @property decerotor it is updates
How to make a @property?
Make an attribute as property by defining it as a function and add the @property decorator before the fn definition.

When to define a setter method for the property?
Typically, if you want to update the source attributes whenever the property is set. It lets you define any other changes as well.
"""