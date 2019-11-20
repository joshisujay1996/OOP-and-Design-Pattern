"""
Multiple Inheritance supported in Python, C++ ; Not in Java

Run through both code and analyze
"""


class car:
    def __init__(self, type1):
        self.type1 = type1

    def print_type(self):
        print("the type of car is ", self.type1)


class bike:
    def __init__(self, type2):
        self.type1 = type2

    def print_type(self):
        print("the type of bike is ", self.type2)

    def pt(self):
        print("hi")


class myclass(car, bike):
    pass


m = myclass('ck')  # by default same method names and vars are inherited from car class;
m.print_type()
m.pt()


# class car:
#     def __init__(self, type1):
#         self.type1 = type1
#
#     def print_type(self):
#         print("the type of car is ", self.type1)
#
#
# class bike:
#     def __init__(self, type2):
#         self.type2 = type2
#
#     def print_type(self):
#         print("the type of bike is ", self.type2)
#
#     def pt(self):
#         print("hi")
#
#
# class myclass(car, bike):
#     def __init__(self, type1, type2):
#         car.__init__(self, type1)
#         bike.__init__(self, type2)
#
#     def print_type(self):
#         print(self.type1, self.type2)
#
#
# m = myclass(type1='ck', type2='gk')
# m.print_type()
# m.pt()