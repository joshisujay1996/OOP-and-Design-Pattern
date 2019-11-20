"""
Examples of magic method:
__init__, __new__

The __call__ method enables Python programmers to write classes where the instances behave like functions.
Both functions and the instances of such classes are called callables.


We have encountered the concept of operator overloading many times
Example:
    4 + 3
    2.33 + 6.98
    "sujay " + "joshi"

It's even possible to overload the "+" operator as well as all the other operators for the purposes of your own class.
To do this, you need to understand the underlying mechanism.
There is a special (or a "magic") method for every operator sign.
The magic method for the "+" sign is the __add__ method. For "-" it is "__sub__" and so on.

The mechanism works like this: If we have an expression "x + y" and x is an instance of class K,
then Python will check the class definition of K. If K has a method __add__ it will be called with x.__add__(y),
otherwise we will get an error message.

Examples:
    +	    object.__add__(self, other)
    -	    object.__sub__(self, other)
    *	    object.__mul__(self, other)

Comparison Operators
    Operator	    Method
    <	    object.__lt__(self, other)
    <=	    object.__le__(self, other)
    ==	    object.__eq__(self, other)
Unary Operators
    Operator	    Method
    -	    object.__neg__(self)
    +	    object.__pos__(self)

There many more examples online check
"""

