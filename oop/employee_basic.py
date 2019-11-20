"""
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




