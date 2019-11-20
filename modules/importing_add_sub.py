# Different kinds of import statements for functions; for more info check py docs;
# Before you import module you need to set path see expn in the end of file
import sys

# Normal import (modules is set in sys.path or using pycharm path)
import modules.add_sub_module

import add_sub_module

# We can import it, since the name is long we can give it an alias name (modules is set in sys.path or using pycharm)
import add_sub_module as ass

# can call this way too, but need to mark the relative paths correctly
import modules.add_sub_module

# This is the other way of importing, importing only required modules, and can be directly be called
# can add as to this in the end but you need to import only one like add_fucn or product_func
# Then we can just call is as that name we imported it as;
from add_sub_module import add_func, product_func

# same as above, but we call all functions and variable here
from add_sub_module import *

# Also, note if the dir(OOP-and_design_Pattern; which is set using sys.path.append(...OOD-and_Design-Pattern)
# is above then you call from oop.filename import *; that is you go inside OOD-and_Design-Pattern

# The local variable in that module can be accssed here
print(add_sub_module.z)

# Calling the function here like this
add_sub_module.add_func(10,20)


# This is done using this import statement (import add_sub_module as ass)
ass.add_func(20, 56)

# This below statement is executed by this way of importing (from add_sub_module import add_func, product_func)
add_func(39, 98)
product_func(87, 21)
# Cant get val of variable z defined in add_sub_module

# This below statement is executed by this way of importing (from add_sub_module import *)
add_func(39, 98)
product_func(87, 21)
print(z)
# main()     can import the main method as well
# Now importing the class
my_class = MyClass(100000)
my_class.print_val()


# This path shoudl have the directory where you modules exists in-order for you to import, can do this in pyCharm
# Preference -> Project Structure -> mark the required folder as Source
print(sys.path)

# Else can do it manually like this
# Important note: if the module you are trying to import is not in current dir
# sys.path.append("the abs path of the dir you wnat to add where modules exists")

# instad to the above approaches you can do it in .bash_profiles also;