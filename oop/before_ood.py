"""
Read through, run separately if needed
"""

"""
What Are Namespaces?

A namespace is basically a system to make sure that all the names in a program are unique and
can be used without any conflict. You might already know that everything in Python—like strings, lists, functions, etc.
—is an object. Another interesting fact is that Python implements namespaces as dictionaries.
There is a name-to-object mapping, with the names as keys and the objects as values.
Multiple namespaces can use the same name and map it to a different object. Here are a few examples of namespaces:

Local Namespace: This namespace includes local names inside a function.
This namespace is created when a function is called, and it only lasts until the function returns.

Global Namespace: This namespace includes names from various imported modules that you are using in a project.
It is created when the module is included in the project, and it lasts until the script ends.

Built-in Namespace: This namespace includes built-in functions and built-in exception names.
"""


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)


"""
Output of the above snippet is :

After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
"""


# Nonlocal Variables
# Nonlocal variable are used in nested function whose local scope is not defined.
# This means, the variable can be neither in the local nor the global scope.

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
# print(x)  # see x cant exists here, btw global would have if it was defined; see above example
# The above line print(x) gives an err (NameError if it's uncommented)


"""
Classes and Objects below

Basic OOD Example
In python everything is derived from a class and they have their own methods, like List, tuple, int, float, etc
Everything is an Object in PY and they have there own methods and attributes

we create instance out of the list class or tuple or etc
pop, append,__str__, remove are methods of th list class

"""


class MyEmployee:
    def __int__(self):
        pass


MyEmployee.branch = "NY"   # will be attached to all the objects fo the class
my_emp = MyEmployee()

my_emp.name = "sujay"
my_emp.age = 23

print(my_emp.branch)   # the branch data is attached to all the objects fo the MyEMployee class
print("printing my_emp", my_emp)

print("printing in dic format \t", my_emp.__dict__) # See branch data is not shown on the dic output;
# since its a class instance var not a obj instance var, its same for every object of MyEmployee

print("Printing the MyEmployee class dic \n", MyEmployee.__dict__)


"""
__str__ : used to give string representation of the object
similarly __repr__; read about it for more detail
"""


"""
Example 2
"""
class MyClass:
    def __init__(self, x):
        self.x = x

my_cls = MyClass(5)
print(my_cls.x)
del my_cls.x
print(my_cls)
# print(my_cls.x)       # will give err that var does not exist
my_cls.x = 21
my_cls.y = 32           # you can add new instance variables to class too
print(my_cls.x)         # now reassigned it a val


# The __init__ is a constructor
# self behaves like this in java


"""
Example 3
"""
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


"""
Example 4
"""


class Dog1:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog1('Fido')
e = Dog1('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)                # unexpectedly shared by all dogs


# Therefore, correct design should look like this!!
class Dog2:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


"""
Private, Protected, Public
 
classes are not usable to implement pure abstract data types. 
In fact, nothing in Python makes it possible to enforce data hiding — it is all based upon convention. 
(On the other hand, the Python implementation, written in C, can completely hide implementation details and
 control access to an object if necessary; this can be used by extensions to Python written in C.)
 
 What do these actually mean:
 
 Public: All member variables and methods are public by default in Python.
         So when you want to make your member public, you just do nothing. Example Below
            class Cup:
                def __init__(self):
                    self.color = None
                    self.content = None
            
                def fill(self, beverage):
                    self.content = beverage
            
                def empty(self):
                    self.content = None
         
         
         
 Protected: Protected member is (in C++ and Java) accessible only from within the class and it’s subclasses. 
            (also, any class in the same package as per Java)
            
            How to accomplish this in Python? The answer is – by convention. 
            By prefixing the name of your member with a single underscore, you’re telling others “don’t touch this, 
            unless you’re a subclass”. See the example below:
            
                class Cup:
                def __init__(self):
                    self.color = None
                    self._content = None # protected variable
            
                def fill(self, beverage):
                    self._content = beverage
            
                def empty(self):
                    self._content = None
                    
            Same example as before, but the content of the cup is now protected. This changes virtually nothing, 
            you’ll still be able to access the variable from outside the class, only if you see something like this:

                cup = Cup()
                cup._content = "tea"
                
            you explain politely to the person responsible for this, 
            that the variable is protected and he should not access it or even worse, change it from outside the class.
            
            So as we see Python does not provide the protectively like Java or C++
            The above way of making protected is just a convention followed by python guys !! 
            (its basically does nothing internally)
            
            
            
 Private: Private in Java or C++ means can be accesed inside the class only, neither subclass or package can access
          How do you do it in Python ?
          Note: In java or C++, the sub class can call the super class method and 
          the super class method can access the data for for you 
          
          If you want to emulate private variables for some reason, you can always use the __ prefix from PEP 8. 
          Python mangles the names of variables like __foo so that they're not easily visible to code outside 
          the class that contains them (although you can get around it 
          if you're determined enough, just like you can get around Java's protections if you work at it).
        
          Since there is a valid use-case for class-private members 
          (namely to avoid name clashes of names with names defined by subclasses), 
          there is limited support for such a mechanism, called name mangling. 
          Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) 
          is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s)
          stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs 
          within the definition of a class.
        
          Name mangling is helpful for letting subclasses override methods without breaking intra-class method calls.
        
                class Car:
                    def __init__(self):
                        self.__val = 10
                        
                    def chnage_val(self, v):
                        self.__val = v
                        print(self.__val)
                        
                c = Car()
                # c.__val   Cannot be accessed here, its can be accessed by metthods inside th class
                c._Car__val = 96    # can be accessed like this; still not as good as Java or C++
                # c.chnage_val(32)
                
          Note this Example:
          class Employee:
              # These values will be shared among all objects of the class
              __location = "New York"
              __raise_pay = 1.0
              __count = 0
            
              def print_loc(self):
                  print(self.__location)
            
          class Dev(Employee):
              pass
            
          my_dev = Dev()
          my_dev.print_loc() # location gets printed
          # even though the instance var location in Employee class is private its being inherited by Developer class
          # its should not happen as per oop principles (in Java, location wont be available in Dev class)
        
        
The Above Protected and Private do not work as good as Java or C++, mostly its a convention ppl follow in py community.
"""


# Python | Method Overloading, (happens inside class methods)
# Like other languages (for example method overloading in C++) do, python does not supports method overloading.
# We may overload the methods but can only use the latest defined method.
# Code need to write, similar to overWriting
def f(n):
    return n + 42


def f(n, m):
    return n + m + 42


print(f(3, 4))

# If you call f with only one parameter, you will raise an exception:
# Yet, it is possible to simulate the overloading behaviour of C++ in Python in this case with a default parameter:


def f(n, m=None):
    if m:
        return n + m + 42
    else:
        return n + 42


print(f(3), f(1, 3))

# --------------------------------------------------------

# Overwriting
# If we overwrite a function, the original function will be gone. The function will be redefined.
# This process has nothing to do with object orientation or inheritance.


def product(a, b):
    p = a * b
    print(p)


# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b * c
    print(p)


# product(4, 5)  shows err

# This line will call the second product method
product(4, 5, 5)