# Just creating module and trying imports


print("module imported")
z = 10


def add_func(x,y):
    print("sum of x and y is {}".format(x+y))


def product_func(x, y):
    print("product of x and y is {}".format(x*y))


class MyClass:
    def __init__(self, val):
        self.values1 = val

    def print_val(self):
        print("The class val is {}".format(self.values1))


def main():
    my_var = 21
    print("my var", my_var)


# Adding this below statement will not run content inside main method when imported as a file in other file;
if "__name__" == "__main__":
    main()