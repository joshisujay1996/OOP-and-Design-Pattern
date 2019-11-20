"""
Class Methods vs. Static Methods and Instance Methods
"""

"""
class Pet:
    _class_info = "pet animals"

    def about(self):
        print("This class is about " + self._class_info + "!")   
    

class Dog(Pet):
    _class_info = "man's best friends"

class Cat(Pet):
    _class_info = "all kinds of cats"

p = Pet()
p.about()
d = Dog()
d.about()
c = Cat()
c.about()

--------------------------------------------------------------------
This program creates the following output:
This class is about pet animals!
This class is about man's best friends!
This class is about all kinds of cats!
This may look alright at first at first glance. On second thought we recognize the awful design. 
We had to create instances of the Pet, Dog and Cat classes to be able to ask what the class is about. 
It would be a lot better, if we could just write "Pet.about()", "Dog.about()" and "Cat.about()" 
to get the previous result. We cannot do this. 
We will have to write "Pet.about(p)", "Dog.about(d)" and "Cat.about(c)" instead.


Now concider using static methods
class Pet:
    _class_info = "pet animals"

    @staticmethod
    def about():
        print("This class is about " + Pet._class_info + "!")   
    

class Dog(Pet):
    _class_info = "man's best friends"

class Cat(Pet):
    _class_info = "all kinds of cats"

Pet.about()
Dog.about()
Cat.about()
--------------------------------------------------------------------
We get the following output:

This class is about pet animals!
This class is about pet animals!
This class is about pet animals!

Which is a problem again
Therefore lets choose Class method

class Pet:
    _class_info = "pet animals"

    @classmethod
    def about(cls):
        print("This class is about " + cls._class_info + "!")   
    

class Dog(Pet):
    _class_info = "man's best friends"

class Cat(Pet):
    _class_info = "all kinds of cats"

Pet.about()
Dog.about()
Cat.about()
--------------------------------------------------------------------
We get the following output:
his class is about pet animals!
This class is about man's best friends!
This class is about all kinds of cats!
"""



# If you dont wnat to use class method you can do it thi way too


class Pets:
    _class_info = "pet animals"

    @staticmethod
    def about():
        print("This class is about " + Pets._class_info + "!")


class Dog(Pets):
    _class_info = "man's best friends"

    @staticmethod
    def about():
        print("This class is about " + Dog._class_info + "!")


p = Pets()
p.about()

d = Dog()
d.about()